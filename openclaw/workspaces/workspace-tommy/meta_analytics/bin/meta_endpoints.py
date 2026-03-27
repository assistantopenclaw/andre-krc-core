#!/usr/bin/env python3
"""Meta endpoint helpers.

We keep this conservative/read-only.

Primary objects:
- FB Pages accessible by token: /me/accounts
- Page -> IG business account: /{page_id}?fields=instagram_business_account

Insights endpoints:
- Page insights (requires Page access token): /{page_id}/insights
- IG account insights: /{ig_user_id}/insights
- IG media list: /{ig_user_id}/media
- IG media comments: /{ig_media_id}/comments

Note: Metric availability varies by asset and API version; we probe/handle errors.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from meta_graph_client import MetaClient, MetaAPIError

# Lead intent keyword set (Option B) — used to detect opt-in style comments.
LEAD_INTENT_PHRASES = [
    "next chapter",
    "nextchapter",
    "ready for next chapter",
    "i want the next chapter",
    "want the next chapter",
    "send me the next chapter",
    "how do i get the next chapter",
    "where do i get the next chapter",
    "i need the next chapter",
]


@dataclass
class MetaContext:
    page_id: str
    page_name: Optional[str] = None
    page_access_token: Optional[str] = None
    ig_user_id: Optional[str] = None


def list_pages(client: MetaClient) -> List[Dict[str, Any]]:
    # Returns pages the token can access. Request page access_token too.
    out: List[Dict[str, Any]] = []
    payload = client.get("me/accounts", params={"fields": "id,name,access_token"})
    for row in payload.get("data", []) or []:
        if isinstance(row, dict) and row.get("id"):
            out.append(row)
    return out


def get_instagram_business_account_id(client: MetaClient, page_id: str) -> Optional[str]:
    payload = client.get(page_id, params={"fields": "instagram_business_account"})
    iba = payload.get("instagram_business_account")
    if isinstance(iba, dict):
        return iba.get("id")
    return None


def with_token(client: MetaClient, token: str) -> MetaClient:
    # clone client with different token (used for Page access token calls)
    return MetaClient(token=token, version=client.version, base_url=client.base_url, timeout_s=client.timeout_s)


def pull_page_insights(
    client: MetaClient,
    page_id: str,
    since_unix: int,
    until_unix: int,
) -> Dict[str, Any]:
    # Must be called with a Page Access Token (Graph requirement).
    # We’ll tune metrics after we confirm what’s supported for your Page.
    # NOTE: Metric availability varies by Page type and API version.
    # These are confirmed working against Andre’s Page via probe.
    metrics = [
        "page_impressions_unique",
        "page_post_engagements",
        "page_views_total",
    ]
    return client.get(
        f"{page_id}/insights",
        params={
            "metric": ",".join(metrics),
            "period": "day",
            "since": since_unix,
            "until": until_unix,
        },
    )


def pull_ig_account_insights(
    client: MetaClient,
    ig_user_id: str,
    since_unix: int,
    until_unix: int,
) -> Dict[str, Any]:
    # Metric availability varies; these are confirmed valid for Andre’s IG.
    # Note: profile_views requires metric_type=total_value.
    reach = client.get(
        f"{ig_user_id}/insights",
        params={
            "metric": "reach",
            "period": "day",
            "since": since_unix,
            "until": until_unix,
        },
    )
    follower_count = client.get(
        f"{ig_user_id}/insights",
        params={
            "metric": "follower_count",
            "period": "day",
            "since": since_unix,
            "until": until_unix,
        },
    )
    profile_views = client.get(
        f"{ig_user_id}/insights",
        params={
            "metric": "profile_views",
            "metric_type": "total_value",
            "period": "day",
            "since": since_unix,
            "until": until_unix,
        },
    )
    return {"reach": reach, "follower_count": follower_count, "profile_views": profile_views}


def list_ig_media(
    client: MetaClient,
    ig_user_id: str,
    *,
    limit: int = 50,
    since_iso_date: Optional[str] = None,
    max_items: int = 120,
) -> List[Dict[str, Any]]:
    """List recent IG media.

    We page until:
    - we reach max_items, or
    - the oldest returned media is older than since_iso_date (YYYY-MM-DD)

    Note: the IG media edge is reverse-chronological.
    """
    fields = "id,caption,media_type,media_product_type,permalink,timestamp"
    out: List[Dict[str, Any]] = []
    after: Optional[str] = None

    def _is_before_cutoff(ts: str) -> bool:
        if not since_iso_date:
            return False
        # timestamp is ISO; compare date portion.
        return (ts or "")[:10] < since_iso_date

    while True:
        params: Dict[str, Any] = {"fields": fields, "limit": limit}
        if after:
            params["after"] = after
        payload = client.get(f"{ig_user_id}/media", params=params)

        rows = payload.get("data", []) or []
        if not isinstance(rows, list) or not rows:
            break

        for row in rows:
            if isinstance(row, dict) and row.get("id"):
                out.append(row)

        if len(out) >= max_items:
            out = out[:max_items]
            break

        # Stop if oldest item in this page is older than cutoff.
        oldest_ts = None
        for row in reversed(rows):
            if isinstance(row, dict) and row.get("timestamp"):
                oldest_ts = str(row.get("timestamp"))
                break
        if oldest_ts and _is_before_cutoff(oldest_ts):
            break

        paging = payload.get("paging") or {}
        cursors = paging.get("cursors") or {}
        after = cursors.get("after")
        if not after:
            break

    # If cutoff provided, filter out anything before it.
    if since_iso_date:
        out = [r for r in out if (str(r.get("timestamp") or "")[:10] >= since_iso_date)]

    return out


def list_ig_comments(client: MetaClient, media_id: str, *, limit: int = 50) -> List[Dict[str, Any]]:
    # Fields: text + timestamp + username if available.
    fields = "id,text,timestamp,username"
    payload = client.get(f"{media_id}/comments", params={"fields": fields, "limit": limit})
    out: List[Dict[str, Any]] = []
    for row in payload.get("data", []) or []:
        if isinstance(row, dict) and row.get("id"):
            out.append(row)
    return out


def get_ig_media_reach(client: MetaClient, media_id: str) -> Optional[int]:
    """Best-effort per-media reach.

    Meta metric support varies by media type (REELS/VIDEO/IMAGE). We attempt `reach`.
    Returns None if not available.
    """
    try:
        payload = client.get(f"{media_id}/insights", params={"metric": "reach"})
        data = payload.get("data") or []
        if isinstance(data, list) and data:
            row = data[0]
            if isinstance(row, dict):
                values = row.get("values")
                # Sometimes it's a list; sometimes it's a scalar in 'value'
                if isinstance(values, list) and values:
                    v0 = values[0]
                    if isinstance(v0, dict) and isinstance(v0.get("value"), (int, float)):
                        return int(v0["value"])
                if isinstance(row.get("value"), (int, float)):
                    return int(row["value"])
    except Exception:
        return None
    return None


def comment_is_lead_intent(text: str) -> bool:
    t = (text or "").strip().lower()
    if not t:
        return False
    return any(p in t for p in LEAD_INTENT_PHRASES)


def discover_context(client: MetaClient, *, preferred_page_name: Optional[str] = None) -> MetaContext:
    pages = list_pages(client)
    if not pages:
        raise MetaAPIError("No Pages returned for token. Ensure pages_show_list + page asset assignment is configured.")

    chosen = pages[0]
    if preferred_page_name:
        for p in pages:
            if (p.get("name") or "").strip().lower() == preferred_page_name.strip().lower():
                chosen = p
                break

    page_id = str(chosen["id"])
    page_name = chosen.get("name")
    page_access_token = chosen.get("access_token")
    ig_user_id = get_instagram_business_account_id(client, page_id)

    return MetaContext(
        page_id=page_id,
        page_name=page_name,
        page_access_token=page_access_token,
        ig_user_id=ig_user_id,
    )
