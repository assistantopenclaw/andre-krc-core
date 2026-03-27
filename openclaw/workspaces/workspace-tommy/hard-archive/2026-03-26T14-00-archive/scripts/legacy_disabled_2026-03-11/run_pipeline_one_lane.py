#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VAULT_ROOT = Path(os.path.expanduser(os.environ.get('KRC_VAULT_ROOT', '/home/openclaw_agent_1/krc_vault')))
RUNS_ROOT = VAULT_ROOT / 'runs'
QUARANTINE_ROOT = VAULT_ROOT / 'quarantine'
EXPORT_ROOT = VAULT_ROOT / 'google_drive_exports'
LOCK_PATH = VAULT_ROOT / 'pipeline.lock'
LOCK_TTL_SEC = 60 * 45

DONALD_PROCESS = '/home/openclaw_agent_1/.openclaw/scripts/krc/donald_process_url.py'
DONALD_EXTRACT = '/home/openclaw_agent_1/.openclaw/scripts/krc/donald_extract_from_manifest.py'

FORBIDDEN_META = ['thinking', 'analysis', 'prime directive', 'here is my output', '```']
JIMMY_AGENT = os.environ.get('KRC_JIMMY_AGENT', 'jimmy')


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def run_id_for(source: str) -> str:
    import hashlib
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    h = hashlib.sha256(source.encode()).hexdigest()[:8]
    return f'{ts}_{h}'


def read_json(p: Path, default: Any = None):
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding='utf-8'))


