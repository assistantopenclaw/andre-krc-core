#!/usr/bin/env python3
"""Orchestrates Meta analytics pull + Google Doc report upload.

Design goals:
- Read-only
- Deterministic: raw JSON snapshots + normalized summary
- No fabricated numbers: failures produce an error report only

Requires:
- META_SYSTEM_USER_TOKEN
- GDRIVE_CONTENT_ANALYTICS_FOLDER_ID
Optional:
- META_PAGE_ID (if you want to pin a specific FB Page)
- META_PREFERRED_PAGE_NAME (for first-time discovery)
- META_GRAPH_VERSION (default v19.0)
"""

from __future__ import annotations

import datetime as dt
import json
import os
import sys
import tempfile
from pathlib import Path
from zoneinfo import ZoneInfo

from meta_graph_client import MetaClient, MetaAPIError, pretty_json
import meta_endpoints as ep


CHI = ZoneInfo("America/Chicago")


def spelled_date(ts: dt.datetime) -> str:
    # Example: March 1, 2026
    return ts.strftime("%B %-d, %Y")


def unix(ts: dt.datetime) -> int:
    return int(ts.timestamp())


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False))


def _extract_daily_series(payload: dict) -> dict:
    """Convert Graph insights payload into {metric_name: [(date_str, value), ...]}"""
    out: dict = {}
    for row in (payload.get("data") or []):
        if not isinstance(row, dict):
            continue
        name = row.get("name")
        values = row.get("values") or []
        series = []
        for v in values:
            if not isinstance(v, dict):
                continue
            end_time = v.get("end_time")
            val = v.get("value")
            # end_time is ISO; keep date for readability
            if end_time:
                series.append((str(end_time)[:10], val))
        if name:
            out[name] = series
    return out


def _sum_last_n_days(series: list[tuple[str, object]], n: int) -> int:
    # Values are usually ints; ignore non-numeric.
    total = 0
    for _, v in series[-n:]:
        if isinstance(v, (int, float)):
            total += int(v)
    return total


