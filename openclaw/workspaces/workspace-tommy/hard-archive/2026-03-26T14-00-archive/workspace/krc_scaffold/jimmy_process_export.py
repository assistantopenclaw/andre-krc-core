import os
import sys
from pathlib import Path

from run_helpers import FINISHED_DIR, append_log, load_manifest, write_manifest


def main():
    if len(sys.argv) < 2:
        print("Usage: jimmy_process_export.py <EXPORT_PATH>", file=sys.stderr)
        return 1

    export_path = sys.argv[1]
    base = os.path.basename(export_path)
    run_id = base.split("__")[0]

    m = load_manifest(run_id)
    if not m:
        m = {
            "run_id": run_id,
            "source_url": None,
            "url_hash": None,
            "status": "fail",
            "raw_transcript_file": None,
            "nugget_export_file": export_path,
            "finished_content_file(s)": [],
            "created_at": None,
            "updated_at": None,
            "error_message": "Manifest missing when Jimmy started",
        }
        write_manifest(m)

    append_log(run_id, f"JIMMY START export={export_path}")

    if not os.path.exists(export_path):
        m["status"] = "fail"
        m["error_message"] = f"Export file not found: {export_path}"
        write_manifest(m)
        append_log(run_id, m["error_message"])
        print(run_id)
        return 4

    Path(FINISHED_DIR).mkdir(parents=True, exist_ok=True)
    finished_path = os.path.join(FINISHED_DIR, f"{run_id}__finished_content.md")
    with open(finished_path, "w", encoding="utf-8") as f:
        f.write(
            "# Finished Content\n\n"
            f"RUN_ID: {run_id}\n\n"
            "(Placeholder — Jimmy identity/soul will generate captions + 3 hooks per caption.)\n"
        )

    m["finished_content_file(s)"] = [finished_path]
    m["status"] = "success"
    m["error_message"] = None
    write_manifest(m)
    append_log(run_id, f"WROTE finished_content_file={finished_path}")

    print(run_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