def write_text_atomic(p: Path, s: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    t = p.with_suffix(p.suffix + '.tmp')
    t.write_text(s, encoding='utf-8')
    os.replace(t, p)


def write_json_atomic(p: Path, obj: Any):
    write_text_atomic(p, json.dumps(obj, indent=2, ensure_ascii=False))


def acquire_global_lock(run_id: str) -> tuple[bool, str]:
    VAULT_ROOT.mkdir(parents=True, exist_ok=True)
    if LOCK_PATH.exists():
        age = time.time() - LOCK_PATH.stat().st_mtime
        if age <= LOCK_TTL_SEC:
            return False, 'busy'
        # stale lock
        stale_note = VAULT_ROOT / 'stalled_runs.log'
        with open(stale_note, 'a', encoding='utf-8') as f:
            f.write(f'{now_iso()} prior_lock_stale age_sec={int(age)}\n')
        LOCK_PATH.unlink(missing_ok=True)
    write_text_atomic(LOCK_PATH, f'run_id={run_id}\nstarted_at={now_iso()}\n')
    return True, 'acquired'


def release_global_lock():
    LOCK_PATH.unlink(missing_ok=True)


def fail_closed(run_root: Path, stage: str, reason: str, paths: list[str]):
    q = QUARANTINE_ROOT / run_root.name
    q.parent.mkdir(parents=True, exist_ok=True)
    if q.exists():
        shutil.rmtree(q)
    shutil.copytree(run_root, q)
    write_text_atomic(run_root / 'FAILURE.txt', f'stage={stage} reason={reason} paths={";".join(paths)}\n')


def deep_assistant_text(obj: Any) -> str:
    if isinstance(obj, dict):
        payloads = ((obj.get('result') or {}).get('payloads') or [])
        for p in payloads:
            if isinstance(p, dict) and isinstance(p.get('text'), str) and p.get('text').strip():
                return p['text'].strip()
        for k in ['result', 'data', 'payload', 'output', 'response', 'message', 'content', 'text', 'assistant', 'completion']:
            if k in obj:
                v = obj[k]
                if isinstance(v, str) and v.strip():
                    return v.strip()
                t = deep_assistant_text(v)
                if t:
                    return t
        for v in obj.values():
            t = deep_assistant_text(v)
            if t:
                return t
    elif isinstance(obj, list):
        for v in obj:
            t = deep_assistant_text(v)
            if t:
                return t
    return ''


def clear_agent_session_locks(agent: str):
    # Best-effort cleanup for stale session locks
    sess_dir = Path(f'/home/openclaw_agent_1/.openclaw/agents/{agent}/sessions')
    if sess_dir.exists():
        for p in sess_dir.glob('*.jsonl.lock'):
            try:
                p.unlink(missing_ok=True)
            except Exception:
                pass


def call_agent(agent: str, message_obj: dict, session_id: str, raw_path: Path) -> str:
    # Force unique session id per call to avoid any session file reuse
    session_id = f"{session_id}:{uuid.uuid4().hex[:8]}"
    clear_agent_session_locks(agent)
    p = subprocess.run([
        'openclaw', 'agent', '--agent', agent, '--session-id', session_id,
        '--timeout', '420', '--message', json.dumps(message_obj, ensure_ascii=False), '--json'
    ], capture_output=True, text=True)
    raw_out = (p.stdout or '') + ('\n[stderr]\n' + (p.stderr or ''))
    write_text_atomic(raw_path, raw_out)
    if p.returncode != 0:
        # One retry after clearing locks again
        clear_agent_session_locks(agent)
        p2 = subprocess.run([
            'openclaw', 'agent', '--agent', agent, '--session-id', session_id,
            '--timeout', '420', '--message', json.dumps(message_obj, ensure_ascii=False), '--json'
        ], capture_output=True, text=True)
        raw_out2 = (p2.stdout or '') + ('\n[stderr]\n' + (p2.stderr or ''))
        write_text_atomic(raw_path.with_suffix('.retry.txt'), raw_out2)
        if p2.returncode != 0:
            raise RuntimeError(f'agent_call_failed:{agent}:{p2.returncode}')
        p = p2

    try:
        j = json.loads(p.stdout)
        txt = deep_assistant_text(j)
        if txt:
            return txt
    except Exception:
        pass
    return (p.stdout or '').strip()


def json_extract(text: str, target_key: str) -> dict:
    t = text.strip()
    if t.startswith('```'):
        m = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', t, re.I)
        if m:
            t = m.group(1).strip()
    # prefer object containing target key
    for m in re.finditer(r'\{', t):
        i = m.start()
        for j in range(len(t)-1, i, -1):
            if t[j] != '}':
                continue
            cand = t[i:j+1]
            try:
                obj = json.loads(cand)
                if isinstance(obj, dict) and target_key in obj:
                    return obj
            except Exception:
                pass
    # fallback full parse
    obj = json.loads(t)
    if isinstance(obj, dict):
        return obj
    raise RuntimeError('json_not_object')


def validate_no_meta(val: str):
    low = val.lower()
    for tok in FORBIDDEN_META:
        if tok in low:
            raise RuntimeError(f'forbidden_meta:{tok}')


def stage_dirs(run_root: Path, stage_num: str, name: str):
    base = run_root / f'{stage_num}_{name}'
    raw = base / 'raw'
    can = base / 'canonical'
    raw.mkdir(parents=True, exist_ok=True)
    can.mkdir(parents=True, exist_ok=True)
    return raw, can


def build_posts_from_link(url_or_id: str, post_count: int = 3) -> dict:
    run_id = run_id_for(url_or_id)
    run_root = RUNS_ROOT / run_id
    run_root.mkdir(parents=True, exist_ok=True)
    EXPORT_ROOT.mkdir(parents=True, exist_ok=True)

    # 01 donald
    raw_d, can_d = stage_dirs(run_root, '01', 'donald')
    p = subprocess.run(['python3', DONALD_PROCESS, url_or_id, 'REPROCESS'], capture_output=True, text=True)
    write_text_atomic(raw_d / 'donald_raw.txt', (p.stdout or '') + '\n[stderr]\n' + (p.stderr or ''))
    if p.returncode not in (0, 2):
        fail_closed(run_root, 'donald', 'donald_process_failed', [str(raw_d / 'donald_raw.txt')])
        return {'ok': False, 'run_id': run_id, 'reason': 'donald_process_failed', 'run_root': str(run_root)}

    donald_run_id = (p.stdout or '').strip().splitlines()[-1]
    manifest_path = VAULT_ROOT / 'manifests' / f'{donald_run_id}__manifest.json'
    p2 = subprocess.run(['python3', DONALD_EXTRACT, str(manifest_path), '--client', 'Unknown'], capture_output=True, text=True)
    write_text_atomic(raw_d / 'donald_extract_raw.txt', (p2.stdout or '') + '\n[stderr]\n' + (p2.stderr or ''))
    if p2.returncode != 0:
        fail_closed(run_root, 'donald', 'donald_extract_failed', [str(raw_d / 'donald_extract_raw.txt')])
        return {'ok': False, 'run_id': run_id, 'reason': 'donald_extract_failed', 'run_root': str(run_root)}

    ext = json.loads((p2.stdout or '{}').strip() or '{}')
    nuggets_file = Path(ext.get('nuggets', ''))
    # System-level race guard: never proceed on placeholder or missing export
    if (not nuggets_file.exists()) or ('placeholder export' in (nuggets_file.read_text(encoding='utf-8', errors='ignore').lower())):
        fail_closed(run_root, 'donald', 'nugget_export_not_ready', [str(nuggets_file)])
        return {'ok': False, 'run_id': run_id, 'reason': 'nugget_export_not_ready', 'run_root': str(run_root)}
    nuggets = read_json(nuggets_file, {})
    nug = ((nuggets.get('nuggets') or [])[:1] or [{}])[0]

    handoff = {
        'run_id': run_id,
        'source_id': manifest_path.name,
        'route': nug.get('post_class_recommendation', 'Authority'),
        'conversion_angle': nug.get('conversion_angle', 'none'),
        'idea_one_liner': nug.get('idea_one_liner', ''),
        'proof_anchor_lines': nug.get('proof_anchor_lines', ['Client described repeated delay loop.', 'Action was clear, execution was postponed.']),
        'first_step_seed': nug.get('first_step_seed', 'Today: Take one avoided action before noon.'),
    }
    write_json_atomic(can_d / 'donald_handoff.json', handoff)

    final_posts = []
    flags_all = []

    for idx in range(1, post_count + 1):
        # 02 mark
        raw_m, can_m = stage_dirs(run_root, '02', 'mark')
        req_m = {
            'task': 'caption_body_only',
            'variation_index': idx,
            'input': handoff,
            'output_contract': {'type': 'json_only', 'required': {'caption_body': 'string'}, 'strict': True},
            'instruction': 'Return JSON only. No commentary. No extra keys.'
        }
        mtxt = call_agent('mark', req_m, f'one_lane:{run_id}:mark:{idx}', raw_m / f'mark_raw_{idx}.txt')
        try:
            mj = json_extract(mtxt, 'caption_body')
            if set(mj.keys()) != {'caption_body'}:
                raise RuntimeError('mark_extra_or_missing_keys')
            body = mj['caption_body'].strip()
            validate_no_meta(body)
            if any(x in body.lower() for x in ['overlay_hook_', 'next chapter', 'notes:']):
                raise RuntimeError('mark_stage_ban')
        except Exception as e:
            fail_closed(run_root, 'mark', str(e), [str(raw_m / f'mark_raw_{idx}.txt')])
            return {'ok': False, 'run_id': run_id, 'reason': f'mark_fail:{e}', 'run_root': str(run_root)}
        write_json_atomic(can_m / f'mark_caption_body_{idx}.json', {'caption_body': body})

        # 03 bob
        raw_b, can_b = stage_dirs(run_root, '03', 'bob')
        req_b = {
            'task': 'append_only_close_cta',
            'variation_index': idx,
            'body_verbatim': body,
            'route': handoff['route'],
            'conversion_angle': handoff['conversion_angle'],
            'output_contract': {'type': 'json_only', 'required': {'final_caption_lines': 'string[]'}, 'strict': True},
            'instruction': 'Return JSON only with final_caption_lines. Each element single line. Use empty string for paragraph breaks only.'
        }
        btxt = call_agent('bob', req_b, f'one_lane:{run_id}:bob:{idx}', raw_b / f'bob_raw_{idx}.txt')
        try:
            bj = json_extract(btxt, 'final_caption_lines')
            if set(bj.keys()) != {'final_caption_lines'}:
                raise RuntimeError('bob_extra_or_missing_keys')
            lines = bj['final_caption_lines']
            if not isinstance(lines, list) or not all(isinstance(x, str) for x in lines):
                raise RuntimeError('bob_lines_invalid')
            # paragraph preservation: Mark body must be verbatim prefix (as a single string)
            merged = []
            for x in lines:
                if '\n' in x:
                    merged.extend(x.split('\n'))
                else:
                    merged.append(x)
            prefix = '\n'.join([ln for ln in merged if ln != ''])
            # compare after collapsing whitespace and dash sanitation
            norm = lambda s: re.sub(r'\s+', ' ', s.replace('—', '-').replace('–', '-')).strip()
            if norm(prefix).find(norm(body)) != 0:
                raise RuntimeError('bob_modified_mark_body')
            final_caption = '\n'.join(merged).strip()
            validate_no_meta(final_caption)
            if 'overlay_hook_' in final_caption.lower():
                raise RuntimeError('bob_stage_ban')
        except Exception as e:
            fail_closed(run_root, 'bob', str(e), [str(raw_b / f'bob_raw_{idx}.txt')])
            return {'ok': False, 'run_id': run_id, 'reason': f'bob_fail:{e}', 'run_root': str(run_root)}
        write_json_atomic(can_b / f'bob_final_caption_lines_{idx}.json', {'final_caption_lines': merged})
        write_text_atomic(can_b / f'final_caption_{idx}.txt', final_caption + '\n')

        # 04 hook
        raw_h, can_h = stage_dirs(run_root, '04', 'hook')
        req_h = {
            'task': 'hooks_only',
            'variation_index': idx,
            'final_caption': final_caption,
            'output_contract': {'type': 'json_only', 'required': {'overlay_hook_1': 'string', 'overlay_hook_2': 'string', 'overlay_hook_3': 'string', 'overlay_cta': 'string'}, 'strict': True},
            'instruction': 'Return JSON only. No extra keys.'
        }
        htxt = call_agent('captainhook', req_h, f'one_lane:{run_id}:hook:{idx}', raw_h / f'hook_raw_{idx}.txt')
        try:
            hj = json_extract(htxt, 'overlay_hook_1')
            if set(hj.keys()) != {'overlay_hook_1', 'overlay_hook_2', 'overlay_hook_3', 'overlay_cta'}:
                raise RuntimeError('hook_extra_or_missing_keys')
            if hj['overlay_cta'].strip().lower() != 'read caption':
                raise RuntimeError('hook_overlay_cta_invalid')
            if final_caption[:60] in (hj['overlay_hook_1'] + hj['overlay_hook_2'] + hj['overlay_hook_3']):
                raise RuntimeError('hook_contains_caption_text')
        except Exception as e:
            fail_closed(run_root, 'hook', str(e), [str(raw_h / f'hook_raw_{idx}.txt')])
            return {'ok': False, 'run_id': run_id, 'reason': f'hook_fail:{e}', 'run_root': str(run_root)}
        write_json_atomic(can_h / f'hooks_{idx}.json', hj)

        # 05 jimmy scanner with fallback
        raw_j, can_j = stage_dirs(run_root, '05', 'jimmy')
        req_j = {
            'task': 'scan_and_finalize_minimal',
            'variation_index': idx,
            'final_caption': final_caption,
            'hooks': hj,
            'output_contract': {'type': 'json_only', 'required': {'final_post_text': 'string', 'flags': 'array', 'edits_made': 'array'}, 'strict': True},
            'instruction': 'No rewrite loops. Tiny fixes only. Return JSON only.'
        }
        jtxt = call_agent(JIMMY_AGENT, req_j, f'one_lane:{run_id}:{JIMMY_AGENT}:{idx}', raw_j / f'{JIMMY_AGENT}_raw_{idx}.txt')
        jimmy_skipped = False
        try:
            jj = json_extract(jtxt, 'final_post_text')
            if not {'final_post_text', 'flags', 'edits_made'}.issubset(set(jj.keys())):
                raise RuntimeError('jimmy_missing_keys')
            final_post = jj['final_post_text'].strip()
            flags = jj.get('flags') or []
            edits = jj.get('edits_made') or []
        except Exception:
            jimmy_skipped = True
            final_post = '\n'.join([
                f'POST_{idx}',
                f"OVERLAY_HOOK_1: {hj['overlay_hook_1']}",
                f"OVERLAY_HOOK_2: {hj['overlay_hook_2']}",
                f"OVERLAY_HOOK_3: {hj['overlay_hook_3']}",
                f"OVERLAY_CTA: {hj['overlay_cta']}",
                '',
                'CAPTION:',
                final_caption,
            ]).strip()
            flags = [{'type': 'jimmy_skipped', 'detail': 'fallback_assembly_used'}]
            edits = []

        write_text_atomic(can_j / f'final_post_{idx}.txt', final_post + '\n')
        write_json_atomic(can_j / f'qc_report_{idx}.json', {'jimmy_skipped': jimmy_skipped, 'flags': flags, 'edits_made': edits})
        final_posts.append(final_post)
        flags_all.extend(flags)

    # 99 export
    raw_x, can_x = stage_dirs(run_root, '99', 'export')
    out_file = run_root / '99_export' / f'{run_id}_final_posts.txt'
    joined = '\n\n' + ('\n\n' + ('='*80) + '\n\n').join(final_posts)
    write_text_atomic(out_file, joined.strip() + '\n')
    drive_copy = EXPORT_ROOT / f'{run_id}_final_posts.txt'
    shutil.copy2(out_file, drive_copy)
    write_text_atomic(can_x / 'export_path.txt', str(drive_copy) + '\n')

    return {'ok': True, 'run_id': run_id, 'posts_exported': len(final_posts), 'export_path': str(drive_copy), 'run_root': str(run_root), 'flags': flags_all}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('url_or_id')
    ap.add_argument('--posts', type=int, default=3)
    args = ap.parse_args()

    run_id = run_id_for(args.url_or_id)
    got, status = acquire_global_lock(run_id)
    if not got:
        print(json.dumps({'ok': True, 'status': 'busy'}))
        return 0
    try:
        res = build_posts_from_link(args.url_or_id, post_count=max(3, min(5, args.posts)))
        if res.get('ok'):
            print(f"RUN_ID={res['run_id']} status=ok posts_exported={res['posts_exported']} export_path={res['export_path']}")
            return 0
        print(f"RUN_ID={res['run_id']} status=fail posts_exported=0 export_path={EXPORT_ROOT}")
        return 1
    finally:
        release_global_lock()


if __name__ == '__main__':
    raise SystemExit(main())
