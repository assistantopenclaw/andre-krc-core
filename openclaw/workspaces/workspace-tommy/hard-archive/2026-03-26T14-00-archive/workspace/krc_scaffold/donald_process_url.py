import os
import re
import sys
import subprocess
from pathlib import Path

from run_helpers import (
    ALLOWED_DOMAIN_SUBSTR_DEFAULT,
    RAW_DIR,
    NUGGET_DIR,
    append_log,
    find_existing_success,
    new_run_id,
    sanitize_filename,
    url_hash,
    write_manifest,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: donald_process_url.py <URL> [REPROCESS]", file=sys.stderr)
        return 1

    url = sys.argv[1].strip()
    reprocess = any(a.strip().upper() == "REPROCESS" for a in sys.argv[2:])

    run_id = new_run_id(url)

    m = {
        "run_id": run_id,
        "source_url": url,
        "url_hash": url_hash(url),
        "status": "fail",
        "raw_transcript_file": None,
        "nugget_export_file": None,
        "finished_content_file(s)": [],
        "created_at": None,
        "updated_at": None,
        "error_message": None,
    }
    write_manifest(m)
    append_log(run_id, f"START run_id={run_id} url={url}")

    # Domain allow check
    allowed_substr = os.environ.get("KRC_ALLOWED_DOMAIN_SUBSTR", ALLOWED_DOMAIN_SUBSTR_DEFAULT)
    if allowed_substr and allowed_substr not in url:
        m["error_message"] = f"Domain not allowed. Required substring: {allowed_substr}"
        write_manifest(m)
        append_log(run_id, m["error_message"])
        print(run_id)
        return 2

    # Idempotency
    existing = find_existing_success(url)
    if existing and not reprocess:
        append_log(run_id, f"SKIP already processed successfully as RUN_ID={existing}")
        m["status"] = "success"
        m["error_message"] = None
        write_manifest(m)
        print(run_id)
        return 0

    # Fetch (no requests dependency): curl
    try:
        res = subprocess.run(
            ["curl", "-fsSL", "--max-time", "30", url],
            capture_output=True,
            text=True,
            check=True,
        )
        html = res.stdout
    except Exception as e:
        m["error_message"] = f"Fetch failed: {e}"
        write_manifest(m)
        append_log(run_id, m["error_message"])
        print(run_id)
        return 3

    # Save raw transcript (placeholder: saves fetched page text)
    Path(RAW_DIR).mkdir(parents=True, exist_ok=True)
    base = sanitize_filename(url)[:60]
    raw_path = os.path.join(RAW_DIR, f"{run_id}__{base}.txt")
    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(html)

    m["raw_transcript_file"] = raw_path
    write_manifest(m)
    append_log(run_id, f"WROTE raw_transcript_file={raw_path}")

    # Placeholder nugget export
    Path(NUGGET_DIR).mkdir(parents=True, exist_ok=True)
    export_path = os.path.join(NUGGET_DIR, f"{run_id}__gold_nugget_export.md")
    with open(export_path, "w", encoding="utf-8") as f:
        f.write(
            "# Gold Nugget Export\n\n"
            f"RUN_ID: {run_id}\n\n"
            "(Placeholder export — Donald identity/soul will implement nugget extraction + scoring rules.)\n"
        )

    m["nugget_export_file"] = export_path
    m["status"] = "success"
    write_manifest(m)
    append_log(run_id, f"WROTE nugget_export_file={export_path}")

    print(run_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
