import urllib.request
import json
import os
import sys

api_key = os.environ.get("FATHOM_API_KEY")
target_url = sys.argv[1]

url = "https://api.fathom.ai/external/v1/meetings?limit=100"
headers = {"X-Api-Key": api_key, "Accept": "application/json"}

while url:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        for item in data.get("items", []):
            if item.get("share_url") == target_url:
                print(json.dumps(item))
                sys.exit(0)
        
        cursor = data.get("next_cursor")
        if cursor:
            # Need to encode the cursor
            from urllib.parse import quote
            url = f"https://api.fathom.ai/external/v1/meetings?limit=100&cursor={quote(cursor)}"
        else:
            url = None

print("NOT_FOUND")
