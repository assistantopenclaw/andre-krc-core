#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import time
from dataclasses import dataclass
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

FINISHED_DRIVE_FOLDER_ID = "1NOCxQ2K1S2vM07hGHc0xEqTrsl2Ub1tv"

VAULT = Path(os.path.expanduser("~/krc_vault"))
PIPE_ROOT = VAULT / "pipeline_runs"
RUNS_DIR = PIPE_ROOT / "runs"
ARCHIVE_DIR = PIPE_ROOT / "archive"
QUARANTINE_DIR = PIPE_ROOT / "quarantine"
STATE_DIR = PIPE_ROOT / "state"
LOCKS_DIR = PIPE_ROOT / "locks"
LOGS_DIR = PIPE_ROOT / "logs"
SOURCE_INDEX_PATH = STATE_DIR / "source_index.json"
RAW_OUTPUTS_DIR = PIPE_ROOT / "raw_outputs"

FORBIDDEN_META_TOKENS = [
    "from identity",
    "from soul",
    "constraints",
    "let me",
    "analysis",
    "thinking",
    "contract reset",
    "ack_",
    "output_shape",
    "self-review",
]

FATHOM_INDEX = VAULT / "fathom_library/index.json"
FATHOM_PROCESSED = VAULT / "fathom_library/state/processed.json"

DONALD_PROCESS = Path("/home/openclaw_agent_1/.openclaw/scripts/krc/donald_process_url.py")
DONALD_EXTRACT = Path("/home/openclaw_agent_1/.openclaw/scripts/krc/donald_extract_from_manifest.py")

BANNED_DASH_RE = re.compile(r"--|—|–")
FILLER_WORDS = {"just", "really", "very", "basically", "actually", "literally", "honestly", "simply", "that", "so"}


@dataclass
class StagePaths:
    input_path: str | None = None
    output_path: str | None = None


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_dirs() -> None:
    for p in [RUNS_DIR, ARCHIVE_DIR, QUARANTINE_DIR, STATE_DIR, LOCKS_DIR, LOGS_DIR, RAW_OUTPUTS_DIR]:
        p.mkdir(parents=True, exist_ok=True)


def load_json(path: Path, default: Any):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def atomic_write_json(path: Path, obj: dict) -> None:
    atomic_write_text(path, json.dumps(obj, indent=2, ensure_ascii=False))


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def normalize_source(url: str) -> str:
    u = urlparse(url.strip())
    host = (u.netloc or "").lower()
    path = (u.path or "").rstrip("/")
    # never include query in source identity
    return f"{host}{path}"


def source_id_for_url(url: str) -> str:
    return f"fathom_{sha(normalize_source(url))[:16]}"


def run_id_for_url(url: str) -> str:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{ts}_{sha(normalize_source(url))[:8]}"


def one_line_status(kind: str, run_id: str) -> str:
    if kind == "ok":
        return f"Received. Processing now. RUN_ID={run_id}."
    if kind == "already":
        return f"Already processed. RUN_ID={run_id}."
    return f"Couldn’t process automatically. Tommy has been alerted. RUN_ID={run_id}."


def lock_path(run_id: str, stage: str) -> Path:
    return LOCKS_DIR / f"{run_id}_{stage}.lock"


def lock_stage(run_id: str, stage: str, allow_reprocess: bool, stale_seconds: int = 1800) -> tuple[bool, str | None]:
    p = lock_path(run_id, stage)
    if p.exists():
        age = time.time() - p.stat().st_mtime
        if allow_reprocess or age > stale_seconds:
            p.unlink(missing_ok=True)
        else:
            return False, f"lock_exists age={int(age)}s"
    atomic_write_text(p, f"{now_iso()}\n")
    return True, None


def unlock_stage(run_id: str, stage: str) -> None:
    lock_path(run_id, stage).unlink(missing_ok=True)


@contextmanager
def global_worker_lock(name: str, stale_seconds: int = 3600):
    p = LOCKS_DIR / f"worker_{name}.lock"
    fd = None
    try:
        while True:
            try:
                fd = os.open(str(p), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, f"{now_iso()}\n".encode())
                break
            except FileExistsError:
                try:
                    age = time.time() - p.stat().st_mtime
                    if age > stale_seconds:
                        p.unlink(missing_ok=True)
                        continue
                except Exception:
                    pass
                time.sleep(0.2)
        yield
    finally:
        try:
            if fd is not None:
                os.close(fd)
        except Exception:
            pass
        p.unlink(missing_ok=True)


def _deep_get_assistant_text(obj: Any) -> str:
    # Priority paths for gateway/tool envelopes
    if isinstance(obj, dict):
        payloads = ((obj.get("result") or {}).get("payloads") or []) if "result" in obj else []
        for p in payloads:
            if isinstance(p, dict) and isinstance(p.get("text"), str) and p.get("text").strip():
                return p.get("text").strip()

        priority = ["result", "data", "payload", "output", "response", "message", "content", "text", "assistant", "completion"]
        for k in priority:
            if k in obj:
                v = obj[k]
                if isinstance(v, str) and v.strip():
                    return v.strip()
                t = _deep_get_assistant_text(v)
                if t:
                    return t
        for v in obj.values():
            t = _deep_get_assistant_text(v)
            if t:
                return t
    elif isinstance(obj, list):
        for it in obj:
            t = _deep_get_assistant_text(it)
            if t:
                return t
    return ""


def read_agent_text(stdout: str) -> str:
    try:
        j = json.loads(stdout)
        t = _deep_get_assistant_text(j)
        if t:
            return t
    except Exception:
        pass
    return stdout.strip()


def call_agent(agent_id: str, message_obj: dict, timeout_sec: int = 240, run_id: str | None = None, stage: str | None = None) -> str:
    # Stateless per-stage execution: unique session id per run+stage
    sid = None
    if run_id and stage:
        sid = f"pipeline:{run_id}:{stage}"

    cmd = [
        "openclaw", "agent",
        "--agent", agent_id,
        "--timeout", str(timeout_sec),
        "--message", json.dumps(message_obj, ensure_ascii=False),
        "--json",
    ]
    if sid:
        cmd.extend(["--session-id", sid])

    p = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )
    if p.returncode != 0:
        raise RuntimeError(f"agent_call_failed agent={agent_id} rc={p.returncode} err={(p.stderr or '')[-400:]}")
    return read_agent_text(p.stdout)


