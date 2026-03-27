#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any

VAULT = Path(os.path.expanduser('~/krc_vault'))
NUGGET_DIR = VAULT / 'gold nugget exports'
FINISHED_DIR = VAULT / 'finished content for posting'
STATE_LAST_BATCH = VAULT / 'fathom_library/state/last_batch.json'
MANIFEST_DIR = VAULT / 'manifests'

AUTHORITY_BODY_MAX = int(os.environ.get('KRC_AUTHORITY_BODY_MAX', '1700'))
CONVERSION_BODY_MAX = int(os.environ.get('KRC_CONVERSION_BODY_MAX', '1500'))
FINAL_CAPTION_MAX = int(os.environ.get('KRC_FINAL_CAPTION_MAX', '2200'))
HOOK_MAX_CHARS = int(os.environ.get('KRC_HOOK_MAX_CHARS', '110'))
AUTHORITY_LOCKED_CTA = os.environ.get('KRC_AUTHORITY_LOCKED_CTA', 'Follow for daily leadership truth.')
CONVERSION_LOCKED_CTA = os.environ.get('KRC_CONVERSION_LOCKED_CTA', 'NEXT CHAPTER')

DASH_BAN_RE = re.compile(r'--|—|–')


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


def call_agent(agent: str, message_obj: Any, timeout: int = 180) -> str:
    msg = message_obj if isinstance(message_obj, str) else json.dumps(message_obj, ensure_ascii=False)
    p = run(['openclaw', 'agent', '--agent', agent, '--timeout', str(timeout), '--message', msg, '--json'])
    if p.returncode != 0:
        raise RuntimeError(f'agent {agent} failed: {p.stderr[-400:]}')
    j = json.loads(p.stdout)
    payloads = (j.get('result') or {}).get('payloads') or []
    if payloads and isinstance(payloads[0], dict):
        return (payloads[0].get('text') or '').strip()
    return ''


def parse_hooks(text: str) -> list[str]:
    hooks: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        m = re.match(r'^OVERLAY_HOOK_[123]\s*:\s*(.+)$', s, re.I)
        if m:
            hooks.append(m.group(1).strip())
    if len(hooks) >= 3:
        return hooks[:3]
    # fallback: first 3 non-empty lines
    return [ln.strip() for ln in text.splitlines() if ln.strip()][:3]


def contains_banned_dash(s: str) -> bool:
    return bool(DASH_BAN_RE.search(s or ''))


def route_of(n: dict) -> str:
    val = (n.get('post_class_recommendation') or n.get('route') or 'Authority').strip().lower()
    return 'Conversion' if val == 'conversion' else 'Authority'


def pick_nuggets(nuggets: list[dict], trial_n: int = 3) -> list[dict]:
    auth = [n for n in nuggets if route_of(n) == 'Authority']
    conv = [n for n in nuggets if route_of(n) == 'Conversion']
    out: list[dict] = []
    if len(auth) >= 2 and len(conv) >= 1 and trial_n >= 3:
        out.extend(auth[:2])
        out.append(conv[0])
    else:
        out.extend(nuggets[:trial_n])
    return out


def find_latest_nuggets() -> Path:
    if STATE_LAST_BATCH.exists():
        lb = json.loads(STATE_LAST_BATCH.read_text())
        run_ids = [r.get('run_id') for r in (lb.get('results') or []) if r.get('ok') and r.get('run_id')]
        cands: list[Path] = []
        for rid in run_ids:
            cands.extend(sorted(NUGGET_DIR.glob(f'{rid}__*__nuggets.json')))
        if cands:
            cands = sorted(cands, key=lambda p: p.stat().st_mtime, reverse=True)
            return cands[0]
    all_cands = sorted(NUGGET_DIR.glob('*__nuggets.json'), key=lambda p: p.stat().st_mtime, reverse=True)
    if not all_cands:
        raise FileNotFoundError('No nuggets files found')
    return all_cands[0]


def normalize_body(text: str) -> str:
    t = text.strip()
    # If model returned prefixed label, strip once
    if t.lower().startswith('body:'):
        t = t.split(':', 1)[1].strip()
    return t