def build_markdown_report(
    now: dt.datetime,
    ctx: ep.MetaContext,
    page_insights: dict,
    ig_insights: dict | None,
    lead_intent: dict | None,
) -> str:
    lines: list[str] = []
    lines.append(f"# Meta Analytics — {spelled_date(now)} — {now.strftime('%-I:%M %p')} CT")
    lines.append("")
    lines.append("## What this means (plain English)")
    lines.append("This report answers three questions:")
    lines.append("1) Are we reaching more people?")
    lines.append("2) Are we converting reach into followers?")
    lines.append("3) Are people opting-in via ‘next chapter’ comments?")
    lines.append("")

    lines.append("## Sources")
    lines.append(f"- Facebook Page: {ctx.page_name or ''} (`{ctx.page_id}`)")
    if ctx.ig_user_id:
        lines.append(f"- Instagram Professional Account ID: `{ctx.ig_user_id}`")
    else:
        lines.append("- Instagram Professional Account ID: **NOT FOUND** (Page not linked to IG or missing permissions)")
    lines.append("")

    # Extract series
    fb_series = _extract_daily_series(page_insights)
    ig_reach_series = None
    ig_follow_series = None
    ig_profile_views_total = None
    if isinstance(ig_insights, dict):
        ig_reach_series = _extract_daily_series(ig_insights.get("reach", {})).get("reach")
        ig_follow_series = _extract_daily_series(ig_insights.get("follower_count", {})).get("follower_count")
        # profile_views comes back as total_value; not a values[] series.
        pv = (ig_insights.get("profile_views", {}) or {}).get("data")
        if isinstance(pv, list) and pv:
            tv = pv[0].get("total_value") if isinstance(pv[0], dict) else None
            if isinstance(tv, dict) and isinstance(tv.get("value"), (int, float)):
                ig_profile_views_total = int(tv["value"])

    # Compute readable rollups
    fb_unique = fb_series.get("page_impressions_unique") or []
    fb_post_eng = fb_series.get("page_post_engagements") or []
    fb_views = fb_series.get("page_views_total") or []

    fb_1d = {
        "unique_impressions": _sum_last_n_days(fb_unique, 1),
        "post_engagements": _sum_last_n_days(fb_post_eng, 1),
        "page_views": _sum_last_n_days(fb_views, 1),
    }
    fb_7d = {
        "unique_impressions": _sum_last_n_days(fb_unique, 7),
        "post_engagements": _sum_last_n_days(fb_post_eng, 7),
        "page_views": _sum_last_n_days(fb_views, 7),
    }
    fb_30d = {
        "unique_impressions": _sum_last_n_days(fb_unique, 30),
        "post_engagements": _sum_last_n_days(fb_post_eng, 30),
        "page_views": _sum_last_n_days(fb_views, 30),
    }

    ig_1d_reach = _sum_last_n_days(ig_reach_series or [], 1) if ig_reach_series else None
    ig_7d_reach = _sum_last_n_days(ig_reach_series or [], 7) if ig_reach_series else None
    ig_30d_reach = _sum_last_n_days(ig_reach_series or [], 30) if ig_reach_series else None

    # Followers: follower_count is a daily value series, not a delta. We compute delta as last - first in window.
    ig_follow_delta_7d = None
    ig_follow_delta_30d = None
    if ig_follow_series and len(ig_follow_series) >= 2:
        def _last_first_delta(series, n):
            s = series[-n:]
            vals = [v for _, v in s if isinstance(v, (int, float))]
            return int(vals[-1] - vals[0]) if len(vals) >= 2 else None
        ig_follow_delta_7d = _last_first_delta(ig_follow_series, 7)
        ig_follow_delta_30d = _last_first_delta(ig_follow_series, 30)

    # Executive scoreboard
    lines.append("## Scoreboard (read this)")
    lines.append("### Instagram")
    if ig_1d_reach is not None:
        lines.append(f"- Reach (last 1 day): **{ig_1d_reach:,}**")
    if ig_7d_reach is not None:
        lines.append(f"- Reach (last 7 days): **{ig_7d_reach:,}**")
    if ig_30d_reach is not None:
        lines.append(f"- Reach (last 30 days): **{ig_30d_reach:,}**")
    if ig_follow_delta_7d is not None:
        lines.append(f"- Followers (change, last 7 days): **{ig_follow_delta_7d:+,}**")
    if ig_follow_delta_30d is not None:
        lines.append(f"- Followers (change, last 30 days): **{ig_follow_delta_30d:+,}**")
    if ig_profile_views_total is not None:
        lines.append(f"- Profile visits (total in window): **{ig_profile_views_total:,}**")

    lines.append("")
    lines.append("### Facebook")
    lines.append(f"- Unique impressions (last 1 day): **{fb_1d['unique_impressions']:,}**")
    lines.append(f"- Unique impressions (last 7 days): **{fb_7d['unique_impressions']:,}**")
    lines.append(f"- Unique impressions (last 30 days): **{fb_30d['unique_impressions']:,}**")
    lines.append(f"- Post engagements (last 7 days): **{fb_7d['post_engagements']:,}**")
    lines.append(f"- Page views (last 7 days): **{fb_7d['page_views']:,}**")

    if lead_intent:
        lines.append("")
        lines.append("### Leads (opt-ins)")
        lines.append(f"- ‘Next chapter’ comment matches (recent scan): **{lead_intent.get('match_count', 0)}**")

    lines.append("")

    if lead_intent:
        lines.append("## Lead Intent — ‘Next chapter’ opt-ins (IG comments)")
        lines.append(f"Scanned media: {lead_intent.get('media_scanned', 0)} · Comments scanned: {lead_intent.get('comments_scanned', 0)}")
        lines.append("")

        def _render_top(label: str, items: list[dict], n: int) -> None:
            if not items:
                lines.append(f"### {label}")
                lines.append("- None found in this window.")
                lines.append("")
                return
            lines.append(f"### {label}")
            for i, p in enumerate(items[:n], 1):
                ts = (p.get("timestamp") or "")
                d = ts[:10] if ts else ""
                lines.append(
                    f"{i}. {d} · Opt-in comments: **{p.get('opt_in_count', 0)}** · Reach: {p.get('reach') if p.get('reach') is not None else 'n/a'}"
                )
                if p.get('permalink'):
                    lines.append(f"   Link: {p['permalink']}")
                cap = (p.get('caption') or '').replace('\n',' ').strip()
                if cap:
                    if len(cap) > 180:
                        cap = cap[:177] + '...'
                    lines.append(f"   Caption: {cap}")
            lines.append("")

        # Windowed rankings
        top_30d = lead_intent.get("top_30d", []) or []
        top_7d = lead_intent.get("top_7d", []) or []
        top_24h = lead_intent.get("top_24h", []) or []

        _render_top("Top 20 posts (last 30 days) — by opt-in comments", top_30d, 20)
        _render_top("Top 10 posts (last 7 days) — by opt-in comments", top_7d, 10)
        _render_top("Top 2 posts (last 24 hours) — by opt-in comments", top_24h, 2)

        matches = lead_intent.get('matches', []) or []
        if not matches:
            lines.append("- No opt-in comments found in the scanned window.")
        else:
            lines.append("### Sample opt-in comments")
            for i, m in enumerate(matches[:20], 1):
                txt = (m.get('text') or '').replace('\n', ' ').strip()
                if len(txt) > 220:
                    txt = txt[:217] + '...'
                lines.append(f"{i}. {txt}")
                if m.get('permalink'):
                    lines.append(f"   Link: {m['permalink']}")
        lines.append("")

    # Keep raw JSON for audit/debug (trimmed)
    lines.append("## Raw Data (for audit/debug)")
    lines.append("### Facebook Page Insights (raw)")
    lines.append("```json")
    lines.append(json.dumps(page_insights, indent=2, ensure_ascii=False)[:120000])
    lines.append("```")
    lines.append("")

    if ig_insights is not None:
        lines.append("### Instagram Account Insights (raw)")
        lines.append("```json")
        lines.append(json.dumps(ig_insights, indent=2, ensure_ascii=False)[:120000])
        lines.append("```")
        lines.append("")

    lines.append("## Notes")
    lines.append("- Automated read-only pull via Meta Graph API.")
    lines.append("- This report intentionally excludes ads analytics.")

    return "\n".join(lines)