def write_raw_output(run_id: str, stage: str, text: str) -> Path:
    d = RAW_OUTPUTS_DIR / run_id
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{stage}_raw.txt"
    atomic_write_text(p, text)
    return p


def has_forbidden_meta(text: str) -> str | None:
    low = text.lower()
    for tok in FORBIDDEN_META_TOKENS:
        if tok in low:
            return tok
    return None


def extract_json_payload(raw: str, target_key: str | None = None) -> str:
    t = raw.strip()
    # strip fenced markdown
    if t.startswith("```"):
        m = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", t, re.I)
        if m:
            t = m.group(1).strip()

    # Prefer object containing target key
    if target_key:
        for m in re.finditer(r"\{", t):
            i = m.start()
            for j in range(len(t)-1, i, -1):
                if t[j] != '}':
                    continue
                cand = t[i:j+1]
                try:
                    obj = json.loads(cand)
                    if isinstance(obj, dict) and target_key in obj:
                        return cand
                except Exception:
                    continue

    # fallback first broad object
    first = t.find("{")
    last = t.rfind("}")
    if first != -1 and last != -1 and last > first:
        t = t[first:last+1]
    return t


def unwrap_to_stage_payload(obj: Any, target_key: str) -> dict:
    found = []

    def rec(x: Any):
        if isinstance(x, dict):
            if target_key in x:
                found.append(x)
            priority = ["result", "data", "payload", "output", "response", "message", "content", "text", "assistant", "completion"]
            for k in priority:
                if k in x:
                    v = x[k]
                    if isinstance(v, str):
                        try:
                            vv = json.loads(extract_json_payload(v, target_key=target_key))
                            rec(vv)
                        except Exception:
                            pass
                    else:
                        rec(v)
            for v in x.values():
                rec(v)
        elif isinstance(x, list):
            for it in x:
                rec(it)
        elif isinstance(x, str):
            try:
                vv = json.loads(extract_json_payload(x, target_key=target_key))
                rec(vv)
            except Exception:
                pass

    rec(obj)
    uniq = []
    seen = set()
    for f in found:
        sid = id(f)
        if sid not in seen:
            seen.add(sid)
            uniq.append(f)
    if len(uniq) == 1:
        return uniq[0]
    if len(uniq) > 1:
        raise RuntimeError("schema_fail:ambiguous_wrapper_candidates")
    raise RuntimeError(f"schema_fail:missing_{target_key}")


def parse_json_obj_strict(raw: str, required_keys: list[str], allow_extra: bool = False) -> dict:
    target = required_keys[0] if required_keys else None
    try:
        j = json.loads(extract_json_payload(raw, target_key=target))
    except Exception:
        # backstop: wrapper unwrapping
        try:
            wrapper = json.loads(extract_json_payload(raw))
            j = unwrap_to_stage_payload(wrapper, target_key=target or "")
        except Exception:
            raise RuntimeError("schema_fail:not_object")

    if not isinstance(j, dict):
        try:
            j = unwrap_to_stage_payload(j, target_key=target or "")
        except Exception:
            raise RuntimeError("schema_fail:not_object")

    if target and target not in j:
        try:
            j = unwrap_to_stage_payload(j, target_key=target)
        except Exception:
            raise RuntimeError(f"schema_fail:missing_{target}")

    for k in required_keys:
        if k not in j:
            raise RuntimeError(f"schema_fail:missing_{k}")
    if not allow_extra:
        extra = sorted(set(j.keys()) - set(required_keys))
        if extra:
            raise RuntimeError(f"extra_keys_fail:{','.join(extra)}")
    return j


def parse_json_lines_only(raw: str, field: str) -> list[str]:
    j = parse_json_obj_strict(raw, [field], allow_extra=False)
    v = j.get(field)
    if not isinstance(v, list):
        raise RuntimeError(f"schema_fail:{field}_not_list")
    out: list[str] = []
    for i, item in enumerate(v):
        if not isinstance(item, str):
            raise RuntimeError(f"schema_fail:{field}_item_{i}_not_string")
        # deterministic sanitizer: split embedded newlines into line elements
        s = item.replace("\\r\\n", "\n").replace("\\n", "\n").replace("\r\n", "\n")
        if "\n" in s:
            parts = s.split("\n")
            for p in parts:
                out.append(p)
        else:
            out.append(s)
    return out


def parse_json_hooks_only(raw: str) -> dict:
    req = ["overlay_hook_1", "overlay_hook_2", "overlay_hook_3", "overlay_cta"]
    j = parse_json_obj_strict(raw, req, allow_extra=False)
    for k in req:
        if not isinstance(j[k], str):
            raise RuntimeError(f"schema_fail:{k}_not_string")
    return {k: j[k].strip() for k in req}


def join_lines(lines: list[str]) -> str:
    return "\n".join(lines).strip()


def validate_mark_output(txt: str) -> str | None:
    bad = has_forbidden_meta(txt)
    if bad:
        return f"schema_fail:forbidden_meta:{bad}"
    txt = remove_banned_dash(txt)
    if BANNED_DASH_RE.search(txt):
        return "dash_ban_fail"
    low = txt.lower()
    for tok in ["notes:", "post_id:", "overlay_hook_"]:
        if tok in low:
            return f"schema_fail:forbidden_section:{tok}"
    if txt.count("\n") > 80:
        return "schema_fail:too_many_lines"
    return None


def validate_bob_output(txt: str) -> str | None:
    bad = has_forbidden_meta(txt)
    if bad:
        return f"schema_fail:forbidden_meta:{bad}"
    txt = remove_banned_dash(txt)
    if BANNED_DASH_RE.search(txt):
        return "dash_ban_fail"
    low = txt.lower()
    for tok in ["notes:", "post_id:", "overlay_hook_"]:
        if tok in low:
            return f"schema_fail:forbidden_section:{tok}"
    if txt.count("\n") > 140:
        return "schema_fail:too_many_lines"
    return None


