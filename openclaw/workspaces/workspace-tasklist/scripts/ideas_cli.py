#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import re
import unicodedata
from pathlib import Path

BASE = Path('/home/openclaw_agent_1/.openclaw/workspace-tasklist')
OPEN_DIR = BASE / 'ideas' / 'open'
ARCHIVE_DIR = BASE / 'ideas' / 'archive'
UNDO_FILE = BASE / 'ideas' / '.undo_last_close.json'
MEMORY_DIR = BASE / 'memory'


def now_iso_local():
    return dt.datetime.now().astimezone().isoformat(timespec='seconds')


def slugify(s: str, max_len: int = 60) -> str:
    s = unicodedata.normalize('NFKD', s)
    s = s.encode('ascii', 'ignore').decode('ascii')
    s = s.lower().strip()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return (s[:max_len] or 'idea')


def alpha_key(i: int) -> str:
    chars = []
    n = i
    while True:
        n, r = divmod(n, 26)
        chars.append(chr(ord('A') + r))
        if n == 0:
            break
        n -= 1
    return ''.join(reversed(chars))


def safe_json(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def write_json(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write('\n')




def append_memory_event(event_type: str, title: str = '', description: str = '', idea_id: str = '', full_idea: str = ''):
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    day = dt.datetime.now().strftime('%Y-%m-%d')
    path = MEMORY_DIR / f'{day}.md'
    ts = now_iso_local()

    lines = [
        f'- [{ts}] event={event_type} id={idea_id}',
        f'  title: {title.strip()}',
        f'  description: {description.strip()}',
    ]
    if full_idea:
        lines.append(f'  full_idea: {full_idea.strip()}')

    with path.open('a', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

def gen_id(title: str) -> str:
    ts = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
    return f"{ts}-{slugify(title, 36)}"


def load_open_rows():
    rows = []
    for p in sorted(OPEN_DIR.glob('*.json')):
        try:
            d = safe_json(p)
            if d.get('status') == 'open':
                rows.append((p, d))
        except Exception:
            continue
    return rows


def dedupe_rows(rows):
    out = []
    seen = set()
    for p, d in rows:
        iid = d.get('id')
        if iid in seen:
            continue
        seen.add(iid)
        out.append((p, d))
    return out


def save_undo_record(idea_id: str, title: str, open_path: str, archive_path: str):
    rec = {
        'idea_id': idea_id,
        'title': title,
        'open_path': open_path,
        'archive_path': archive_path,
        'closed_at': now_iso_local(),
        'can_undo': True,
    }
    write_json(UNDO_FILE, rec)


def close_exact_id(idea_id: str, emit: bool = True):
    for p, d in load_open_rows():
        if d.get('id') != idea_id:
            continue
        d['status'] = 'closed'
        d['closed_at'] = now_iso_local()
        d['updated_at'] = now_iso_local()
        out = ARCHIVE_DIR / p.name
        write_json(out, d)
        p.unlink(missing_ok=True)
        save_undo_record(
            idea_id=d.get('id', ''),
            title=d.get('title', ''),
            open_path=str(p),
            archive_path=str(out),
        )
        append_memory_event(
            event_type='closed_archive',
            title=d.get('title',''),
            description=d.get('description',''),
            idea_id=d.get('id',''),
            full_idea=d.get('full_idea',''),
        )
        if emit:
            print(json.dumps({
                'ok': True,
                'status': 'closed',
                'closed_id': d.get('id'),
                'title': d.get('title'),
                'archived_path': str(out),
                'undo_hint': 'If this was a mistake, run: ideas_cli.py undo-last'
            }))
        return 0

    if emit:
        print(json.dumps({'ok': False, 'status': 'not_found', 'error': f'No open idea found with id: {idea_id}'}))
    return 2



def close_by_numbers(nums: list[int]):
    """Close multiple open ideas by numeric position from ideas_cli.py summary order.

    This is a non-interactive fast-path for Andre.
    Returns JSON with closed items.
"""
    rows = [d for _p, d in load_open_rows()]
    if not rows:
        print(json.dumps({'ok': False, 'error': 'No OPEN ideas to close.', 'closed': []}))
        return 2

    # Build 1-indexed mapping based on summary order
    mapping = {i+1: d for i, d in enumerate(rows)}

    closed = []
    errors = []
    for n in nums:
        d = mapping.get(n)
        if not d:
            errors.append({'num': n, 'error': 'out_of_range'})
            continue
        idea_id = d.get('id')
        if not idea_id:
            errors.append({'num': n, 'error': 'missing_id'})
            continue
        rc = close_exact_id(idea_id, emit=False)
        if rc == 0:
            closed.append({'num': n, 'id': idea_id, 'title': d.get('title','')})
        else:
            errors.append({'num': n, 'id': idea_id, 'error': 'close_failed'})

    print(json.dumps({'ok': len(errors)==0, 'closed': closed, 'errors': errors}, ensure_ascii=False))
    return 0 if len(errors)==0 else 1
def undo_last_close():
    if not UNDO_FILE.exists():
        print(json.dumps({'ok': False, 'status': 'nothing_to_undo', 'error': 'No recent close action to undo.'}))
        return 2

    rec = safe_json(UNDO_FILE)
    if not rec.get('can_undo', False):
        print(json.dumps({'ok': False, 'status': 'nothing_to_undo', 'error': 'Latest close action already undone.'}))
        return 2

    archive_path = Path(rec.get('archive_path', ''))
    open_path = Path(rec.get('open_path', ''))

    if not archive_path.exists():
        print(json.dumps({'ok': False, 'status': 'archive_missing', 'error': f'Archive file not found: {archive_path}'}))
        return 2

    d = safe_json(archive_path)
    d['status'] = 'open'
    d['updated_at'] = now_iso_local()
    d['reopened_at'] = now_iso_local()

    # keep close history if present; do not destroy audit trail
    write_json(open_path, d)
    archive_path.unlink(missing_ok=True)

    rec['can_undo'] = False
    rec['undone_at'] = now_iso_local()
    write_json(UNDO_FILE, rec)

    append_memory_event(
        event_type='reopened_undo',
        title=d.get('title',''),
        description=d.get('description',''),
        idea_id=d.get('id',''),
        full_idea=d.get('full_idea',''),
    )
    print(json.dumps({
        'ok': True,
        'status': 'reopened',
        'id': d.get('id'),
        'title': d.get('title'),
        'open_path': str(open_path)
    }))
    return 0


def find_matches(selector: str):
    rows = load_open_rows()
    exact = [(p, d) for p, d in rows if d.get('id') == selector]
    if exact:
        return exact

    sel = selector.lower().strip()
    prefix = [(p, d) for p, d in rows if d.get('id', '').startswith(selector)]
    title = [(p, d) for p, d in rows if sel and sel in d.get('title', '').lower()]
    return dedupe_rows(prefix + title)


def print_options(selector: str, rows):
    options = []
    for i, (_p, d) in enumerate(rows):
        options.append({
            'key': alpha_key(i),
            'id': d.get('id'),
            'title': d.get('title'),
            'description': d.get('description', '').strip(),
        })

    print(json.dumps({
        'ok': False,
        'status': 'confirm_required',
        'selector': selector,
        'count': len(options),
        'options': options,
        'next_step': 'Ask user to choose option key (A, B, C...) then close by exact id using close-id.'
    }, ensure_ascii=False))


def create_idea(title: str, description: str, source_text: str = None):
    idea_id = gen_id(title)
    obj = {
        'id': idea_id,
        'title': title.strip(),
        'description': description.strip(),
        'status': 'open',
        'created_at': now_iso_local(),
        'updated_at': now_iso_local(),
        # Internal detail: keep full original idea text for memory,
        # but user-facing lists should only show title + one-line description.
        'full_idea': source_text.strip() if source_text else f"{title.strip()} — {description.strip()}",
    }
    if source_text:
        full = source_text.strip()
        obj['source_text'] = full
        obj['full_idea'] = full

    out = OPEN_DIR / f'{idea_id}.json'
    write_json(out, obj)
    append_memory_event(
        event_type='remember_open',
        title=obj.get('title',''),
        description=obj.get('description',''),
        idea_id=obj.get('id',''),
        full_idea=obj.get('full_idea',''),
    )
    print(json.dumps({'ok': True, 'id': idea_id, 'path': str(out), 'title': obj['title'], 'description': obj['description']}))


def list_open():
    rows = [d for _p, d in load_open_rows()]
    print(json.dumps({'ok': True, 'count': len(rows), 'ideas': rows}, ensure_ascii=False))


def close_idea(selector: str):
    matches = find_matches(selector)
    if not matches:
        print(json.dumps({'ok': False, 'status': 'not_found', 'error': f'No open idea found for selector: {selector}'}))
        return 2

    if len(matches) == 1 and matches[0][1].get('id') == selector:
        return close_exact_id(selector)

    print_options(selector, matches)
    return 3


def summary_text():
    rows = [d for _p, d in load_open_rows()]

    if not rows:
        print('OPEN IDEAS (0)\n- None')
        return

    print(f'OPEN IDEAS ({len(rows)})')
    for i, d in enumerate(rows, 1):
        print(f"{i}. {d.get('title','(untitled)')} — {d.get('description','').strip()} [id:{d.get('id')}]" )


def main():
    parser = argparse.ArgumentParser(description='Tasklist ideas manager')
    sub = parser.add_subparsers(dest='cmd', required=True)

    c = sub.add_parser('create', help='Create open idea')
    c.add_argument('--title', required=True)
    c.add_argument('--description', required=True)
    c.add_argument('--source-text', required=False)

    sub.add_parser('list-open', help='List open ideas as JSON')
    sub.add_parser('summary', help='Printable summary of open ideas')

    cl = sub.add_parser('close', help='Close by exact id; non-exact returns A/B/C options')
    cl.add_argument('selector')

    cid = sub.add_parser('close-id', help='Close by exact id only')
    cid.add_argument('id')

    opt = sub.add_parser('options', help='Return A/B/C options for selector without closing')
    opt.add_argument('selector')

    sub.add_parser('undo-last', help='Undo most recent close action')

    cn = sub.add_parser('close-nums', help='Close by numeric positions from summary (fast-path)')
    cn.add_argument('nums', nargs='+', type=int)

    args = parser.parse_args()

    OPEN_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

    if args.cmd == 'create':
        create_idea(args.title, args.description, args.source_text)
        return 0
    if args.cmd == 'list-open':
        list_open()
        return 0
    if args.cmd == 'summary':
        summary_text()
        return 0
    if args.cmd == 'close':
        return close_idea(args.selector)
    if args.cmd == 'close-id':
        return close_exact_id(args.id)
    if args.cmd == 'options':
        matches = find_matches(args.selector)
        if not matches:
            print(json.dumps({'ok': False, 'status': 'not_found', 'error': f'No open idea found for selector: {args.selector}'}))
            return 2
        print_options(args.selector, matches)
        return 0
    if args.cmd == 'close-nums':
        return close_by_numbers(args.nums)

    if args.cmd == 'undo-last':
        return undo_last_close()

    return 1


if __name__ == '__main__':
    raise SystemExit(main())
