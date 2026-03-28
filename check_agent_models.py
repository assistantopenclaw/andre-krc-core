import json

with open("/home/openclaw_agent_1/.openclaw/openclaw.json") as f:
    config = json.load(f)

# Only check agents with an explicit locked expectation here.
# Ignore legacy/specialized agents so the script never crashes when the roster expands.
expected = {
    "main": "openrouter/openai/gpt-5-mini",
    "tommy": "openrouter/openai/gpt-5.4",
    "research": "openrouter/google/gemini-3-flash-preview",
    "tasklist": "openrouter/openai/gpt-5-nano",
    "alex": "openrouter/moonshotai/kimi-k2-thinking",
    "transcriptscraper": "openrouter/google/gemini-3-flash-preview",
    "contentwriter": "openrouter/anthropic/claude-sonnet-4.6",
    "manager": "openrouter/openai/gpt-5-mini",
}

problems = []
for agent in config["agents"]["list"]:
    aid = agent["id"]
    if aid not in expected:
        continue
    m = agent.get("model")
    if m is None:
        problems.append(f"DRIFT: {aid} has NO explicit model (inheriting default)")
        continue
    if isinstance(m, dict):
        primary = m.get("primary", "MISSING")
    else:
        primary = m
    if primary != expected[aid]:
        problems.append(f"MISMATCH: {aid} expected {expected[aid]} got {primary}")

if problems:
    for p in problems:
        print(p)
else:
    print("ALL_CLEAR")