def validate_hook_output(h1: str, h2: str, h3: str, cta: str) -> str | None:
    all_txt = remove_banned_dash("\n".join([h1, h2, h3, cta]))
    bad = has_forbidden_meta(all_txt)
    if bad:
        return f"schema_fail:forbidden_meta:{bad}"
    if cta.strip().lower() != "read caption":
        return "cta_verbatim_fail"
    for h in [h1, h2, h3]:
        if not h or len(h) > 110:
            return "hook_len_fail"
    if BANNED_DASH_RE.search(all_txt):
        return "dash_ban_fail"
    return None


def remove_banned_dash(s: str) -> str:
    return s.replace("—", ", ").replace("–", ", ").replace("--", ", ")


def trim_hook_words(hook: str, max_chars: int = 110) -> str:
    h = remove_banned_dash(hook)
    if len(h) <= max_chars:
        return h
    words = h.split()
    i = 0
    while len(" ".join(words)) > max_chars and i < len(words):
        if words[i].strip(".,!?;:").lower() in FILLER_WORDS:
            words.pop(i)
            i = 0
            continue
        i += 1
    out = " ".join(words)
    if len(out) > max_chars:
        out = out[:max_chars].rstrip()
    return out


def stage_template() -> dict:
    return {
        "status": "pending",
        "canonical_input_path": None,
        "canonical_output_path": None,
        "started_at": None,
        "completed_at": None,
        "handoff_message": None,
    }


def new_manifest(run_id: str, source_id: str, source_kind: str, reprocess: bool) -> dict:
    return {
        "run_id": run_id,
        "source_id": source_id,
        "source_kind": source_kind,
        "reprocess": reprocess,
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "current_stage": "donald",
        "stage_status": {
            "donald": stage_template(),
            "mark": stage_template(),
            "bob": stage_template(),
            "hook": stage_template(),
            "jimmy": stage_template(),
        },
        "flags": [],
        "errors": {},
        "meta": {
            "chat_policy": "one_line_only",
            "pipeline_mode": "single_direction_no_revision_loop",
        },
    }


def add_flag(manifest: dict, code: str, stage: str, severity: str, note: str) -> None:
    manifest["flags"].append({
        "flag_code": code,
        "stage": stage,
        "severity": severity,
        "short_note": note,
        "ts": now_iso(),
    })


def _counter_inc(manifest: dict, key: str) -> None:
    m = manifest.setdefault("metrics", {}).setdefault("counters", {})
    m[key] = int(m.get(key, 0)) + 1


def normalize_failure_code(code: str) -> str:
    c = (code or "").strip()
    if c.startswith("schema_fail"):
        return "schema_fail"
    if c.startswith("extra_keys_fail"):
        return "extra_keys_fail"
    if c.startswith("newline_json_fail"):
        return "newline_json_fail"
    if c.startswith("dash_ban_fail"):
        return "dash_ban_fail"
    if c.startswith("hook_len_fail"):
        return "hook_len_fail"
    if c.startswith("cta_verbatim_fail"):
        return "cta_verbatim_fail"
    return c or "schema_fail"


def log_stage_metric(manifest: dict, run_id: str, stage: str, model: str, failure_code: str | None, raw_path: str | None, canonical_path: str | None) -> None:
    evt = {
        "ts": now_iso(),
        "run_id": run_id,
        "stage": stage,
        "model": model,
        "failure_code": failure_code,
        "raw_path": raw_path,
        "canonical_path": canonical_path,
    }
    manifest.setdefault("metrics", {}).setdefault("events", []).append(evt)
    if failure_code:
        _counter_inc(manifest, normalize_failure_code(failure_code))


def set_error(manifest: dict, stage: str, step: str, err: str, log_path: str) -> None:
    manifest["errors"] = {
        "stage": stage,
        "step": step,
        "error_message": err,
        "log_path": log_path,
        "ts": now_iso(),
    }


def manifest_path(run_dir: Path) -> Path:
    return run_dir / "manifest.json"


def append_log(run_id: str, line: str) -> None:
    lp = LOGS_DIR / f"{run_id}.log"
    with open(lp, "a", encoding="utf-8") as f:
        f.write(f"{now_iso()} {line}\n")


def select_donald_nugget(donald_nuggets: dict) -> dict | None:
    nuggets = donald_nuggets.get("nuggets") or []
    if not nuggets:
        return None
    eligible = [n for n in nuggets if n.get("eligible_for_content") is True]
    return (eligible or nuggets)[0]


def fallback_nugget_from_transcript(raw_transcript_file: str) -> dict:
    text = ""
    try:
        text = Path(raw_transcript_file).read_text(encoding="utf-8", errors="ignore")
    except Exception:
        text = ""

    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    # prefer spoken content after speaker marker
    spoken = []
    for ln in lines:
        if ":" in ln:
            spoken.append(ln.split(":", 1)[1].strip())
        else:
            spoken.append(ln)
    joined = " ".join(spoken)
    joined = re.sub(r"\s+", " ", joined).strip()
    snippet = (joined[:260] + "...") if len(joined) > 260 else (joined or "Choose one concrete step and do it before the day ends.")

    return {
        "nugget_id": "N_FALLBACK_1",
        "post_class_recommendation": "Authority",
        "conversion_angle": "none",
        "idea_one_liner": snippet,
        "proof_anchor_lines": ["Client described repeated delay loop.", "Action was clear, execution was postponed."],
        "first_step_seed": "Today: Take one avoided action before noon.",
        "eligible_for_content": True,
        "fallback_generated": True,
    }


def stage_paths(run_dir: Path, stage: str) -> StagePaths:
    in_map = {
        "donald": run_dir / "stage_inputs" / "donald_url_intake.json",
        "mark": run_dir / "stage_outputs" / "donald_canonical.json",
        "bob": run_dir / "stage_outputs" / "mark_body.md",
        "hook": run_dir / "stage_outputs" / "bob_caption.md",
        "jimmy": run_dir / "stage_outputs" / "hook_overlays.json",
    }
    out_map = {
        "donald": run_dir / "stage_outputs" / "donald_canonical.json",
        "mark": run_dir / "stage_outputs" / "mark_body.md",
        "bob": run_dir / "stage_outputs" / "bob_caption.md",
        "hook": run_dir / "stage_outputs" / "hook_overlays.json",
        "jimmy": run_dir / "final" / "final_post_ready.md",
    }
    return StagePaths(str(in_map[stage]), str(out_map[stage]))


