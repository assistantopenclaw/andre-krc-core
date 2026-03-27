#!/usr/bin/env python3
"""Meta Graph API client (read-only).

- Uses System User access token.
- Simple requests-based client with robust error reporting.

Env:
- META_SYSTEM_USER_TOKEN
- META_GRAPH_VERSION (default v19.0)
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

import urllib.parse
import urllib.request


class MetaAPIError(RuntimeError):
    def __init__(self, message: str, *, status: Optional[int] = None, payload: Any = None):
        super().__init__(message)
        self.status = status
        self.payload = payload


@dataclass
class MetaClient:
    token: str
    version: str = "v19.0"
    base_url: str = "https://graph.facebook.com"
    timeout_s: int = 45

    @classmethod
    def from_env(cls) -> "MetaClient":
        token = os.environ.get("META_SYSTEM_USER_TOKEN", "").strip()
        if not token:
            raise MetaAPIError("META_SYSTEM_USER_TOKEN is not set")
        version = os.environ.get("META_GRAPH_VERSION", "v19.0").strip() or "v19.0"
        return cls(token=token, version=version)

    def _url(self, path: str) -> str:
        path = path.lstrip("/")
        return f"{self.base_url}/{self.version}/{path}"

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if params is None:
            params = {}
        # Always pass access token in query params for Graph API
        params = {**params, "access_token": self.token}

        t0 = time.time()
        url = self._url(path)
        qs = urllib.parse.urlencode(params, doseq=True)
        full = f"{url}?{qs}" if qs else url

        req = urllib.request.Request(full, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=self.timeout_s) as resp:
                status = getattr(resp, "status", 200)
                body = resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            status = e.code
            body = e.read().decode("utf-8", errors="replace")
        except Exception as e:
            dt_s = time.time() - t0
            raise MetaAPIError(f"Meta request failed GET {path} ({dt_s:.2f}s): {e}")

        dt_s = time.time() - t0

        try:
            payload = json.loads(body)
        except Exception:
            payload = {"non_json_body": body[:2000]}

        if status >= 400:
            raise MetaAPIError(
                f"Meta Graph API error {status} GET {path} ({dt_s:.2f}s)",
                status=status,
                payload=payload,
            )

        if isinstance(payload, dict) and "error" in payload:
            raise MetaAPIError(
                f"Meta Graph API logical error GET {path} ({dt_s:.2f}s)",
                status=status,
                payload=payload,
            )

        if not isinstance(payload, dict):
            raise MetaAPIError(
                f"Unexpected Meta response type: {type(payload)}",
                status=status,
                payload=payload,
            )

        return payload


def pretty_json(obj: Any) -> str:
    return json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False)