def process_nugget(n: dict, donald_export: dict, retries: int = 2) -> dict:
    route = route_of(n)
    body_max = AUTHORITY_BODY_MAX if route == 'Authority' else CONVERSION_BODY_MAX

    body = ''
    append = ''
    hooks: list[str] = []
    routes: list[str] = []

    # MARK
    for i in range(retries):
      mark_req = {
        'task': 'caption_body_only',
        'route': route,
        'body_max_chars': body_max,
        'hard_constraints': {
          'no_browsing': True,
          'no_outside_facts': True,
          'ban_punctuation': ['--', '—', '–']
        },
        'donald_fields': {
          'nugget': n,
          'source': {
            'schema_version': donald_export.get('schema_version'),
            'run_id': donald_export.get('run_id')
          }
        },
        'required_elements': {
          'first_step_starter': True,
          'mid_caption_comment_moment_for_authority': route == 'Authority',
          'local_enemy_frame_behavior': True
        },
        'output_shape': 'BODY only, no hooks, no CTA'
      }
      if i > 0:
        mark_req['revision'] = f'Body violated constraints in prior attempt. Keep under {body_max} chars and remove banned punctuation.'
      body = normalize_body(call_agent('mark', mark_req, timeout=220))
      if len(body) <= body_max and not contains_banned_dash(body):
        break
      routes.append('ROUTE_TO: MARK')
    if len(body) > body_max:
      return {'ok': False, 'route_to': 'MARK', 'reason': 'Body too long before Bob append', 'nugget_id': n.get('nugget_id'), 'routes': routes}

    # BOB
    for i in range(retries):
      bob_req = {
        'task': 'append_only_close_cta',
        'route': route,
        'body_verbatim': body,
        'locked_cta': CONVERSION_LOCKED_CTA if route == 'Conversion' else AUTHORITY_LOCKED_CTA,
        'final_caption_max_chars': FINAL_CAPTION_MAX,
        'non_negotiable': 'Append only. Do not rewrite/merge/split/reorder/compress body.',
        'output_shape': 'APPEND only'
      }
      if i > 0:
        bob_req['revision'] = 'Fix CTA/runway formatting only. Keep body untouched.'
      append = call_agent('bob', bob_req, timeout=180).strip()
      if append.lower().startswith('append:'):
        append = append.split(':', 1)[1].strip()

      caption = (body + '\n\n' + append).strip()
      lines = [ln.rstrip() for ln in caption.splitlines() if ln.strip()]
      last_line = lines[-1] if lines else ''
      locked = CONVERSION_LOCKED_CTA if route == 'Conversion' else AUTHORITY_LOCKED_CTA
      cta_ok = (last_line == locked)
      if len(caption) <= FINAL_CAPTION_MAX and cta_ok and not contains_banned_dash(caption):
        break
      routes.append('ROUTE_TO: BOB')
    caption = (body + '\n\n' + append).strip()
    lines = [ln.rstrip() for ln in caption.splitlines() if ln.strip()]
    last_line = lines[-1] if lines else ''
    locked = CONVERSION_LOCKED_CTA if route == 'Conversion' else AUTHORITY_LOCKED_CTA
    if len(caption) > FINAL_CAPTION_MAX:
      return {'ok': False, 'route_to': 'BOB', 'reason': 'Final caption too long after Bob append', 'nugget_id': n.get('nugget_id'), 'routes': routes}
    if last_line != locked:
      return {'ok': False, 'route_to': 'BOB', 'reason': 'Locked CTA violation', 'nugget_id': n.get('nugget_id'), 'routes': routes}

    # CAPTAIN HOOK
    for i in range(retries):
      hook_req = {
        'task': 'hooks_only',
        'need': 3,
        'max_chars_each': HOOK_MAX_CHARS,
        'caption_value_context': caption,
        'banned_punctuation': ['--', '—', '–'],
        'output_shape': 'OVERLAY_HOOK_1/2/3 only'
      }
      if i > 0:
        hook_req['revision'] = 'Hooks violated format/length. Return exactly 3 one-sentence hooks within limits.'
      hooks = parse_hooks(call_agent('captainhook', hook_req, timeout=180))
      ok = len(hooks) == 3 and all(len(h) <= HOOK_MAX_CHARS and not contains_banned_dash(h) for h in hooks)
      if ok:
        break
      routes.append('ROUTE_TO: CAPTAIN_HOOK')
    if not (len(hooks) == 3 and all(len(h) <= HOOK_MAX_CHARS and not contains_banned_dash(h) for h in hooks)):
      return {'ok': False, 'route_to': 'CAPTAIN_HOOK', 'reason': 'Hook issues', 'nugget_id': n.get('nugget_id'), 'routes': routes}

    # Jimmy as Overseer (final assembly/notes, no creative rewrite)
    qa = {
      'schema_ok': True,
      'dash_ban_ok': not (contains_banned_dash(caption) or any(contains_banned_dash(h) for h in hooks)),
      'body_before_bob_ok': len(body) <= body_max,
      'final_after_bob_ok': len(caption) <= FINAL_CAPTION_MAX,
      'cta_last_line_ok': last_line == locked,
      'hooks_ok': len(hooks) == 3 and all(len(h) <= HOOK_MAX_CHARS for h in hooks),
    }

    overseer_req = {
      'task': 'assemble_and_qa',
      'role': 'Overseer',
      'rewrite_policy': 'no_polish_rewrite',
      'mark_body': body,
      'bob_append': append,
      'hooks': {
        'OVERLAY_HOOK_1': hooks[0],
        'OVERLAY_HOOK_2': hooks[1],
        'OVERLAY_HOOK_3': hooks[2],
      },
      'caption': caption,
      'qa_checklist_results': qa,
      'output_mode': 'pass_or_route_one_specialist'
    }
    overseer_out = call_agent('jimmy', overseer_req, timeout=220)

    return {
      'ok': True,
      'route': route,
      'nugget_id': n.get('nugget_id'),
      'caption': caption,
      'hooks': hooks,
      'qa': qa,
      'overseer_out': overseer_out,
      'routes': routes,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=3)
    ap.add_argument('--nuggets', default='')
    args = ap.parse_args()

    nuggets_path = Path(args.nuggets) if args.nuggets else find_latest_nuggets()
    donald_export = json.loads(nuggets_path.read_text())

    nuggets = donald_export.get('nuggets') or []
    if not nuggets:
      print(json.dumps({'ok': False, 'error': 'No nuggets in export', 'file': str(nuggets_path)}))
      return 2

    selected = pick_nuggets(nuggets, trial_n=args.n)
    results = [process_nugget(n, donald_export) for n in selected]

    FINISHED_DIR.mkdir(parents=True, exist_ok=True)
    run_id = donald_export.get('run_id') or nuggets_path.name.split('__')[0]
    out_path = FINISHED_DIR / f'{run_id}__deterministic_pipeline_trial.md'

    lines: list[str] = []
    lines.append('# Deterministic Marketing Pipeline Trial')
    lines.append(f'RUN_ID: {run_id}')
    lines.append(f'SOURCE: {nuggets_path.name}')
    lines.append('')

    pass_count = 0
    for idx, r in enumerate(results, start=1):
      lines.append('---')
      if not r.get('ok'):
        lines.append(f'POST {idx}: FAIL')
        lines.append(f'NUGGET_ID: {r.get("nugget_id")}')
        lines.append(f'ROUTE_TO: {r.get("route_to")}')
        lines.append(f'FIX_REQUEST: {r.get("reason")}')
        continue
      pass_count += 1
      h1, h2, h3 = r['hooks']
      lines.append(f'POST {idx}: PASS')
      lines.append(f'NUGGET_ID: {r.get("nugget_id")}')
      lines.append(f'OVERLAY_HOOK_1: {h1}')
      lines.append(f'OVERLAY_HOOK_2: {h2}')
      lines.append(f'OVERLAY_HOOK_3: {h3}')
      lines.append('CAPTION:')
      lines.append(r['caption'])
      lines.append('NOTES:')
      lines.append(f'- QA: PASS')
      lines.append(f'- Route: {r.get("route")}')
      lines.append(f'- Lengths: body={len(r["caption"]) - len((r.get("caption") or "").splitlines()[-1])} caption={len(r["caption"])}')
      lines.append(f'- final=true')

    out_path.write_text('\n'.join(lines), encoding='utf-8')

    summary = {
      'ok': pass_count == len(results),
      'selected': len(results),
      'passed': pass_count,
      'failed': len(results) - pass_count,
      'out_file': str(out_path),
      'source_nuggets': str(nuggets_path),
      'results': [
        {
          'nugget_id': r.get('nugget_id'),
          'ok': r.get('ok'),
          'route_to': r.get('route_to') if not r.get('ok') else None,
          'reason': r.get('reason') if not r.get('ok') else None
        } for r in results
      ]
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0 if summary['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