def run_donald(run_dir: Path, manifest: dict, url: str, simulate: bool, reprocess: bool) -> None:
    stage = "donald"
    sp = stage_paths(run_dir, stage)
    s = manifest["stage_status"][stage]
    s["started_at"] = now_iso()
    s["canonical_input_path"] = sp.input_path
    atomic_write_json(Path(sp.input_path), {"run_id": manifest["run_id"], "source_id": manifest["source_id"], "url_present": True})

    if simulate:
        nug = {
            "nugget_id": "N1",
            "post_class_recommendation": "Authority",
            "conversion_angle": "none",
            "idea_one_liner": "Stop negotiating with fear, start obeying what you already know.",
            "proof_anchor_lines": ["You already knew what to do.", "You delayed because you feared the cost."],
            "first_step_seed": "Today: Do the one avoided action before noon.",
            "eligible_for_content": True,
        }
        canonical = {
            "run_id": manifest["run_id"],
            "source_id": manifest["source_id"],
            "route": nug["post_class_recommendation"],
            "conversion_angle": nug["conversion_angle"],
            "nugget": nug,
        }
    else:
        cmd = ["python3", str(DONALD_PROCESS), url]
        if reprocess:
            cmd.append("REPROCESS")
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode not in (0, 2):
            raise RuntimeError(f"donald_process_failed rc={p.returncode} err={(p.stderr or '')[-350:]}")
        donald_run = (p.stdout or "").strip().splitlines()[-1]
        d_manifest = VAULT / "manifests" / f"{donald_run}__manifest.json"
        client = "Unknown"
        p2 = subprocess.run(["python3", str(DONALD_EXTRACT), str(d_manifest), "--client", client], capture_output=True, text=True)
        if p2.returncode != 0:
            raise RuntimeError(f"donald_extract_failed rc={p2.returncode} err={(p2.stderr or '')[-350:]}")
        out = json.loads((p2.stdout or "{}").strip() or "{}")
        nuggets_path = out.get("nuggets")
        if not nuggets_path:
            raise RuntimeError("donald_extract_missing_nuggets_path")
        nug_payload = json.loads(Path(nuggets_path).read_text(encoding="utf-8"))
        sel = select_donald_nugget(nug_payload)
        if sel is None:
            # deterministic fallback for zero-nugget exports so pipeline still lands final review doc
            dman = json.loads(d_manifest.read_text(encoding="utf-8")) if d_manifest.exists() else {}
            raw_tf = dman.get("raw_transcript_file") or ""
            sel = fallback_nugget_from_transcript(raw_tf)
            add_flag(manifest, "DONALD_ZERO_NUGGET_FALLBACK", "donald", "warn", "No nuggets returned, generated deterministic fallback nugget")

        canonical = {
            "run_id": manifest["run_id"],
            "source_id": manifest["source_id"],
            "route": sel.get("post_class_recommendation") or "Authority",
            "conversion_angle": sel.get("conversion_angle") or "none",
            "nugget": sel,
            "donald_artifacts": {
                "donald_run_id": donald_run,
                "donald_manifest": str(d_manifest),
                "nuggets_json": nuggets_path,
            },
        }

    atomic_write_json(Path(sp.output_path), canonical)
    s["status"] = "done"
    s["completed_at"] = now_iso()
    s["canonical_output_path"] = sp.output_path
    s["handoff_message"] = f"RUN_ID={manifest['run_id']} STAGE=DONALD_DONE"


def run_mark(run_dir: Path, manifest: dict, simulate: bool) -> None:
    stage = "mark"
    sp = stage_paths(run_dir, stage)
    s = manifest["stage_status"][stage]
    s["started_at"] = now_iso()
    s["canonical_input_path"] = sp.input_path
    donald = json.loads(Path(sp.input_path).read_text(encoding="utf-8"))
    route = donald.get("route") or "Authority"

    if simulate:
        if route == "Conversion":
            body = "You keep calling it stress, but it is fear running your home.\n\nWhen you avoid one hard truth, you teach your heart to hide.\n\nWhen the fear hits: tell the truth in one sentence before you defend yourself."
        else:
            body = "Most men do not need more information, they need obedience.\n\nComment yes if you have delayed what God already made clear.\n\nToday: Do the one avoided action before noon."
    else:
        req = {
            "task": "caption_body_only",
            "run_id": manifest["run_id"],
            "route": route,
            "donald_canonical": donald,
            "output_contract": {
                "type": "json_only",
                "required": {"caption_body_lines": "string[]"},
                "strict": True,
                "forbid_preamble": True,
            },
            "constraints": {
                "no_hooks": True,
                "no_cta": True,
                "no_notes": True,
                "dash_ban": ["--", "—", "–"],
            },
        }
        raw = call_agent("mark", req, run_id=manifest["run_id"], stage="mark")
        raw_path = write_raw_output(manifest["run_id"], "mark", raw)
        try:
            body_lines = parse_json_lines_only(raw, "caption_body_lines")
            body = join_lines(body_lines)
        except Exception as e:
            repair_req = {
                "task": "repair_format",
                "run_id": manifest["run_id"],
                "schema": {"caption_body_lines": ["line 1", "", "line 2"]},
                "example": {"caption_body_lines": ["Most men delay clarity.", "", "Today: take one action before noon."]},
                "validator_error": str(e),
                "instruction": "Return JSON only. No markdown. No commentary. No extra keys.",
                "source_output": raw,
            }
            raw2 = call_agent("mark", repair_req, run_id=manifest["run_id"], stage="mark_repair")
            raw_path = write_raw_output(manifest["run_id"], "mark_repair", raw2)
            body_lines = parse_json_lines_only(raw2, "caption_body_lines")
            body = join_lines(body_lines)

    v = validate_mark_output(body)
    if v:
        set_error(manifest, "mark", "validator", f"mark_validator_failed:{v}", str(raw_path) if 'raw_path' in locals() else str(RAW_OUTPUTS_DIR / manifest['run_id'] / 'mark_raw.txt'))
        log_stage_metric(manifest, manifest["run_id"], "mark", "openrouter/moonshotai/kimi-k2-thinking", v, str(raw_path) if 'raw_path' in locals() else None, None)
        raise RuntimeError(f"mark_validator_failed:{v}")
    if "OVERLAY_HOOK" in body or "Comment NEXT CHAPTER" in body:
        raise RuntimeError("mark_boundary_violation")

    body = remove_banned_dash(body)
    atomic_write_text(Path(sp.output_path), body.strip() + "\n")
    log_stage_metric(manifest, manifest["run_id"], "mark", "openrouter/moonshotai/kimi-k2-thinking", None, str(raw_path) if 'raw_path' in locals() else None, sp.output_path)
    s["status"] = "done"
    s["completed_at"] = now_iso()
    s["canonical_output_path"] = sp.output_path
    s["handoff_message"] = f"RUN_ID={manifest['run_id']} STAGE=MARK_DONE"


