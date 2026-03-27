#!/usr/bin/env python3
"""Build a searchable Fathom library index + per-client link lists.

Stage 1 deliverables (local vault only):
- ~/krc_vault/fathom_library/index.csv
- ~/krc_vault/fathom_library/index.json
- ~/krc_vault/fathom_library/clients/<Letter>/<Client Name> (<email>).md

Client naming rule:
- Default: the other meeting participant (non-Andre) display name.
- Always include (email) suffix when available.
- Worst case: Unknown (<email>)

This script uses the Fathom External API via X-Api-Key.
Env:
- FATHOM_API_KEY (required)
- FATHOM_API_BASE_URL (optional)
"""

from __future__ import annotations

import csv
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


API_BASE = os.environ.get("FATHOM_API_BASE_URL", "https://api.fathom.ai")
VAULT = Path(os.path.expanduser("~/krc_vault"))
OUT_BASE = VAULT / "fathom_library"
CLIENTS_DIR = OUT_BASE / "clients"


def http_get_json(url: str, api_key: str) -> Dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"X-Api-Key": api_key, "Accept": "application/json"},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read().decode("utf-8")
    return json.loads(body)


def normalize_spaces(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())


def safe_filename(s: str, max_len: int = 140) -> str:
    s = normalize_spaces(s)
    s = re.sub(r"[^A-Za-z0-9 ._()\-]+", "_", s)
    s = s.strip(" ._")
    return (s[:max_len] or "Unknown")


def parse_dt(s: str) -> str:
    return (s or "").strip()


def choose_client(invitees: list[dict], recorded_by_email: str, meeting_title: str) -> Tuple[str, Optional[str]]:
    """Pick the participant who is NOT Andre (recorded_by).

    Returns: (display_name, email)

    If calendar_invitees.name is missing or unhelpful, we fall back to parsing
    the meeting title format: "<Client> and Andre Panet-Raymond".
    """

    def parse_client_from_title(title: str) -> Optional[str]:
        t = normalize_spaces(title)
        if not t:
            return None
        # Common format
        if " and Andre Panet-Raymond" in t:
            return t.split(" and Andre Panet-Raymond", 1)[0].strip() or None
        # Fallback: split on ' and Andre'
        if " and Andre" in t:
            return t.split(" and Andre", 1)[0].strip() or None
        return None

    title_client = parse_client_from_title(meeting_title)

    # Prefer non-recorded_by participant with an email
    for p in invitees:
        if not isinstance(p, dict):
            continue
        email = (p.get("email") or "").strip().lower()
        name = normalize_spaces(p.get("name") or "")
        if email and email != recorded_by_email:
            # If the invitee "name" is an email, treat it as unknown.
            if name and "@" in name:
                name = ""
            # If name missing, use title-derived name.
            if not name and title_client:
                name = title_client
            return (name or "Unknown", email)

    # Fallback: first participant that's not recorded_by
    for p in invitees:
        if not isinstance(p, dict):
            continue
        email = (p.get("email") or "").strip().lower()
        name = normalize_spaces(p.get("name") or "")
        if email != recorded_by_email:
            return (name or "Unknown", email or None)

    return ("Unknown", None)


@dataclass
class Row:
    client: str
    email: str
    created_at: str
    recording_id: str
    share_url: str
    meeting_title: str


def list_meetings(api_key: str, *, limit: int = 100) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    cursor: Optional[str] = None

    for _ in range(500):
        params = {"limit": str(limit)}
        if cursor:
            params["cursor"] = cursor
        url = f"{API_BASE}/external/v1/meetings?{urllib.parse.urlencode(params)}"
        payload = http_get_json(url, api_key)
        page = payload.get("items") or []
        if not isinstance(page, list) or not page:
            break
        for it in page:
            if isinstance(it, dict):
                items.append(it)
        cursor = payload.get("next_cursor")
        if not cursor:
            break

    return items


def main() -> int:
    api_key = (os.environ.get("FATHOM_API_KEY") or "").strip()
    if not api_key:
        print("FATHOM_API_KEY not set", file=sys.stderr)
        return 2

    OUT_BASE.mkdir(parents=True, exist_ok=True)
    CLIENTS_DIR.mkdir(parents=True, exist_ok=True)

    meetings = list_meetings(api_key)

    rows: List[Row] = []
    for m in meetings:
        invitees = m.get("calendar_invitees") or []
        recorded_by = (m.get("recorded_by") or {})
        recorded_by_email = ((recorded_by.get("email") or "").strip().lower())
        meeting_title = normalize_spaces(m.get("meeting_title") or m.get("title") or "")

        client_name, client_email = choose_client(invitees, recorded_by_email, meeting_title)
        client_email = client_email or "unknown@example.com"

        client_label = client_name if client_name else "Unknown"
        client_full = f"{client_label} ({client_email})"

        rows.append(
            Row(
                client=client_full,
                email=client_email,
                created_at=parse_dt(m.get("created_at") or ""),
                recording_id=str(m.get("recording_id") or ""),
                share_url=str(m.get("share_url") or ""),
                meeting_title=normalize_spaces(m.get("meeting_title") or m.get("title") or ""),
            )
        )

    # Sort: client alpha, then date desc inside client file
    rows.sort(key=lambda r: (r.client.lower(), r.created_at))

    # Index files
    index_csv = OUT_BASE / "index.csv"
    with index_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["client", "email", "created_at", "recording_id", "share_url", "meeting_title"])
        for r in rows:
            w.writerow([r.client, r.email, r.created_at, r.recording_id, r.share_url, r.meeting_title])

    (OUT_BASE / "index.json").write_text(
        json.dumps([r.__dict__ for r in rows], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    # Per-client docs
    by_client: Dict[str, List[Row]] = {}
    for r in rows:
        by_client.setdefault(r.client, []).append(r)

    for client, items in by_client.items():
        items_sorted = sorted(items, key=lambda r: r.created_at, reverse=True)
        letter = (client[:1] or "U").upper()
        if not ("A" <= letter <= "Z"):
            letter = "U"

        out_dir = CLIENTS_DIR / letter
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{safe_filename(client)}.md"

        lines = [f"# {client}", "", f"Total calls: {len(items_sorted)}", ""]
        for r in items_sorted:
            lines.append(f"- {r.created_at} | {r.meeting_title}")
            lines.append(f"  {r.share_url}")
        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({"ok": True, "meetings": len(meetings), "rows": len(rows), "out": str(OUT_BASE)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