def upload_google_doc(*, markdown: str, title: str) -> dict:
    folder_id = os.environ.get("GDRIVE_CONTENT_ANALYTICS_FOLDER_ID", "").strip()
    if not folder_id:
        raise RuntimeError("GDRIVE_CONTENT_ANALYTICS_FOLDER_ID is not set")

    # Write to temp file then upload, convert to Google Doc.
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "report.md"
        p.write_text(markdown, encoding="utf-8")

        import subprocess

        cmd = [
            "gog",
            "drive",
            "upload",
            str(p),
            "--convert-to",
            "doc",
            "--parent",
            folder_id,
            "--name",
            title,
            "--json",
            "--results-only",
        ]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError(f"Drive upload failed: {r.stderr.strip() or r.stdout.strip()}")
        return json.loads(r.stdout)


def main() -> int:
    now = dt.datetime.now(tz=CHI)

    try:
        client = MetaClient.from_env()

        # Define reporting window: last 30 days (we’ll derive 1d/7d/30d views from this).
        # Meta 'since'/'until' are unix seconds; we’ll use day-aligned window.
        # Keep within Meta's <=30-day constraint between since/until.
        # Use 29 days back, aligned to midnight, which stays safely under the 30-day seconds limit.
        start = (now - dt.timedelta(days=29)).replace(hour=0, minute=0, second=0, microsecond=0)
        end = now.replace(second=0, microsecond=0)

        page_id = os.environ.get("META_PAGE_ID", "").strip() or None
        preferred_page_name = os.environ.get("META_PREFERRED_PAGE_NAME", "").strip() or None

        if page_id:
            # If page is pinned, we still need a Page access token. Best-effort:
            # user can set META_PAGE_ACCESS_TOKEN in env if needed.
            page_access_token = os.environ.get("META_PAGE_ACCESS_TOKEN", "").strip() or None
            ctx = ep.MetaContext(
                page_id=page_id,
                page_name=None,
                page_access_token=page_access_token,
                ig_user_id=ep.get_instagram_business_account_id(client, page_id),
            )
        else:
            ctx = ep.discover_context(client, preferred_page_name=preferred_page_name)

        if not ctx.page_access_token:
            raise MetaAPIError(
                "Missing Page access token. Ensure token has pages_show_list/pages_read_engagement and that the Page is assigned to the System User."
            )

        page_client = ep.with_token(client, ctx.page_access_token)
        page_insights = ep.pull_page_insights(page_client, ctx.page_id, unix(start), unix(end))

        ig_insights = None
        lead_intent = None
        if ctx.ig_user_id:
            # IG insights generally also accept the Page access token when the IG is linked to the Page.
            ig_insights = ep.pull_ig_account_insights(page_client, ctx.ig_user_id, unix(start), unix(end))

            # Lead intent: scan recent IG media comments for opt-in phrases.
            try:
                # Pull enough media to cover the last 30 days for ranking.
                cutoff_30d = (now - dt.timedelta(days=30)).strftime("%Y-%m-%d")
                media = ep.list_ig_media(page_client, ctx.ig_user_id, limit=50, since_iso_date=cutoff_30d, max_items=200)
                matches = []
                comments_scanned = 0

                per_post_counts = {}  # media_id -> {permalink, caption, opt_in_count, reach}
                for item in media:
                    mid = item.get("id")
                    if not mid:
                        continue
                    permalink = item.get("permalink")
                    caption = item.get("caption")
                    per_post_counts[mid] = {
                        "media_id": mid,
                        "permalink": permalink,
                        "caption": caption,
                        "timestamp": item.get("timestamp"),
                        "opt_in_count": 0,
                        "reach": None,
                    }

                    # best-effort per-media reach
                    per_post_counts[mid]["reach"] = ep.get_ig_media_reach(page_client, mid)

                    comments = ep.list_ig_comments(page_client, mid, limit=50)
                    comments_scanned += len(comments)
                    for c in comments:
                        txt = c.get("text") or ""
                        if ep.comment_is_lead_intent(txt):
                            per_post_counts[mid]["opt_in_count"] += 1
                            matches.append({"text": txt, "permalink": permalink, "media_id": mid})

                top_posts = sorted(per_post_counts.values(), key=lambda x: x.get("opt_in_count", 0), reverse=True)

                def _in_last_hours(ts: str, hours: int) -> bool:
                    try:
                        t = dt.datetime.fromisoformat(ts.replace('Z', '+00:00'))
                        if t.tzinfo is None:
                            t = t.replace(tzinfo=dt.timezone.utc)
                        # Convert to Chicago for comparison
                        t_chi = t.astimezone(CHI)
                        return (now - t_chi) <= dt.timedelta(hours=hours)
                    except Exception:
                        return False

                def _in_last_days(ts: str, days: int) -> bool:
                    try:
                        t = dt.datetime.fromisoformat(ts.replace('Z', '+00:00'))
                        if t.tzinfo is None:
                            t = t.replace(tzinfo=dt.timezone.utc)
                        t_chi = t.astimezone(CHI)
                        return (now - t_chi) <= dt.timedelta(days=days)
                    except Exception:
                        return False

                top_30d = [p for p in top_posts if _in_last_days(str(p.get('timestamp','')), 30)]
                top_7d = [p for p in top_posts if _in_last_days(str(p.get('timestamp','')), 7)]
                top_24h = [p for p in top_posts if _in_last_hours(str(p.get('timestamp','')), 24)]

                lead_intent = {
                    "media_scanned": len(media),
                    "comments_scanned": comments_scanned,
                    "match_count": len(matches),
                    "matches": matches,
                    "top_posts": top_posts,
                    "top_30d": top_30d,
                    "top_7d": top_7d,
                    "top_24h": top_24h,
                    "phrases": ep.LEAD_INTENT_PHRASES,
                }
            except Exception as _e:
                # Do not fail the run just because comment scan fails; keep it best-effort.
                lead_intent = {"error": str(_e), "match_count": 0, "matches": [], "phrases": ep.LEAD_INTENT_PHRASES}

        # Persist raw snapshots locally (workspace).
        out_dir = Path(__file__).resolve().parents[1] / "data" / now.strftime("%Y-%m-%d") / now.strftime("%H%M%S")
        write_json(
            out_dir / "meta_context.json",
            {
                "page_id": ctx.page_id,
                "page_name": ctx.page_name,
                "ig_user_id": ctx.ig_user_id,
                "has_page_access_token": bool(ctx.page_access_token),
            },
        )
        write_json(out_dir / "page_insights.json", page_insights)
        if ig_insights is not None:
            write_json(out_dir / "ig_insights.json", ig_insights)
        if lead_intent is not None:
            write_json(out_dir / "lead_intent.json", lead_intent)

        title = f"{spelled_date(now)} — {now.strftime('%-I:%M %p')} CT — Meta Analytics (IG + FB)"
        md = build_markdown_report(now, ctx, page_insights, ig_insights, lead_intent)
        drive_meta = upload_google_doc(markdown=md, title=title)

        summary = {
            "ok": True,
            "title": title,
            "drive": {
                "id": drive_meta.get("id"),
                "name": drive_meta.get("name"),
                "webViewLink": drive_meta.get("webViewLink"),
            },
            "local_snapshot_dir": str(out_dir),
        }
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0

    except MetaAPIError as e:
        err = {
            "ok": False,
            "error": str(e),
            "status": getattr(e, "status", None),
            "payload": getattr(e, "payload", None),
        }
        print(json.dumps(err, indent=2, ensure_ascii=False))
        return 2
    except Exception as e:
        err = {"ok": False, "error": str(e)}
        print(json.dumps(err, indent=2, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