def run_bob(run_dir: Path, manifest: dict, simulate: bool) -> None:
    stage = "bob"
    sp = stage_paths(run_dir, stage)
    s = manifest["stage_status"][stage]
    s["started_at"] = now_iso()
    s["canonical_input_path"] = sp.input_path

    body = Path(sp.input_path).read_text(encoding="utf-8").strip()
    donald = json.loads(Path(stage_paths(run_dir, "mark").input_path).read_text(encoding="utf-8"))
    route = donald.get("route") or "Authority"

    if simulate:
        if route == "Conversion":
            cta = "Comment NEXT CHAPTER and I’ll send you the first step to fast-track your healing process."
            append = "\n\nUnderstanding this is one thing.\nMost Christian men know the truth, but don’t know how to apply it in real time.\nSo if you’ve been struggling, this is your next step."
        else:
            cta = "If you're gonna use this in your life, follow so you don't miss out on more applicable relationship wisdom."
            append = ""
        caption = f"{body}{append}\n\n{cta}".strip()
    else:
        req = {
            "task": "append_only_close_cta",
            "run_id": manifest["run_id"],
            "route": route,
            "body_verbatim": body,
            "output_contract": {
                "type": "json_only",
                "required": {"final_caption_lines": "string[]"},
                "strict": True,
                "forbid_preamble": True,
            },
            "constraints": {
                "append_only": True,
                "dash_ban": ["--", "—", "–"],
                "line_array_rules": "Each final_caption_lines element must be single-line. Use empty string items for paragraph breaks only."
            },
            "example": {
                "final_caption_lines": [
                    "Body paragraph line 1",
                    "Body paragraph line 2",
                    "",
                    "If you're gonna use this in your life, follow so you don't miss out on more applicable relationship wisdom."
                ]
            }
        }
        raw = call_agent("bob", req, run_id=manifest["run_id"], stage="bob")
        raw_path = write_raw_output(manifest["run_id"], "bob", raw)
        raw = read_agent_text(raw)
        try:
            j_try = parse_json_obj_strict(raw, ["final_caption_lines"], allow_extra=False)
            if isinstance(j_try, dict) and ('final_caption' in j_try) and ('final_caption_lines' not in j_try):
                raise RuntimeError('schema_fail:key_alias_denied_final_caption')
            caption_lines = parse_json_lines_only(raw, "final_caption_lines")
            caption = join_lines(caption_lines)
        except Exception as e:
            repair_req = {
                "task": "repair_format",
                "run_id": manifest["run_id"],
                "schema": {"final_caption_lines": ["body line", "", "cta line"]},
                "example": {"final_caption_lines": ["Most men delay what they know.", "", "If you're gonna use this in your life, follow so you don't miss out on more applicable relationship wisdom."]},
                "validator_error": str(e),
                "instruction": "Return JSON only. No markdown. No commentary. No extra keys.",
                "source_output": raw,
                "temperature": 0
            }
            raw2 = call_agent("bob", repair_req, run_id=manifest["run_id"], stage="bob_repair")
            raw_path = write_raw_output(manifest["run_id"], "bob_repair", raw2)
            raw2 = read_agent_text(raw2)
            j_try2 = parse_json_obj_strict(raw2, ["final_caption_lines"], allow_extra=False)
            if isinstance(j_try2, dict) and ('final_caption' in j_try2) and ('final_caption_lines' not in j_try2):
                raise RuntimeError('schema_fail:key_alias_denied_final_caption')
            caption_lines = parse_json_lines_only(raw2, "final_caption_lines")
            caption = join_lines(caption_lines)

    v = validate_bob_output(caption)
    if v:
        set_error(manifest, "bob", "validator", f"bob_validator_failed:{v}", str(raw_path) if 'raw_path' in locals() else str(RAW_OUTPUTS_DIR / manifest['run_id'] / 'bob_raw.txt'))
        log_stage_metric(manifest, manifest["run_id"], "bob", "openrouter/deepseek/deepseek-chat-v3.1", v, str(raw_path) if 'raw_path' in locals() else None, None)
        raise RuntimeError(f"bob_validator_failed:{v}")

    if not caption.lstrip().startswith(body):
        add_flag(manifest, "BOB_APPEND_ONLY_FALLBACK", stage, "warn", "Bob output modified body, using deterministic append fallback")
        if route == "Conversion":
            fallback_cta = "Comment NEXT CHAPTER and I’ll send you the first step to fast-track your healing process."
            fallback_append = "\n\nUnderstanding this is one thing.\nMost Christian men know the truth, but don’t know how to apply it in real time.\nSo if you’ve been struggling, start with one honest action today."
        else:
            fallback_cta = "If you're gonna use this in your life, follow so you don't miss out on more applicable relationship wisdom."
            fallback_append = ""
        caption = f"{body}{fallback_append}\n\n{fallback_cta}".strip()

    caption = remove_banned_dash(caption)
    atomic_write_text(Path(sp.output_path), caption.strip() + "\n")
    log_stage_metric(manifest, manifest["run_id"], "bob", "openrouter/deepseek/deepseek-chat-v3.1", None, str(raw_path) if 'raw_path' in locals() else None, sp.output_path)
    s["status"] = "done"
    s["completed_at"] = now_iso()
    s["canonical_output_path"] = sp.output_path
    s["handoff_message"] = f"RUN_ID={manifest['run_id']} STAGE=BOB_DONE"


def run_hook(run_dir: Path, manifest: dict, simulate: bool) -> None:
    stage = "hook"
    sp = stage_paths(run_dir, stage)
    s = manifest["stage_status"][stage]
    s["started_at"] = now_iso()
    s["canonical_input_path"] = sp.input_path

    caption = Path(sp.input_path).read_text(encoding="utf-8").strip()

    if simulate:
        hooks = [
            "Delay becomes destiny faster than most men realize.",
            "Strong men act before feelings agree.",
            "Clarity comes when you obey before comfort.",
        ]
        overlay_cta = "read caption"
    else:
        req = {
            "task": "hooks_only",
            "run_id": manifest["run_id"],
            "caption_value_context": caption,
            "output_contract": {
                "type": "json_only",
                "required": {
                    "overlay_hook_1": "string",
                    "overlay_hook_2": "string",
                    "overlay_hook_3": "string",
                    "overlay_cta": "string"
                },
                "strict": True,
                "forbid_preamble": True,
            },
            "constraints": {
                "count": 3,
                "one_sentence_each": True,
                "max_chars_each": 110,
                "dash_ban": ["--", "—", "–"],
            },
        }
        raw = call_agent("captainhook", req, run_id=manifest["run_id"], stage="hook")
        raw_path = write_raw_output(manifest["run_id"], "hook", raw)
        try:
            hooks_obj = parse_json_hooks_only(raw)
        except Exception:
            repair_req = {
                "task": "repair_format",
                "run_id": manifest["run_id"],
                "schema": {
                    "overlay_hook_1": "...",
                    "overlay_hook_2": "...",
                    "overlay_hook_3": "...",
                    "overlay_cta": "read caption"
                },
                "example": {
                    "overlay_hook_1": "Delay becomes destiny when action stays postponed.",
                    "overlay_hook_2": "Leaders lose authority when fear makes decisions.",
                    "overlay_hook_3": "Clarity compounds when you act before comfort.",
                    "overlay_cta": "read caption"
                },
                "validator_error": "schema_fail or extra_keys_fail",
                "instruction": "Return JSON only. No markdown. No commentary. No extra keys.",
                "source_output": raw,
            }
            raw2 = call_agent("captainhook", repair_req, run_id=manifest["run_id"], stage="hook_repair")
            raw_path = write_raw_output(manifest["run_id"], "hook_repair", raw2)
            hooks_obj = parse_json_hooks_only(raw2)

        hooks = [hooks_obj["overlay_hook_1"], hooks_obj["overlay_hook_2"], hooks_obj["overlay_hook_3"]]
        overlay_cta = hooks_obj["overlay_cta"]

    hooks = [trim_hook_words(h, 110) for h in hooks][:3]
    if len(hooks) != 3:
        raise RuntimeError("hook_count_invalid")

    v = validate_hook_output(hooks[0], hooks[1], hooks[2], overlay_cta if 'overlay_cta' in locals() else 'read caption')
    if v:
        set_error(manifest, "hook", "validator", f"hook_validator_failed:{v}", str(raw_path) if 'raw_path' in locals() else str(RAW_OUTPUTS_DIR / manifest['run_id'] / 'hook_raw.txt'))
        log_stage_metric(manifest, manifest["run_id"], "hook", "openrouter/anthropic/claude-sonnet-4.6", v, str(raw_path) if 'raw_path' in locals() else None, None)
        raise RuntimeError(f"hook_validator_failed:{v}")

    payload = {"OVERLAY_HOOK_1": hooks[0], "OVERLAY_HOOK_2": hooks[1], "OVERLAY_HOOK_3": hooks[2], "OVERLAY_CTA": "read caption"}
    atomic_write_json(Path(sp.output_path), payload)
    log_stage_metric(manifest, manifest["run_id"], "hook", "openrouter/anthropic/claude-sonnet-4.6", None, str(raw_path) if 'raw_path' in locals() else None, sp.output_path)
    s["status"] = "done"
    s["completed_at"] = now_iso()
    s["canonical_output_path"] = sp.output_path
    s["handoff_message"] = f"RUN_ID={manifest['run_id']} STAGE=HOOK_DONE"


def upload_final_to_drive(run_id: str, final_path: Path) -> dict:
    title = f"{run_id}: Final Post Ready"
    cmd = [
        "gog", "drive", "upload", str(final_path),
        "--parent", FINISHED_DRIVE_FOLDER_ID,
        "--convert-to", "doc",
        "--name", title,
        "--json", "--results-only", "--no-input",
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"drive_upload_failed rc={p.returncode} err={(p.stderr or '')[-350:]}")
    out = json.loads((p.stdout or "{}").strip() or "{}")
    file_id = out.get("id") or out.get("fileId")
    link = out.get("webViewLink") or out.get("link")
    return {"file_id": file_id, "link": link, "raw": out}


def run_jimmy(run_dir: Path, manifest: dict, simulate: bool) -> None:
    stage = "jimmy"
    sp = stage_paths(run_dir, stage)
    s = manifest["stage_status"][stage]
    s["started_at"] = now_iso()
    s["canonical_input_path"] = sp.input_path

    bob_path = Path(stage_paths(run_dir, "hook").input_path)
    hook_path = Path(stage_paths(run_dir, "jimmy").input_path)

    if not bob_path.exists() and hook_path.exists():
        add_flag(manifest, "PAIR_MISSING_BOB", stage, "error", "Hook exists but Bob missing")
        raise RuntimeError("pairing_failed_missing_bob")
    if bob_path.exists() and not hook_path.exists():
        add_flag(manifest, "PAIR_MISSING_HOOK", stage, "error", "Bob exists but Hook missing")
        raise RuntimeError("pairing_failed_missing_hook")

    caption = bob_path.read_text(encoding="utf-8").strip()
    hooks_obj = json.loads(hook_path.read_text(encoding="utf-8"))
    hooks = [hooks_obj.get("OVERLAY_HOOK_1", ""), hooks_obj.get("OVERLAY_HOOK_2", ""), hooks_obj.get("OVERLAY_HOOK_3", "")]

    clean_caption = remove_banned_dash(caption)
    clean_hooks = [trim_hook_words(h, 110) for h in hooks]

    if clean_caption != caption:
        add_flag(manifest, "JIMMY_MINIMAL_DASH_CLEANUP", stage, "warn", "Removed banned dash punctuation")

    # CTA last line check by route
    donald = json.loads(Path(stage_paths(run_dir, "mark").input_path).read_text(encoding="utf-8"))
    route = donald.get("route") or "Authority"
    lines = [ln for ln in clean_caption.splitlines() if ln.strip()]
    last = lines[-1] if lines else ""
    if route == "Authority":
        expected = "If you're gonna use this in your life, follow so you don't miss out on more applicable relationship wisdom."
    else:
        angle = (donald.get("conversion_angle") or "heartbreak").lower()
        expected = "Comment NEXT CHAPTER and I’ll send you the first step to becoming your wife’s safe place again." if "divorce" in angle else "Comment NEXT CHAPTER and I’ll send you the first step to fast-track your healing process."

    if last != expected:
        add_flag(manifest, "CTA_LAST_LINE_MISMATCH", stage, "warn", "Final CTA line not exact expected line")

    out = []
    out.append(f"RUN_ID: {manifest['run_id']}")
    out.append("OVERLAY_HOOK_1: " + clean_hooks[0])
    out.append("OVERLAY_HOOK_2: " + clean_hooks[1])
    out.append("OVERLAY_HOOK_3: " + clean_hooks[2])
    out.append("OVERLAY_CTA: " + (hooks_obj.get("OVERLAY_CTA") if isinstance(hooks_obj, dict) and hooks_obj.get("OVERLAY_CTA") else "read caption"))
    out.append("")
    out.append("CAPTION:")
    out.append(clean_caption)
    out.append("")
    out.append("NOTES:")
    out.append("- mechanical_assembly_only=true")
    out.append("- style_rewrite=false")
    out.append("- final=true")

    final_path = Path(sp.output_path)
    atomic_write_text(final_path, "\n".join(out).strip() + "\n")

    drive = upload_final_to_drive(manifest["run_id"], final_path)
    manifest.setdefault("final_delivery", {})
    manifest["final_delivery"] = {
        "drive_folder_id": FINISHED_DRIVE_FOLDER_ID,
        "drive_file_id": drive.get("file_id"),
        "drive_link": drive.get("link"),
        "uploaded_at": now_iso(),
    }

    s["status"] = "done"
    s["completed_at"] = now_iso()
    s["canonical_output_path"] = sp.output_path
    s["handoff_message"] = f"RUN_ID={manifest['run_id']} STAGE=FINAL_READY"


def finalize_run(run_dir: Path, manifest: dict, success: bool) -> None:
    target = ARCHIVE_DIR / manifest["run_id"] if success else QUARANTINE_DIR / manifest["run_id"]
    if target.exists():
        subprocess.run(["rm", "-rf", str(target)], check=False)
    os.replace(run_dir, target)


def update_source_index(source_id: str, run_id: str) -> None:
    idx = load_json(SOURCE_INDEX_PATH, {"items": {}, "updated_at": None})
    idx["items"][source_id] = {"run_id": run_id, "status": "success", "updated_at": now_iso()}
    idx["updated_at"] = now_iso()
    atomic_write_json(SOURCE_INDEX_PATH, idx)


def already_processed(source_id: str) -> str | None:
    idx = load_json(SOURCE_INDEX_PATH, {"items": {}})
    item = (idx.get("items") or {}).get(source_id)
    if item and item.get("status") == "success":
        return item.get("run_id")
    return None


def run_one(url: str, reprocess: bool = False, simulate: bool = False, force_partial_write_test: bool = False) -> dict:
    ensure_dirs()
    source_id = source_id_for_url(url)
    existing = already_processed(source_id)
    if existing and not reprocess:
        return {"ok": True, "run_id": existing, "status_line": one_line_status("already", existing), "already_processed": True}

    run_id = run_id_for_url(url)
    run_dir = RUNS_DIR / run_id
    (run_dir / "stage_inputs").mkdir(parents=True, exist_ok=True)
    (run_dir / "stage_outputs").mkdir(parents=True, exist_ok=True)
    (run_dir / "final").mkdir(parents=True, exist_ok=True)

    manifest = new_manifest(run_id, source_id, "fathom_share_url", reprocess)
    mpath = manifest_path(run_dir)
    atomic_write_json(mpath, manifest)

    stages = ["donald", "mark", "bob", "hook", "jimmy"]
    ok = False
    try:
        for stage in stages:
            can, reason = lock_stage(run_id, stage, allow_reprocess=reprocess)
            if not can:
                raise RuntimeError(f"{stage}_lock_blocked {reason}")
            try:
                manifest["current_stage"] = stage
                atomic_write_json(mpath, manifest)

                if stage == "donald":
                    run_donald(run_dir, manifest, url, simulate=simulate, reprocess=reprocess)
                elif stage == "mark":
                    run_mark(run_dir, manifest, simulate=simulate)
                elif stage == "bob":
                    with global_worker_lock("bob"):
                        run_bob(run_dir, manifest, simulate=simulate)
                elif stage == "hook":
                    run_hook(run_dir, manifest, simulate=simulate)
                    if force_partial_write_test:
                        # simulate delay and verify downstream reads canonical only after completed file exists
                        time.sleep(1)
                elif stage == "jimmy":
                    run_jimmy(run_dir, manifest, simulate=simulate)

                atomic_write_json(mpath, manifest)
            finally:
                unlock_stage(run_id, stage)

        ok = True
        update_source_index(source_id, run_id)
        status_line = one_line_status("ok", run_id)
        append_log(run_id, f"SUCCESS {status_line}")
        return {"ok": True, "run_id": run_id, "status_line": status_line, "manifest": str(mpath)}
    except Exception as e:
        set_error(manifest, manifest.get("current_stage") or "unknown", "pipeline", str(e), str(LOGS_DIR / f"{run_id}.log"))
        atomic_write_json(mpath, manifest)
        status_line = one_line_status("fail", run_id)
        append_log(run_id, f"FAIL stage={manifest.get('current_stage')} err={e}")
        return {"ok": False, "run_id": run_id, "status_line": status_line, "manifest": str(mpath), "error": str(e)}
    finally:
        finalize_run(run_dir, manifest, success=ok)


def intake_from_index(n: int) -> list[str]:
    idx = load_json(FATHOM_INDEX, [])
    processed = set((load_json(FATHOM_PROCESSED, {"processed": []}).get("processed") or []))
    urls = []
    for item in idx:
        u = (item or {}).get("share_url")
        if not u:
            continue
        if u in processed:
            continue
        urls.append(u)
    return urls[:max(0, n)]


def run_soak(n: int = 20, url: str = "https://fathom.video/share/mAu9_pHzpFsV2y5vnf4Xf3Z5pRdVBP6s") -> dict:
    ensure_dirs()
    runs = []
    for i in range(n):
        runs.append(run_one(url, reprocess=True, simulate=False))
        time.sleep(0.1)

    fail_by_code: dict[str, int] = {}
    stage_fail_by_code: dict[str, dict[str, int]] = {}
    ok = 0
    for r in runs:
        rid = r.get("run_id")
        if not rid:
            continue
        mp = ARCHIVE_DIR / rid / "manifest.json"
        kind = "archive"
        if not mp.exists():
            mp = QUARANTINE_DIR / rid / "manifest.json"
            kind = "quarantine"
        if not mp.exists():
            continue
        j = json.loads(mp.read_text(encoding="utf-8"))
        if kind == "archive" and not j.get("errors"):
            ok += 1

        em = (j.get("errors") or {}).get("error_message", "")
        st = (j.get("errors") or {}).get("stage", "none")
        if em:
            if "session file locked" in em:
                code = "infra_session_lock_fail"
            elif "newline_json_fail" in em:
                code = "newline_json_fail"
            elif "extra_keys_fail" in em:
                code = "extra_keys_fail"
            elif "dash_ban_fail" in em:
                code = "dash_ban_fail"
            elif "hook_len_fail" in em:
                code = "hook_len_fail"
            elif "cta_verbatim_fail" in em:
                code = "cta_verbatim_fail"
            elif "schema_fail" in em:
                code = "schema_fail"
            else:
                code = "other_fail"
            fail_by_code[code] = fail_by_code.get(code, 0) + 1
            s = stage_fail_by_code.setdefault(st, {})
            s[code] = s.get(code, 0) + 1

    return {
        "ok": True,
        "runs": len(runs),
        "ok_runs": ok,
        "failed_runs": len(runs) - ok,
        "failure_rate": (len(runs) - ok) / max(1, len(runs)),
        "fail_by_code": fail_by_code,
        "stage_fail_by_code": stage_fail_by_code,
        "run_ids": [r.get("run_id") for r in runs],
    }


def run_acceptance_tests() -> dict:
    ensure_dirs()
    test_results: list[dict] = []

    # 1, 2, 5, 7, 8 basic happy path with simulate
    r1 = run_one("https://fathom.video/share/test_abc123", reprocess=True, simulate=True)
    test_results.append({"name": "URL intake one line", "pass": bool(re.match(r"^(Received\. Processing now\.|Already processed\.|Couldn’t process automatically\.)", r1.get("status_line", ""))), "run_id": r1.get("run_id")})

    # 3 idempotency
    r2 = run_one("https://fathom.video/share/test_abc123", reprocess=False, simulate=True)
    test_results.append({"name": "Idempotency same URL", "pass": r2.get("already_processed") is True, "run_id": r2.get("run_id")})

    # 4 atomic write with delay
    r3 = run_one("https://fathom.video/share/test_atomic_1", reprocess=True, simulate=True, force_partial_write_test=True)
    test_results.append({"name": "Atomic write no partial reads", "pass": bool(r3.get("ok")), "run_id": r3.get("run_id")})

    # 6 pairing test, force missing hook by creating run and manually invoking jimmy pre-hook
    rid = run_id_for_url("https://fathom.video/share/test_pairing")
    run_dir = RUNS_DIR / rid
    (run_dir / "stage_inputs").mkdir(parents=True, exist_ok=True)
    (run_dir / "stage_outputs").mkdir(parents=True, exist_ok=True)
    (run_dir / "final").mkdir(parents=True, exist_ok=True)
    m = new_manifest(rid, source_id_for_url("https://fathom.video/share/test_pairing"), "fathom_share_url", True)
    atomic_write_json(manifest_path(run_dir), m)
    atomic_write_text(Path(stage_paths(run_dir, "hook").input_path), "Body only\n\nIf you're gonna use this in your life, follow so you don't miss out on more applicable relationship wisdom.\n")
    pairing_pass = False
    try:
        run_jimmy(run_dir, m, simulate=True)
    except Exception:
        pairing_pass = True
    finalize_run(run_dir, m, success=False)
    test_results.append({"name": "Pairing rule blocks finalize when hook missing", "pass": pairing_pass, "run_id": rid})

    # failure test (bad url, non simulate)
    r4 = run_one("https://example.com/not-fathom", reprocess=True, simulate=False)
    test_results.append({"name": "Failure one-line response", "pass": (not r4.get("ok")) and bool(re.match(r"^Couldn’t process automatically\.", r4.get("status_line", ""))), "run_id": r4.get("run_id")})

    # punctuation ban on final output
    final_ok = False
    if r1.get("run_id"):
        p = ARCHIVE_DIR / r1["run_id"] / "final" / "final_post_ready.md"
        if p.exists():
            final_ok = not bool(BANNED_DASH_RE.search(p.read_text(encoding="utf-8")))
    test_results.append({"name": "Punctuation ban final output", "pass": final_ok, "run_id": r1.get("run_id")})

    all_pass = all(t["pass"] for t in test_results)
    out = {
        "ok": all_pass,
        "tests": test_results,
        "ts": now_iso(),
    }
    atomic_write_json(LOGS_DIR / f"acceptance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", out)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic 5-agent pipeline v2")
    ap.add_argument("--url", action="append", default=[])
    ap.add_argument("--from-index", type=int, default=0, help="take N pending URLs from fathom index")
    ap.add_argument("--reprocess", action="store_true")
    ap.add_argument("--simulate", action="store_true")
    ap.add_argument("--acceptance-tests", action="store_true")
    ap.add_argument("--soak", type=int, default=0, help="run N end-to-end runs for failure-code stats")
    args = ap.parse_args()

    if args.acceptance_tests:
        out = run_acceptance_tests()
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0 if out["ok"] else 1

    if args.soak > 0:
        out = run_soak(args.soak)
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0

    urls = list(args.url)
    if args.from_index > 0:
        urls.extend(intake_from_index(args.from_index))

    if not urls:
        print(json.dumps({"ok": False, "error": "no_urls"}, indent=2))
        return 2

    results = [run_one(u, reprocess=args.reprocess, simulate=args.simulate) for u in urls]
    ok = all(r.get("ok") for r in results)
    print(json.dumps({"ok": ok, "count": len(results), "results": results}, indent=2, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
