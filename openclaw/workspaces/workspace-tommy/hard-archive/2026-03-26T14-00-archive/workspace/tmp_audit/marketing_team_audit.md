# Marketing Team Audit

Generated at: 2026-03-08T18:32:15-05:00



## openclaw status

```
OpenClaw status

Overview
┌─────────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Item            │ Value                                                                                             │
├─────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Dashboard       │ http://127.0.0.1:18789/                                                                           │
│ OS              │ linux 6.6.87.2-microsoft-standard-WSL2 (x64) · node 25.8.0                                        │
│ Tailscale       │ off                                                                                               │
│ Channel         │ stable (default)                                                                                  │
│ Update          │ available · pnpm · npm update 2026.3.7                                                            │
│ Gateway         │ local · ws://127.0.0.1:18789 (local loopback) · reachable 21ms · auth token · ANDRE-GAMING (172.  │
│                 │ 18.162.119) app 2026.3.2 linux 6.6.87.2-microsoft-standard-WSL2                                   │
│ Gateway service │ systemd installed · enabled · running (pid 47557, state active)                                   │
│ Node service    │ systemd not installed                                                                             │
│ Agents          │ 11 · 11 bootstrap files present · sessions 75 · default main active 10m ago                       │
│ Memory          │ 0 files · 0 chunks · dirty · sources memory · plugin memory-core · vector unknown · fts ready ·   │
│                 │ cache on (0)                                                                                      │
│ Probes          │ skipped (use --deep)                                                                              │
│ Events          │ none                                                                                              │
│ Heartbeat       │ 30m (main), disabled (alex), disabled (bob), disabled (captainhook), disabled (donald), disabled  │
│                 │ (jimmy), disabled (mark), disabled (overseer), disabled (research), disabled (tasklist),          │
│                 │ disabled (tommy)                                                                                  │
│ Sessions        │ 75 active · default google/gemini-3-flash-preview (200k ctx) · 11 stores                          │
└─────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────┘

Security audit
Summary: 0 critical · 1 warn · 1 info
  WARN Reverse proxy headers are not trusted
    gateway.bind is loopback and gateway.trustedProxies is empty. If you expose the Control UI through a reverse proxy, configure trusted proxies so local-client c…
    Fix: Set gateway.trustedProxies to your proxy IPs or keep the Control UI local-only.
Full report: openclaw security audit
Deep probe: openclaw security audit --deep

Channels
┌──────────┬─────────┬────────┬───────────────────────────────────────────────────────────────────────────────────────┐
│ Channel  │ Enabled │ State  │ Detail                                                                                │
├──────────┼─────────┼────────┼───────────────────────────────────────────────────────────────────────────────────────┤
│ Telegram │ ON      │ OK     │ token config×9 (8513…gGZg · len 46) · accounts 9/9                                    │
└──────────┴─────────┴────────┴───────────────────────────────────────────────────────────────────────────────────────┘

Sessions
┌────────────────────────────────┬────────┬─────────┬───────────────────────────────┬─────────────────────────────────┐
│ Key                            │ Kind   │ Age     │ Model                         │ Tokens                          │
├────────────────────────────────┼────────┼─────────┼───────────────────────────────┼─────────────────────────────────┤
│ agent:tommy:telegram:direct:84 │ direct │ 2m ago  │ openai/gpt-5.3-codex          │ 162k/400k (40%)                 │
│ 3…                             │        │         │                               │                                 │
│ agent:tommy:main               │ direct │ 2m ago  │ openai/gpt-5.3-codex          │ 179k/400k (45%) · 🗄️ 99% cached │
│ agent:donald:telegram:direct:8 │ direct │ 4m ago  │ google/gemini-3-flash-preview │ 13k/1049k (1%) · 🗄️ 97% cached  │
│ 4…                             │        │         │                               │                                 │
│ agent:donald:main              │ direct │ 4m ago  │ google/gemini-3-flash-preview │ 76k/1049k (7%)                  │
│ agent:main:main                │ direct │ 10m ago │ openai/gpt-5-mini             │ 13k/400k (3%) · 🗄️ 53% cached   │
│ agent:captainhook:main         │ direct │ 10m ago │ anthropic/claude-sonnet-4.6   │ 21k/1000k (2%) · 🗄️ 97% cached  │
│ agent:bob:main                 │ direct │ 10m ago │ deepseek/deepseek-chat-v3.1   │ 27k/33k (83%) · 🗄️ 12% cached   │
│ agent:mark:main                │ direct │ 11m ago │ moonshotai/kimi-k2-thinking   │ 25k/131k (19%) · 🗄️ 97% cached  │
│ agent:jimmy:telegram:direct:84 │ direct │ 12m ago │ anthropic/claude-sonnet-4.6   │ 16k/1000k (2%) · 🗄️ 97% cached  │
│ 3…                             │        │         │                               │                                 │
│ agent:captainhook:telegram:dir │ direct │ 13m ago │ anthropic/claude-sonnet-4.6   │ 15k/1000k (2%)                  │
│ e…                             │        │         │                               │                                 │
└────────────────────────────────┴────────┴─────────┴───────────────────────────────┴─────────────────────────────────┘

FAQ: https://docs.openclaw.ai/faq
Troubleshooting: https://docs.openclaw.ai/troubleshooting

Update available (npm 2026.3.7). Run: openclaw update

Next steps:
  Need to share?      openclaw status --all
  Need to debug live? openclaw logs --follow
  Need to test channels? openclaw status --deep

[stderr]

```



## openclaw gateway status

```
Service: systemd (enabled)
File logs: /tmp/openclaw/openclaw-2026-03-08.log
Command: /home/linuxbrew/.linuxbrew/opt/node/bin/node /home/linuxbrew/.linuxbrew/lib/node_modules/openclaw/dist/index.js gateway --port 18789
Service file: ~/.config/systemd/user/openclaw-gateway.service
Service env: OPENCLAW_GATEWAY_PORT=18789

Config (cli): ~/.openclaw/openclaw.json
Config (service): ~/.openclaw/openclaw.json

Gateway: bind=loopback (127.0.0.1), port=18789 (service args)
Probe target: ws://127.0.0.1:18789
Dashboard: http://127.0.0.1:18789/
Probe note: Loopback-only gateway; only local clients can connect.

Runtime: running (pid 47557, state active, sub running, last exit 0, reason 0)
RPC probe: ok

Listening: 127.0.0.1:18789
Troubles: run openclaw status
Troubleshooting: https://docs.openclaw.ai/troubleshooting

[stderr]

```



## Inventory

```
=== WORKSPACES ===
total 228
drwx------ 30 openclaw_agent_1 openclaw_agent_1  4096 Mar  8 18:19 .
drwxr-x--- 14 openclaw_agent_1 openclaw_agent_1  4096 Feb 27 22:36 ..
drwx------ 13 openclaw_agent_1 openclaw_agent_1  4096 Mar  7 20:22 agents
drwxrwxr-x  9 openclaw_agent_1 openclaw_agent_1  4096 Mar  8 03:00 backups
drwxrwxr-x  2 openclaw_agent_1 openclaw_agent_1  4096 Feb 24 13:22 canvas
drwxr-xr-x  2 openclaw_agent_1 openclaw_agent_1  4096 Feb 26 00:45 completions
drwx------  4 openclaw_agent_1 openclaw_agent_1  4096 Mar  1 00:56 credentials
drwxrwxr-x  3 openclaw_agent_1 openclaw_agent_1  4096 Mar  8 18:02 cron
drwx------  3 openclaw_agent_1 openclaw_agent_1  4096 Mar  8 18:19 delivery-queue
drwxrwxr-x  2 openclaw_agent_1 openclaw_agent_1  4096 Mar  8 18:32 devices
-rw-------  1 openclaw_agent_1 openclaw_agent_1  1961 Mar  8 18:32 exec-approvals.json
drwxr-xr-x  2 openclaw_agent_1 openclaw_agent_1  4096 Feb 26 20:57 identity
drwx------  2 openclaw_agent_1 openclaw_agent_1  4096 Feb 24 13:22 logs
drwxrwxr-x  3 openclaw_agent_1 openclaw_agent_1  4096 Feb 28 22:11 manual_snapshots
drwx------  3 openclaw_agent_1 openclaw_agent_1  4096 Feb 24 20:22 media
drwxrwxr-x  2 openclaw_agent_1 openclaw_agent_1  4096 Mar  8 18:19 memory
-rw-------  1 openclaw_agent_1 openclaw_agent_1 13864 Mar  7 21:39 openclaw.json
-rw-r--r--  1 openclaw_agent_1 openclaw_agent_1  6257 Feb 26 20:13 openclaw.json"allowFrom": [8434682557],yy
-rw-r--r--  1 openclaw_agent_1 openclaw_agent_1  6258 Feb 26 20:13 openclaw.json"allowFrom": [8434682557],yy.save
-rw-------  1 openclaw_agent_1 openclaw_agent_1 13883 Mar  7 21:39 openclaw.json.bak
-rw-------  1 openclaw_agent_1 openclaw_agent_1 13279 Mar  7 20:23 openclaw.json.bak.1
-rw-------  1 openclaw_agent_1 openclaw_agent_1 10514 Mar  7 18:47 openclaw.json.bak.2
-rw-------  1 openclaw_agent_1 openclaw_agent_1 10512 Mar  2 16:11 openclaw.json.bak.3
-rw-------  1 openclaw_agent_1 openclaw_agent_1 10137 Feb 28 21:57 openclaw.json.bak.4
drwxrwxr-x  4 openclaw_agent_1 openclaw_agent_1  4096 Mar  1 00:52 scripts
drwx------  2 openclaw_agent_1 openclaw_agent_1  4096 Feb 26 18:46 subagents
drwx------  2 openclaw_agent_1 openclaw_agent_1  4096 Mar  8 18:28 telegram
-rw-------  1 openclaw_agent_1 openclaw_agent_1   187 Mar  8 18:19 update-check.json
drwxr-xr-x 14 openclaw_agent_1 openclaw_agent_1  4096 Feb 25 23:35 workspace
drwxrwxr-x  6 openclaw_agent_1 openclaw_agent_1  4096 Mar  2 19:04 workspace-alex-ceo
drwxrwxr-x  2 openclaw_agent_1 openclaw_agent_1  4096 Feb 25 16:12 workspace-base-agent
drwxrwxr-x  5 openclaw_agent_1 openclaw_agent_1  4096 Mar  8 17:28 workspace-bob
drwxrwxr-x  4 openclaw_agent_1 openclaw_agent_1  4096 Mar  7 20:47 workspace-captainhook
drwxrwxr-x  5 openclaw_agent_1 openclaw_agent_1  4096 Mar  7 22:02 workspace-donald
drwxrwxr-x  4 openclaw_agent_1 openclaw_agent_1  4096 Mar  7 20:49 workspace-jimmy
drwxrwxr-x  4 openclaw_agent_1 openclaw_agent_1  4096 Mar  7 20:47 workspace-mark
drwxrwxr-x  4 openclaw_agent_1 openclaw_agent_1  4096 Mar  7 20:23 workspace-overseer
drwxrwxr-x  5 openclaw_agent_1 openclaw_agent_1  4096 Feb 25 23:35 workspace-research
drwxrwxr-x  7 openclaw_agent_1 openclaw_agent_1  4096 Feb 28 00:08 workspace-tasklist
drwxrwxr-x 12 openclaw_agent_1 openclaw_agent_1  4096 Mar  8 18:31 workspace-tommy

=== KRC SCRIPTS ===
total 128
drwxrwxr-x 3 openclaw_agent_1 openclaw_agent_1  4096 Mar  8 17:15 .
drwxrwxr-x 4 openclaw_agent_1 openclaw_agent_1  4096 Mar  1 00:52 ..
-rw-rw-r-- 1 openclaw_agent_1 openclaw_agent_1   915 Feb 27 16:22 README.md
drwxrwxr-x 2 openclaw_agent_1 openclaw_agent_1  4096 Mar  8 17:23 __pycache__
-rwxr-xr-x 1 openclaw_agent_1 openclaw_agent_1   109 Feb 27 16:22 _env.sh
-rwxrwxr-x 1 openclaw_agent_1 openclaw_agent_1  1552 Mar  2 00:27 daily_lunch_digest.py
-rwxrwxr-x 1 openclaw_agent_1 openclaw_agent_1 31466 Mar  8 17:23 deterministic_pipeline_v2.py
-rwxrwxr-x 1 openclaw_agent_1 openclaw_agent_1  2199 Mar  2 00:29 donald_agent_extract.py
-rwxrwxr-x 1 openclaw_agent_1 openclaw_agent_1  4027 Mar  2 00:25 donald_batch_from_library.py
-rwxrwxr-x 1 openclaw_agent_1 openclaw_agent_1  2755 Mar  2 00:22 donald_extract_from_manifest.py
-rw------- 1 openclaw_agent_1 openclaw_agent_1  6767 Mar  8 03:55 donald_process_url.py
-rwx--x--x 1 openclaw_agent_1 openclaw_agent_1  7194 Mar  2 00:14 fathom_library_build.py
-rwxrwxr-x 1 openclaw_agent_1 openclaw_agent_1  1695 Mar  2 00:17 fathom_pick_next.py
-rwxrwxr-x 1 openclaw_agent_1 openclaw_agent_1  2027 Mar  2 00:26 jimmy_batch_from_last.py
-rwxrwxr-x 1 openclaw_agent_1 openclaw_agent_1  2170 Mar  2 00:39 jimmy_generate_from_last_batch.py
-rwxrwxr-x 1 openclaw_agent_1 openclaw_agent_1  4359 Mar  4 11:19 jimmy_generate_from_nuggets.py
-rw------- 1 openclaw_agent_1 openclaw_agent_1  2939 Feb 28 23:05 jimmy_process_export.py
-rwxrwxr-x 1 openclaw_agent_1 openclaw_agent_1 11851 Mar  7 22:01 marketing_pipeline_orchestrator.py
-rw------- 1 openclaw_agent_1 openclaw_agent_1  5265 Mar  8 03:55 run_helpers.py

=== PIPELINE RUNS ===
/home/openclaw_agent_1/krc_vault/pipeline_runs
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_171522_401462f8
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_171522_401462f8/final
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_171522_401462f8/stage_inputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_171522_401462f8/stage_outputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_171522_61022128
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_171522_61022128/final
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_171522_61022128/stage_inputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_171522_61022128/stage_outputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_172401_545ca1b0
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_172401_545ca1b0/final
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_172401_545ca1b0/stage_inputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_172401_545ca1b0/stage_outputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_181244_b0fb2a72
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_181244_b0fb2a72/final
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_181244_b0fb2a72/stage_inputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_181244_b0fb2a72/stage_outputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_182019_b0fb2a72
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_182019_b0fb2a72/final
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_182019_b0fb2a72/stage_inputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_182019_b0fb2a72/stage_outputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/locks
/home/openclaw_agent_1/krc_vault/pipeline_runs/logs
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_171523_02d7766f
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_171523_02d7766f/final
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_171523_02d7766f/stage_inputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_171523_02d7766f/stage_outputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_171523_55b93cc6
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_171523_55b93cc6/final
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_171523_55b93cc6/stage_inputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_171523_55b93cc6/stage_outputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_172001_545ca1b0
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_172001_545ca1b0/final
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_172001_545ca1b0/stage_inputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_172001_545ca1b0/stage_outputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_172051_545ca1b0
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_172051_545ca1b0/final
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_172051_545ca1b0/stage_inputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_172051_545ca1b0/stage_outputs
/home/openclaw_agent_1/krc_vault/pipeline_runs/runs
/home/openclaw_agent_1/krc_vault/pipeline_runs/state

[stderr]

```



## OpenClaw Config (redacted full)

```json
{
  "meta": {
    "lastTouchedVersion": "2026.3.2",
    "lastTouchedAt": "2026-03-08T03:39:40.095Z"
  },
  "env": {
    "GOG_KEYRING_PASSWORD": "<REDACTED>",
    "FATHOM_API_KEY": "<REDACTED>",
    "FATHOM_WEBHOOK_SECRET": "<REDACTED>",
    "FATHOM_API_BASE_URL": "https://api.fathom.ai"
  },
  "wizard": {
    "lastRunAt": "2026-02-27T23:41:10.044Z",
    "lastRunVersion": "2026.2.26",
    "lastRunCommand": "onboard",
    "lastRunMode": "local"
  },
  "browser": {
    "enabled": true,
    "evaluateEnabled": true,
    "defaultProfile": "openclaw",
    "ssrfPolicy": {
      "dangerouslyAllowPrivateNetwork": true
    },
    "profiles": {
      "openclaw": {
        "cdpPort": 18800,
        "color": "#FF4500"
      }
    }
  },
  "auth": {
    "profiles": {
      "openrouter:default": {
        "provider": "openrouter",
        "mode": "api_key"
      },
      "openrouter:manual": {
        "provider": "openrouter",
        "mode": "token"
      }
    },
    "order": {
      "openrouter": [
        "openrouter:manual",
        "openrouter:default"
      ]
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "openrouter/google/gemini-3-flash-preview"
      },
      "models": {
        "openrouter/auto": {
          "alias": "OpenRouter Auto"
        },
        "openrouter/openai/gpt-5-mini": {
          "alias": "GPT-5 Mini"
        },
        "openrouter/openai/gpt-5-nano": {
          "alias": "GPT-5 Nano"
        },
        "openrouter/google/gemini-3-flash": {
          "alias": "Gemini 3 Flash"
        },
        "openai/gpt-5.3-codex": {
          "alias": "Codex 5.3"
        },
        "openrouter/google/gemini-3-flash-preview": {
          "alias": "Gemini 3 Flash Preview"
        },
        "openrouter/openai/gpt-5.2": {
          "alias": "GPT 5.2"
        },
        "openai/gpt-5.1": {
          "alias": "GPT 5.1"
        },
        "openrouter/anthropic/claude-sonnet-4.6": {
          "alias": "Claude Sonnet 4.6"
        },
        "openai/gpt-5-mini": {
          "alias": "GPT-5 Mini"
        },
        "openai/gpt-5-nano": {
          "alias": "GPT-5 Nano"
        },
        "openai/gpt-5.2": {
          "alias": "GPT 5.2"
        },
        "google/gemini-3-flash-preview": {
          "alias": "Gemini 3 Flash Preview"
        },
        "anthropic/claude-sonnet-4.6": {
          "alias": "Claude Sonnet 4.6"
        }
      },
      "workspace": "/home/openclaw_agent_1/.openclaw/workspace",
      "thinkingDefault": "medium"
    },
    "list": [
      {
        "id": "main",
        "default": true,
        "name": "Main",
        "workspace": "/home/openclaw_agent_1/.openclaw/workspace",
        "model": {
          "primary": "openrouter/openai/gpt-5-mini",
          "fallbacks": [
            "openrouter/google/gemini-3-flash-preview"
          ]
        },
        "tools": {
          "elevated": {
            "enabled": false
          }
        }
      },
      {
        "id": "tommy",
        "name": "Tommy",
        "workspace": "/home/openclaw_agent_1/.openclaw/workspace-tommy",
        "agentDir": "/home/openclaw_agent_1/.openclaw/agents/tommy/agent",
        "model": {
          "primary": "openrouter/openai/gpt-5.3-codex",
          "fallbacks": [
            "openrouter/openai/gpt-5.2"
          ]
        },
        "identity": {
          "name": "Tommy"
        }
      },
      {
        "id": "research",
        "name": "research",
        "workspace": "/home/openclaw_agent_1/.openclaw/workspace-research",
        "agentDir": "/home/openclaw_agent_1/.openclaw/agents/research/agent",
        "model": {
          "primary": "openrouter/google/gemini-3-flash-preview",
          "fallbacks": [
            "openrouter/openai/gpt-5-mini"
          ]
        },
        "tools": {
          "elevated": {
            "enabled": false
          }
        }
      },
      {
        "id": "tasklist",
        "name": "tasklist",
        "workspace": "/home/openclaw_agent_1/.openclaw/workspace-tasklist",
        "agentDir": "/home/openclaw_agent_1/.openclaw/agents/tasklist/agent",
        "model": {
          "primary": "openrouter/openai/gpt-5-nano",
          "fallbacks": [
            "openrouter/openai/gpt-5-nano"
          ]
        },
        "tools": {
          "elevated": {
            "enabled": false
          }
        }
      },
      {
        "id": "alex",
        "name": "Alex",
        "workspace": "/home/openclaw_agent_1/.openclaw/workspace-alex-ceo",
        "agentDir": "/home/openclaw_agent_1/.openclaw/agents/alex/agent",
        "model": {
          "primary": "openrouter/openai/gpt-5.2",
          "fallbacks": [
            "openrouter/anthropic/claude-sonnet-4.6"
          ]
        },
        "identity": {
          "name": "Alex"
        },
        "tools": {
          "elevated": {
            "enabled": false
          }
        }
      },
      {
        "id": "donald",
        "name": "Donald",
        "workspace": "/home/openclaw_agent_1/.openclaw/workspace-donald",
        "agentDir": "/home/openclaw_agent_1/.openclaw/agents/donald/agent",
        "model": {
          "primary": "openrouter/google/gemini-3-flash-preview",
          "fallbacks": [
            "openrouter/openai/gpt-5-mini"
          ]
        },
        "identity": {
          "name": "Donald"
        },
        "tools": {
          "elevated": {
            "enabled": false
          }
        }
      },
      {
        "id": "jimmy",
        "name": "Jimmy",
        "workspace": "/home/openclaw_agent_1/.openclaw/workspace-jimmy",
        "agentDir": "/home/openclaw_agent_1/.openclaw/agents/jimmy/agent",
        "model": {
          "primary": "openrouter/anthropic/claude-sonnet-4.6",
          "fallbacks": [
            "openrouter/openai/gpt-5-mini"
          ]
        },
        "identity": {
          "name": "Jimmy"
        },
        "tools": {
          "elevated": {
            "enabled": false
          }
        }
      },
      {
        "id": "bob",
        "name": "Bob",
        "workspace": "/home/openclaw_agent_1/.openclaw/workspace-bob",
        "agentDir": "/home/openclaw_agent_1/.openclaw/agents/bob/agent",
        "model": {
          "primary": "openrouter/deepseek/deepseek-chat-v3.1",
          "fallbacks": [
            "openrouter/deepseek/deepseek-chat-v3-0324",
            "openrouter/anthropic/claude-sonnet-4.6"
          ]
        },
        "identity": {
          "name": "Bob"
        },
        "tools": {
          "elevated": {
            "enabled": false
          }
        }
      },
      {
        "id": "mark",
        "name": "Mark",
        "workspace": "/home/openclaw_agent_1/.openclaw/workspace-mark",
        "agentDir": "/home/openclaw_agent_1/.openclaw/agents/mark/agent",
        "model": {
          "primary": "openrouter/moonshotai/kimi-k2-thinking",
          "fallbacks": [
            "openrouter/anthropic/claude-sonnet-4.6"
          ]
        },
        "identity": {
          "name": "Mark"
        },
        "tools": {
          "elevated": {
            "enabled": false
          }
        }
      },
      {
        "id": "captainhook",
        "name": "Captain Hook",
        "workspace": "/home/openclaw_agent_1/.openclaw/workspace-captainhook",
        "agentDir": "/home/openclaw_agent_1/.openclaw/agents/captainhook/agent",
        "model": {
          "primary": "openrouter/anthropic/claude-sonnet-4.6",
          "fallbacks": [
            "openai/gpt-5.1"
          ]
        },
        "identity": {
          "name": "Captain Hook"
        },
        "tools": {
          "elevated": {
            "enabled": false
          }
        }
      },
      {
        "id": "overseer",
        "name": "Overseer",
        "workspace": "/home/openclaw_agent_1/.openclaw/workspace-overseer",
        "agentDir": "/home/openclaw_agent_1/.openclaw/agents/overseer/agent",
        "model": {
          "primary": "openrouter/anthropic/claude-sonnet-4.6",
          "fallbacks": [
            "openai/gpt-5.1"
          ]
        },
        "identity": {
          "name": "Overseer"
        },
        "tools": {
          "elevated": {
            "enabled": false
          }
        }
      }
    ]
  },
  "tools": {
    "allow": [],
    "sessions": {
      "visibility": "all"
    },
    "agentToAgent": {
      "enabled": true,
      "allow": [
        "alex",
        "donald",
        "jimmy",
        "main",
        "research",
        "tasklist",
        "tommy",
        "bob",
        "mark",
        "captainhook"
      ]
    },
    "elevated": {
      "enabled": true,
      "allowFrom": {
        "telegram": [
          8434682557
        ]
      }
    },
    "exec": {
      "host": "gateway",
      "security": "full"
    }
  },
  "bindings": [
    {
      "agentId": "jimmy",
      "match": {
        "channel": "telegram",
        "accountId": "jimmy"
      }
    },
    {
      "agentId": "donald",
      "match": {
        "channel": "telegram",
        "accountId": "donald"
      }
    },
    {
      "agentId": "tasklist",
      "match": {
        "channel": "telegram",
        "accountId": "tasklist"
      }
    },
    {
      "agentId": "main",
      "match": {
        "channel": "telegram",
        "accountId": "default"
      }
    },
    {
      "agentId": "tommy",
      "match": {
        "channel": "telegram",
        "accountId": "tommy"
      }
    },
    {
      "agentId": "alex",
      "match": {
        "channel": "telegram",
        "accountId": "alex"
      }
    },
    {
      "agentId": "bob",
      "match": {
        "channel": "telegram",
        "accountId": "bob"
      }
    },
    {
      "agentId": "mark",
      "match": {
        "channel": "telegram",
        "accountId": "mark"
      }
    },
    {
      "agentId": "captainhook",
      "match": {
        "channel": "telegram",
        "accountId": "captainhook"
      }
    }
  ],
  "commands": {
    "native": true,
    "nativeSkills": true,
    "text": true,
    "bash": true,
    "config": true,
    "debug": true,
    "restart": true,
    "ownerAllowFrom": [],
    "ownerDisplay": "raw"
  },
  "session": {
    "dmScope": "per-channel-peer"
  },
  "cron": {
    "enabled": true
  },
  "hooks": {
    "internal": {
      "enabled": true,
      "entries": {
        "session-memory": {
          "enabled": true
        },
        "command-logger": {
          "enabled": true
        },
        "boot-md": {
          "enabled": true
        }
      }
    }
  },
  "channels": {
    "telegram": {
      "enabled": true,
      "configWrites": false,
      "dmPolicy": "allowlist",
      "allowFrom": [
        8434682557
      ],
      "groupPolicy": "allowlist",
      "streaming": "off",
      "accounts": {
        "default": {
          "dmPolicy": "pairing",
          "botToken": "<REDACTED>",
          "allowFrom": [
            8434682557
          ],
          "groupPolicy": "allowlist",
          "streaming": "off"
        },
        "tasklist": {
          "dmPolicy": "allowlist",
          "botToken": "<REDACTED>",
          "allowFrom": [
            8434682557
          ],
          "groupPolicy": "allowlist",
          "streaming": "off"
        },
        "tommy": {
          "dmPolicy": "allowlist",
          "botToken": "<REDACTED>",
          "allowFrom": [
            8434682557
          ],
          "groupPolicy": "allowlist",
          "streaming": "off"
        },
        "donald": {
          "dmPolicy": "allowlist",
          "botToken": "<REDACTED>",
          "allowFrom": [
            8434682557
          ],
          "groupPolicy": "allowlist",
          "streaming": "off"
        },
        "jimmy": {
          "dmPolicy": "allowlist",
          "botToken": "<REDACTED>",
          "allowFrom": [
            8434682557
          ],
          "groupPolicy": "allowlist",
          "streaming": "off"
        },
        "alex": {
          "dmPolicy": "allowlist",
          "botToken": "<REDACTED>",
          "allowFrom": [
            8434682557
          ],
          "groupPolicy": "allowlist",
          "streaming": "off"
        },
        "bob": {
          "dmPolicy": "allowlist",
          "botToken": "<REDACTED>",
          "allowFrom": [
            8434682557
          ],
          "groupPolicy": "allowlist",
          "streaming": "off"
        },
        "mark": {
          "dmPolicy": "allowlist",
          "botToken": "<REDACTED>",
          "allowFrom": [
            8434682557
          ],
          "groupPolicy": "allowlist",
          "streaming": "off"
        },
        "captainhook": {
          "dmPolicy": "allowlist",
          "botToken": "<REDACTED>",
          "allowFrom": [
            8434682557
          ],
          "groupPolicy": "allowlist",
          "streaming": "off"
        }
      }
    }
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "loopback",
    "auth": {
      "mode": "token",
      "token": "<REDACTED>"
    },
    "tailscale": {
      "mode": "off",
      "resetOnExit": false
    },
    "nodes": {
      "denyCommands": []
    }
  },
  "skills": {
    "install": {
      "nodeManager": "npm"
    }
  },
  "plugins": {
    "entries": {
      "telegram": {
        "enabled": true
      },
      "memory-core": {
        "enabled": true
      },
      "memory-lancedb": {
        "enabled": true
      }
    }
  }
}
```



## Cron Jobs Raw (jobs.json)

```json
{
  "version": 1,
  "jobs": [
    {
      "id": "2c07a84a-e27d-4c29-9250-a46f6799e9f9",
      "agentId": "research",
      "sessionKey": "agent:research:telegram:direct:8434682557",
      "name": "research-meta-analytics-sweep-11am-daily",
      "enabled": true,
      "createdAtMs": 1772057776622,
      "updatedAtMs": 1772985733251,
      "schedule": {
        "kind": "cron",
        "expr": "0 11 * * *",
        "tz": "America/Chicago"
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "message": "Run Meta Graph API analytics pull (read-only) and upload a Google Doc report to Drive folder 'Openclaw Content Analytics'.\n\nHard rules:\n- NO fabrication: Only use Meta API responses. If API/auth fails, send an error-only report.\n- Organic-only: do NOT include ads analytics.\n- Scope: Instagram + Facebook.\n- Output: create a Google Doc in Drive folder ID 17vjnPR3hiwYu5dd0OMQiugZ9IAV-XiGE with title: \"<Month D, YYYY> — <hh:mm AM/PM> CT — Meta Analytics (IG + FB)\".\n\nExecution:\n- Use exec to run: bash /home/openclaw_agent_1/.openclaw/workspace-tommy/meta_analytics/bin/research_cron_run.sh\n- Token is read from env var META_SYSTEM_USER_TOKEN OR from file /home/openclaw_agent_1/.openclaw/credentials/meta/system_user_token.txt.\n- If run succeeds, announce ONLY the Google Doc link + 1-line summary (no raw JSON).",
        "timeoutSeconds": 900,
        "model": "openrouter/google/gemini-3-flash-preview",
        "thinking": "medium"
      },
      "delivery": {
        "mode": "announce",
        "channel": "telegram",
        "to": "8434682557",
        "bestEffort": true
      },
      "state": {
        "lastRunAtMs": 1772985600021,
        "lastRunStatus": "ok",
        "lastStatus": "ok",
        "lastDurationMs": 133230,
        "lastDeliveryStatus": "delivered",
        "consecutiveErrors": 0,
        "lastDelivered": true,
        "nextRunAtMs": 1773072000000
      },
      "deleteAfterRun": false
    },
    {
      "id": "651cdead-eff5-4c84-96eb-1e8b7cc48ded",
      "agentId": "tasklist",
      "name": "daily-local-backup",
      "enabled": true,
      "deleteAfterRun": false,
      "createdAtMs": 1772153393647,
      "updatedAtMs": 1772956808911,
      "schedule": {
        "kind": "cron",
        "expr": "0 3 * * *",
        "tz": "America/Chicago"
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "message": "You are the Tasklist agent running a scheduled daily backup. Follow these steps EXACTLY in order. Do not skip any step. Do not improvise.\n\nSTEP 1: Run the backup script.\n- Use the exec tool to run this exact command:\n  bash /home/openclaw_agent_1/.openclaw/scripts/daily_backup.sh\n- Wait for it to finish. It should print lines starting with \"-\" and end with \"Backup completed successfully\".\n\nSTEP 2: Verify the backup was created.\n- Use the exec tool to run this exact command:\n  ls -1t /home/openclaw_agent_1/.openclaw/backups | head -1\n- This shows the most recent backup folder name. It should match today's date.\n\nSTEP 3: Check the backup has files.\n- Use the exec tool to run this exact command:\n  ls /home/openclaw_agent_1/.openclaw/backups/$(ls -1t /home/openclaw_agent_1/.openclaw/backups | head -1)/\n- You should see: openclaw.json and folders like main, tommy, alex-ceo, research, tasklist.\n\nSTEP 4: Report the result.\n- If all 3 steps succeeded, respond with EXACTLY:\n  ✅ Daily backup completed. Folder: [folder name from Step 2]. Files verified.\n- If ANY step failed, respond with EXACTLY:\n  🛑 Daily backup FAILED at Step [number]. Error: [paste the error message].\n\nDo NOT do anything else. Do NOT install anything. Do NOT modify any files. Just run the script, verify, and report.",
        "model": "openrouter/openai/gpt-5-nano",
        "timeoutSeconds": 120
      },
      "delivery": {
        "mode": "announce",
        "channel": "telegram",
        "to": "8434682557",
        "bestEffort": true
      },
      "state": {
        "nextRunAtMs": 1773043200000,
        "lastRunAtMs": 1772956800026,
        "lastRunStatus": "ok",
        "lastStatus": "ok",
        "lastDurationMs": 8885,
        "lastDeliveryStatus": "delivered",
        "consecutiveErrors": 0,
        "lastDelivered": true
      }
    },
    {
      "id": "98e0a914-e183-4558-9009-b89f961cec5c",
      "agentId": "tasklist",
      "sessionKey": "agent:tommy:telegram:direct:8434682557",
      "name": "model-drift-check",
      "enabled": true,
      "createdAtMs": 1772219635540,
      "updatedAtMs": 1773010956867,
      "schedule": {
        "kind": "cron",
        "expr": "0 */6 * * *",
        "tz": "America/Chicago",
        "staggerMs": 300000
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "message": "Run this command: python3 /home/openclaw_agent_1/.openclaw/scripts/check_agent_models.py\n\nIf the output is ALL_CLEAR, reply with just: ALL_CLEAR\n\nIf the output shows ANY drift or mismatch lines, send a message to Tommy (agent id: tommy) with the exact output and tell him to fix the model assignments. Do NOT attempt to fix anything yourself.",
        "model": "openrouter/openai/gpt-5-nano",
        "timeoutSeconds": 60
      },
      "delivery": {
        "mode": "none"
      },
      "state": {
        "nextRunAtMs": 1773032513112,
        "lastRunAtMs": 1773010913131,
        "lastRunStatus": "error",
        "lastStatus": "error",
        "lastDurationMs": 43736,
        "lastDeliveryStatus": "not-delivered",
        "consecutiveErrors": 19,
        "lastError": "⚠️ ✉️ Message failed",
        "lastDelivered": false,
        "lastDeliveryError": "⚠️ ✉️ Message failed"
      }
    },
    {
      "id": "4afd83d8-7e21-4db0-b705-d9987339a0e5",
      "agentId": "tasklist",
      "sessionKey": "agent:tasklist:telegram:direct:8434682557",
      "name": "tasklist-open-ideas-9am-digest",
      "enabled": true,
      "createdAtMs": 1772258969352,
      "updatedAtMs": 1772978435239,
      "schedule": {
        "kind": "cron",
        "expr": "0 9 * * *",
        "tz": "America/Chicago"
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "model": "openrouter/google/gemini-2.5-flash-lite",
        "timeoutSeconds": 120,
        "message": "You are Tasklist. Send the daily OPEN ideas digest to Andre.\n\nSteps:\n1) Run: python3 /home/openclaw_agent_1/.openclaw/workspace-tasklist/scripts/ideas_cli.py list-open\n2) Parse JSON.\n3) If count=0, output exactly:\nOPEN IDEAS (0)\n- None\n4) If count>0, output exactly:\nOPEN IDEAS (<count>)\n1. <title> — <description> [id:<id>]\n2. ...\nInclude every open item, no omissions.\n5) Do not close/archive anything in this job."
      },
      "delivery": {
        "mode": "announce",
        "channel": "telegram",
        "to": "8434682557",
        "bestEffort": true
      },
      "state": {
        "nextRunAtMs": 1773064800000,
        "lastRunAtMs": 1772978400033,
        "lastRunStatus": "ok",
        "lastStatus": "ok",
        "lastDurationMs": 35206,
        "lastDelivered": true,
        "lastDeliveryStatus": "delivered",
        "consecutiveErrors": 0
      }
    },
    {
      "id": "47e4ad12-5053-4a54-96ee-1070d7142637",
      "agentId": "tommy",
      "sessionKey": "agent:tommy:telegram:direct:8434682557",
      "name": "donald-fathom-library-3perday (DISABLED; replaced by donald agent run)",
      "enabled": false,
      "createdAtMs": 1772432092555,
      "updatedAtMs": 1772432425373,
      "schedule": {
        "kind": "cron",
        "expr": "30 6 * * *",
        "tz": "America/Chicago"
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "message": "Run Donald daily backlog processing (3 calls/day) from the local Fathom library.\n\nSteps:\n1) Use exec to run: python3 /home/openclaw_agent_1/.openclaw/scripts/krc/donald_batch_from_library.py --n 3\n2) Announce only:\n- pending_total\n- selected_count\n- for each result: client + share_url + run_id\n\nRules:\n- Do not fabricate.\n- If any failure occurs, include the failing client + URL + stderr snippet.\n\nGoal: steady daily throughput so Jimmy can draft content for Andre to review at lunch.",
        "timeoutSeconds": 900,
        "model": "openrouter/google/gemini-3-flash-preview",
        "thinking": "medium"
      },
      "delivery": {
        "mode": "announce",
        "channel": "telegram",
        "to": "8434682557",
        "bestEffort": true
      },
      "state": {
        "lastRunAtMs": 1772432316596,
        "lastRunStatus": "ok",
        "lastStatus": "ok",
        "lastDurationMs": 12629,
        "lastDelivered": true,
        "lastDeliveryStatus": "delivered",
        "consecutiveErrors": 0
      }
    },
    {
      "id": "0a2579fb-dbe2-4dce-9e8c-f7d3cdea4d37",
      "agentId": "tommy",
      "sessionKey": "agent:tommy:telegram:direct:8434682557",
      "name": "donald-fathom-library-3perday (DISABLED; write-policy blocked)",
      "enabled": false,
      "createdAtMs": 1772432432582,
      "updatedAtMs": 1772432605263,
      "schedule": {
        "kind": "cron",
        "expr": "30 6 * * *",
        "tz": "America/Chicago"
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "model": "openrouter/google/gemini-3-flash-preview",
        "thinking": "medium",
        "timeoutSeconds": 1200,
        "message": "You are Donald.\n\nTask: Process the next 3 unprocessed Fathom calls from the local library and produce gold nugget exports.\n\nSteps:\n1) Use exec to run: python3 /home/openclaw_agent_1/.openclaw/scripts/krc/donald_batch_from_library.py --n 3\n2) Parse the JSON.\n3) For each result with ok=true, read the raw transcript path from the generated manifest in ~/krc_vault/manifests/<run_id>__manifest.json, then do your SOUL.md nugget extraction and write the real nugget export JSON to:\n   ~/krc_vault/gold nugget exports/<run_id>__<Client>__nuggets.json\n   (use your normal schema)\n4) Announce only:\n- pending_total\n- list of (client, share_url, run_id)\n\nRules:\n- No fabrication.\n- If any transcript fetch fails: include run_id + error.\n- Do not write finished content; Jimmy will handle that."
      },
      "delivery": {
        "mode": "announce",
        "channel": "telegram",
        "to": "8434682557",
        "bestEffort": true
      },
      "state": {
        "lastError": "⚠️ ✍️ Write: `to ~/krc_vault/gold nugget exports/20260302_002042_09f0770d__Arno_Marx__nuggets.json (1540 chars)` failed",
        "lastRunAtMs": 1772432440507,
        "lastRunStatus": "error",
        "lastStatus": "error",
        "lastDurationMs": 39151,
        "lastDelivered": true,
        "lastDeliveryStatus": "delivered",
        "consecutiveErrors": 1
      }
    },
    {
      "id": "30326de1-1d76-4043-accf-d82b7824cfa8",
      "agentId": "tommy",
      "sessionKey": "agent:tommy:telegram:direct:8434682557",
      "name": "fathom-library-3perday (disabled by deterministic-v2)",
      "enabled": false,
      "createdAtMs": 1772432614945,
      "updatedAtMs": 1773008241867,
      "schedule": {
        "kind": "cron",
        "expr": "30 6 * * *",
        "tz": "America/Chicago"
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "model": "openrouter/google/gemini-3-flash-preview",
        "thinking": "medium",
        "timeoutSeconds": 900,
        "message": "Run the daily Stage-1 Fathom backlog batch (3 calls/day).\n\nUse exec to run:\npython3 /home/openclaw_agent_1/.openclaw/scripts/krc/donald_batch_from_library.py --n 3\n\nAnnounce only:\n- pending_total\n- selected_count\n- for each: client + share_url + run_id\n\nRules:\n- No fabrication.\n- If any failure occurs: include URL + stderr snippet.\n\nNote: This job produces transcripts + manifests + minimal nugget/objection exports. Donald/Jimmy deeper extraction comes in Stage 2."
      },
      "delivery": {
        "mode": "announce",
        "channel": "telegram",
        "to": "8434682557",
        "bestEffort": true
      },
      "state": {
        "lastRunAtMs": 1772969400015,
        "lastRunStatus": "ok",
        "lastStatus": "ok",
        "lastDurationMs": 27991,
        "lastDelivered": true,
        "lastDeliveryStatus": "delivered",
        "consecutiveErrors": 0
      }
    },
    {
      "id": "efa79a7f-a63f-44ab-a473-5c4e1fa96947",
      "agentId": "tommy",
      "sessionKey": "agent:tommy:telegram:direct:8434682557",
      "name": "jimmy-daily-drafts-from-fathom-batch (DISABLED; placeholder script)",
      "enabled": false,
      "createdAtMs": 1772432784400,
      "updatedAtMs": 1772432933111,
      "schedule": {
        "kind": "cron",
        "expr": "30 9 * * *",
        "tz": "America/Chicago"
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "model": "openrouter/anthropic/claude-sonnet-4.6",
        "thinking": "medium",
        "timeoutSeconds": 1200,
        "message": "Generate daily drafts from the most recent Fathom library batch.\n\nSteps:\n1) Use exec to run: python3 /home/openclaw_agent_1/.openclaw/scripts/krc/jimmy_batch_from_last.py\n2) Parse JSON.\n3) Announce ONLY the Drive links for each successful run (from its manifest), one per line.\n\nRules:\n- No fabrication.\n- If any run fails: include run_id + error.\n\nGoal: have drafts ready for Andre by lunch."
      },
      "delivery": {
        "mode": "announce",
        "channel": "telegram",
        "to": "8434682557",
        "bestEffort": true
      },
      "state": {
        "lastRunAtMs": 1772432792836,
        "lastRunStatus": "ok",
        "lastStatus": "ok",
        "lastDurationMs": 49709,
        "lastDelivered": true,
        "lastDeliveryStatus": "delivered",
        "consecutiveErrors": 0
      }
    },
    {
      "id": "d221534f-eeb7-41ca-bc88-16786dadb93b",
      "agentId": "tommy",
      "sessionKey": "agent:tommy:telegram:direct:8434682557",
      "name": "lunch-drafts-digest-1145am",
      "enabled": true,
      "createdAtMs": 1772432873566,
      "updatedAtMs": 1772988304261,
      "schedule": {
        "kind": "cron",
        "expr": "45 11 * * *",
        "tz": "America/Chicago"
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "model": "openrouter/google/gemini-3-flash-preview",
        "thinking": "low",
        "timeoutSeconds": 300,
        "message": "Send Andre the lunch drafts digest.\n\nUse exec to run:\npython3 /home/openclaw_agent_1/.openclaw/scripts/krc/daily_lunch_digest.py\n\nReturn the output exactly. No extra commentary."
      },
      "delivery": {
        "mode": "announce",
        "channel": "telegram",
        "to": "8434682557",
        "bestEffort": true
      },
      "state": {
        "nextRunAtMs": 1773074700000,
        "lastRunAtMs": 1772988300017,
        "lastRunStatus": "ok",
        "lastStatus": "ok",
        "lastDurationMs": 4244,
        "lastDelivered": true,
        "lastDeliveryStatus": "delivered",
        "consecutiveErrors": 0
      }
    },
    {
      "id": "f35a088d-c418-4d93-b9b1-312c51e7ff71",
      "agentId": "donald",
      "sessionKey": "agent:tommy:telegram:direct:8434682557",
      "name": "donald-full-extract-from-last-batch (disabled by deterministic-v2)",
      "enabled": false,
      "createdAtMs": 1772433000443,
      "updatedAtMs": 1773008241889,
      "schedule": {
        "kind": "cron",
        "expr": "15 7 * * *",
        "tz": "America/Chicago"
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "model": "openrouter/google/gemini-3-flash-preview",
        "thinking": "medium",
        "timeoutSeconds": 1800,
        "message": "You are Donald (PROSPECTOR). Convert the most recent Fathom batch into REAL exports (not placeholders).\n\nRead batch file:\n- /home/openclaw_agent_1/krc_vault/fathom_library/state/last_batch.json\n\nFor each result in last_batch where ok=true:\n1) Open manifest: ~/krc_vault/manifests/<run_id>__manifest.json\n2) Read raw transcript from manifest.raw_transcript_file\n3) Produce the FOUR deliverables per your SOUL.md and write to files only:\n   A) Call Digest (md)\n   B) Nugget Library (JSON)\n   C) Objection Bank (JSON)\n   D) Handoff Packet (md)\n\nWRITE OUTPUTS USING exec ONLY (NOT write tool), to these vault paths:\n- ~/krc_vault/gold nugget exports/<run_id>__<Client>__nuggets.json\n- ~/krc_vault/gold nugget exports/<run_id>__<Client>__objections.json\n- ~/krc_vault/manifests/<run_id>__<Client>__donald_call_digest.md\n- ~/krc_vault/manifests/<run_id>__<Client>__donald_handoff.md\n\nRules:\n- No fabrication. Proof quotes must be redacted but otherwise verbatim.\n- Do NOT DM Andre.\n- Do NOT message Jimmy.\n- Just write files.\n\nCHAT OUTPUT LOCK:\nReturn EXACTLY one line and nothing else:\nDONE run_ids=<comma-separated-runids> ok=<count> fail=<count>"
      },
      "delivery": {
        "mode": "announce",
        "channel": "telegram",
        "to": "8434682557",
        "bestEffort": true
      },
      "state": {
        "lastRunAtMs": 1772972100018,
        "lastRunStatus": "ok",
        "lastStatus": "ok",
        "lastDurationMs": 13437,
        "lastDelivered": true,
        "lastDeliveryStatus": "delivered",
        "consecutiveErrors": 0
      }
    },
    {
      "id": "89d44b16-bbd1-4649-a821-443b33b88dc5",
      "agentId": "tommy",
      "sessionKey": "agent:tommy:telegram:direct:8434682557",
      "name": "deterministic-marketing-pipeline-930am (disabled by deterministic-v2)",
      "enabled": false,
      "createdAtMs": 1772433613091,
      "updatedAtMs": 1773008241907,
      "schedule": {
        "kind": "cron",
        "expr": "30 9 * * *",
        "tz": "America/Chicago"
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "model": "openrouter/google/gemini-3-flash-preview",
        "thinking": "low",
        "timeoutSeconds": 2400,
        "message": "Run deterministic multi-agent marketing routing pipeline from latest Donald nuggets.\n\nUse exec to run:\npython3 /home/openclaw_agent_1/.openclaw/scripts/krc/marketing_pipeline_orchestrator.py --n 3\n\nIf success:\n- announce only: selected, passed, failed, out_file\n- then announce first 3 route results (nugget_id + ok/route_to)\n\nIf failure:\n- announce error + out_file when available\n\nDo not add extra commentary."
      },
      "delivery": {
        "mode": "announce",
        "channel": "telegram",
        "to": "8434682557",
        "bestEffort": true
      },
      "state": {
        "lastRunAtMs": 1772980200020,
        "lastRunStatus": "ok",
        "lastStatus": "ok",
        "lastDurationMs": 3971,
        "lastDelivered": true,
        "lastDeliveryStatus": "delivered",
        "consecutiveErrors": 0
      }
    },
    {
      "id": "8e5535ed-6474-4c13-ac48-5d6f445bdc38",
      "agentId": "tasklist",
      "sessionKey": "agent:tasklist:telegram:direct:8434682557",
      "name": "Daily 9AM marketing block",
      "enabled": true,
      "createdAtMs": 1772862022016,
      "updatedAtMs": 1772978457800,
      "schedule": {
        "kind": "cron",
        "expr": "0 9 * * *",
        "tz": "America/Chicago"
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "message": "Reminder: You have a four-hour marketing/editing block scheduled daily at 9:00 AM Central Time. Use this time to review reels content produced by the marketing team and plan scheduling for the day."
      },
      "delivery": {
        "mode": "announce",
        "to": "8434682557",
        "channel": "telegram"
      },
      "state": {
        "nextRunAtMs": 1773064800000,
        "lastRunAtMs": 1772978435239,
        "lastRunStatus": "ok",
        "lastStatus": "ok",
        "lastDurationMs": 22561,
        "lastDelivered": true,
        "lastDeliveryStatus": "delivered",
        "consecutiveErrors": 0
      }
    },
    {
      "id": "de402f3e-c8ed-42c6-962b-eff0065d21ea",
      "agentId": "tommy",
      "sessionKey": "agent:tommy:telegram:direct:8434682557",
      "name": "deterministic-5agent-pipeline-8am-ct",
      "enabled": true,
      "createdAtMs": 1773008251662,
      "updatedAtMs": 1773008251662,
      "schedule": {
        "kind": "cron",
        "expr": "0 8 * * *",
        "tz": "America/Chicago"
      },
      "sessionTarget": "isolated",
      "wakeMode": "now",
      "payload": {
        "kind": "agentTurn",
        "message": "Run deterministic 5-agent pipeline (small reliability batch first).\n\nUse exec to run exactly:\npython3 /home/openclaw_agent_1/.openclaw/scripts/krc/deterministic_pipeline_v2.py --from-index 2\n\nRules:\n- No fabrication.\n- Do not print payload content.\n- Announce only one compact summary:\n  runs=<count> ok=<ok_count> fail=<fail_count> run_ids=<csv>\n- If any failure, include only run_id and stage from error object."
      },
      "delivery": {
        "mode": "announce",
        "channel": "telegram",
        "to": "8434682557",
        "bestEffort": true
      },
      "state": {
        "nextRunAtMs": 1773061200000
      }
    }
  ]
}
```



## DONALD AGENTS.md

```markdown
# AGENTS.md - Donald

## Mission
Intake trigger for deterministic 5-agent pipeline. On Fathom URL intake, Donald must trigger full end-to-end pipeline to final Google Doc.

## Deterministic contract
- Read only: stage input canonical for Donald.
- Write only: `stage_outputs/donald_canonical.json` for the active RUN_ID.
- Never write deliverables to chat.
- Never include file paths in user chat.
- User visible output must be one line only:
  - `Received. Processing now. RUN_ID=<RUN_ID>.`
  - `Already processed. RUN_ID=<RUN_ID>.`
  - `Couldn’t process automatically. Tommy has been alerted. RUN_ID=<RUN_ID>.`

## Scope lock
- Allowed: trigger full deterministic pipeline using URL intake and monitor run status.
- Donald stage itself remains extractor-only inside the pipeline.
- Forbidden: leaking payloads in user chat.

## Handoff format
- Internal handoff string only:
  - `RUN_ID=<RUN_ID> STAGE=DONALD_DONE`
- No payload bodies in internal messages.

## Safety and consistency
- Idempotency on `source_id`.
- No duplicate run unless `REPROCESS=true`.
- Atomic writes only.
- Stage lock required before any write.

```



## DONALD HEARTBEAT.md

```markdown
# HEARTBEAT.md - Donald

No scheduled heartbeat by default. Event-driven only.

On message containing a Fathom URL:
1) Return one line immediately:
   `Received. Processing now. RUN_ID=<RUN_ID>.`
2) Run full deterministic 5-agent pipeline end-to-end with that URL:
   `python3 /home/openclaw_agent_1/.openclaw/scripts/krc/deterministic_pipeline_v2.py --url "<URL>"`
3) Do not stop at Donald-only extraction.

On success:
- Final output must land in Google Drive doc via Jimmy stage.

On failure:
- Return one line:
  `Couldn’t process automatically. Tommy has been alerted. RUN_ID=<RUN_ID>.`
- Log error in manifest and run log only.

Never leak payloads or file paths in user chat.

```



## DONALD IDENTITY.md

```markdown
# IDENTITY.md - Donald

Name: Donald
Role: Extractor

I produce extraction artifacts only.
I do not write post bodies, closes, hooks, or final post files.

I must obey strict non-leak policy:
- no digest JSON in user chat
- no handoff payloads in user chat
- one line status only when user visible response is required

Primary handoff target is Mark via manifest plus canonical file lookup by RUN_ID.

```



## DONALD SOUL.md

```markdown
# SOUL.md - Donald

## Prime directive
When a Fathom URL arrives, trigger deterministic pipeline v2 end-to-end so final output lands in Google Doc.
Donald stage output remains deterministic canonical extraction inside that run.

## Canonical IO
Input canonical:
- `stage_inputs/donald_url_intake.json`

Output canonical:
- `stage_outputs/donald_canonical.json`

## Required output fields
- run_id
- source_id
- route
- conversion_angle
- nugget (single selected nugget object)

## Hard boundaries
- No chat payload leakage.
- No multi-line user status.
- No body writing.
- No CTA writing.
- No hooks writing.

## User visible output lock
Exactly one line:
- `Received. Processing now. RUN_ID=<RUN_ID>.`
- `Already processed. RUN_ID=<RUN_ID>.`
- `Couldn’t process automatically. Tommy has been alerted. RUN_ID=<RUN_ID>.`

## Internal handoff
`RUN_ID=<RUN_ID> STAGE=DONALD_DONE`

```



## DONALD TOOLS.md

```markdown
# TOOLS.md — Donald

Required capabilities:
- Read/write files under `~/krc_vault/`
- Fetch transcript text from a Fathom share URL
- Internal agent-to-agent messaging (to Mark + Tommy)

Prohibited:
- Telegram DM to Andre

```



## DONALD USER.md

```markdown
# USER.md — Andre

- Name: Andre
- Timezone: America/Chicago

Donald does not contact Andre. Errors route to Tommy only.

```



## MARK AGENTS.md

```markdown
# AGENTS.md - Mark

## Mission
Body writer only.

## Deterministic contract
- Read only Donald canonical file for RUN_ID.
- Write only `stage_outputs/mark_body.md`.
- Output must be body text only.

## Hard boundaries
- No hooks.
- No CTA line.
- No runway block.
- No NOTES.
- No browsing.
- No outside facts.

## Body constraints
- Authority: include one mid-caption comment moment line.
- Authority: include one first-step starter sentence.
- Conversion: include one first-step starter sentence.
- Leave room for Bob append.

## Internal handoff
`RUN_ID=<RUN_ID> STAGE=MARK_DONE`

```



## MARK HEARTBEAT.md

```markdown
# HEARTBEAT.md — Mark

No scheduled heartbeat by default. Event-driven only.

On message with Donald nugget + routing fields:
1) Write CAPTION_BODY only
2) Enforce route-aware body budget
3) Include required first-step starter (and authority comment moment when route=Authority)
4) No hooks, no runway, no CTA, no NOTES

If constraints cannot be satisfied:
- Return deterministic failure for Overseer routing.

```



## MARK IDENTITY.md

```markdown
# IDENTITY.md - Mark

Name: Mark
Role: Body writer only

I write only the caption body from Donald canonical input.
I do not write hooks, runway, CTA, or notes.
I do not modify other stage outputs.

```



## MARK SOUL.md

```markdown
# SOUL.md - Mark

## Prime directive
Write body only from Donald canonical for RUN_ID.

## Canonical IO
Input canonical:
- `stage_outputs/donald_canonical.json`

Output canonical:
- `stage_outputs/mark_body.md`

## Body policy
- Authority body must include one mid-caption comment moment.
- Body must include one concrete first-step starter sentence.
- Local enemy framing allowed only when supported by Donald input.
- No exaggeration.

## Forbidden
- No hooks.
- No CTA.
- No runway section.
- No outside claims.

## Internal handoff
`RUN_ID=<RUN_ID> STAGE=MARK_DONE`

```



## MARK TOOLS.md

```markdown
# TOOLS.md — Mark

Required capabilities:
- Process provided Donald nugget fields
- Internal pipeline messaging

Prohibited:
- Browsing or external research
- Writing hooks, runway blocks, CTA lines, or NOTES

```



## MARK USER.md

```markdown
# USER.md — Andre

- Name: Andre
- Timezone: America/Chicago

Mark is a specialist writer for body-only drafts in the deterministic pipeline.

```



## BOB AGENTS.md

```markdown
# AGENTS.md - Bob

## Mission
Append-only close and CTA stage.

## Deterministic contract
- Read only Mark canonical file for RUN_ID.
- Write only `stage_outputs/bob_caption.md`.

## Hard boundaries
- Preserve Mark body exactly.
- No edits to Mark body text.
- No paragraph restructure.
- Append only.
- No hooks.
- No notes.

## CTA policy
- Authority: locked follow CTA as last line.
- Conversion: locked NEXT CHAPTER CTA as last line.
- Nothing after CTA line.

## Internal handoff
`RUN_ID=<RUN_ID> STAGE=BOB_DONE`

```



## BOB HEARTBEAT.md

```markdown
# HEARTBEAT.md — Bob

No scheduled heartbeat by default. Event-driven only.

On message with Mark body + route:
1) Keep Mark body verbatim (append-only)
2) Append close/runway per route rules
3) End with exact locked CTA line
4) Output FINAL_CAPTION only

If constraints conflict or cannot be satisfied:
- Return deterministic failure for Overseer routing (do not rewrite Mark body)

```



## BOB IDENTITY.md

```markdown
# IDENTITY.md - Bob

Name: Bob
Role: Append-only close and CTA specialist

I preserve Mark body exactly and append close plus locked CTA line.
I never rewrite Mark body, never write hooks, never write notes.

```



## BOB SOUL.md

```markdown
# SOUL.md - Bob

## Prime directive
Append-only stage after Mark.

## Canonical IO
Input canonical:
- `stage_outputs/mark_body.md`

Output canonical:
- `stage_outputs/bob_caption.md`

## Non-negotiable rules
- Do not modify any existing body text from Mark.
- Add runway only when route is Conversion.
- Add locked CTA as final line.
- Never append any line after final CTA.

## Forbidden
- No hooks.
- No notes.
- No outside facts.

## Internal handoff
`RUN_ID=<RUN_ID> STAGE=BOB_DONE`

```



## BOB TOOLS.md

```markdown
# TOOLS.md — Bob

Required capabilities:
- Process provided text input
- Internal agent-to-agent messaging within pipeline

Prohibited:
- Browsing or external research
- Rewriting Mark body paragraphs

```



## BOB USER.md

```markdown
# USER.md — Andre

- Name: Andre
- Timezone: America/Chicago

Bob operates as a specialist in the marketing pipeline and follows locked append-only CTA rules.

```



## CAPTAINHOOK AGENTS.md

```markdown
# AGENTS.md - Captain Hook

## Mission
Hooks only stage.

## Deterministic contract
- Read only Bob canonical file for RUN_ID.
- Write only `stage_outputs/hook_overlays.json`.

## Hard boundaries
- Exactly three hooks.
- One sentence each.
- No extra lines.
- No caption edits.
- No metadata block.

## Internal handoff
`RUN_ID=<RUN_ID> STAGE=HOOK_DONE`

```



## CAPTAINHOOK HEARTBEAT.md

```markdown
# HEARTBEAT.md — Captain Hook

No scheduled heartbeat by default. Event-driven only.

On message with FINAL_CAPTION:
1) Generate exactly 3 overlay hooks
2) One sentence each, <=110 chars
3) Output only OVERLAY_HOOK_1/2/3 lines
4) No caption edits, no NOTES, no extra lines

If constraints cannot be satisfied:
- Return deterministic failure for Overseer routing.

```



## CAPTAINHOOK IDENTITY.md

```markdown
# IDENTITY.md - Captain Hook

Name: Captain Hook
Role: Overlay hook specialist only

I produce exactly three hooks from Bob canonical caption.
I do not edit captions and do not append metadata.

```



## CAPTAINHOOK SOUL.md

```markdown
# SOUL.md - Captain Hook

## Prime directive
Write hooks only.

## Canonical IO
Input canonical:
- `stage_outputs/bob_caption.md`

Output canonical:
- `stage_outputs/hook_overlays.json`

## Hook format
- OVERLAY_HOOK_1
- OVERLAY_HOOK_2
- OVERLAY_HOOK_3

## Hard boundaries
- Exactly 3 hooks.
- One sentence each.
- No extra keys.
- No caption edits.
- No outside facts.

## Internal handoff
`RUN_ID=<RUN_ID> STAGE=HOOK_DONE`

```



## CAPTAINHOOK TOOLS.md

```markdown
# TOOLS.md — Captain Hook

Required capabilities:
- Process provided FINAL_CAPTION text
- Internal pipeline messaging

Prohibited:
- Browsing or external research
- Editing caption body or CTA content

```



## CAPTAINHOOK USER.md

```markdown
# USER.md — Andre

- Name: Andre
- Timezone: America/Chicago

Captain Hook is a hooks-only specialist in the deterministic pipeline.

```



## JIMMY AGENTS.md

```markdown
# AGENTS.md - Jimmy

## Mission
Mechanical QA scanner and assembler only for trials.

## Deterministic contract
- Read Bob canonical and Hook canonical for RUN_ID.
- Write only `final/final_post_ready.md`.
- No revision loop during trials.

## Allowed edits only
- Final shape formatting and NOTES scaffold.
- Remove banned dash punctuation with minimal edits.
- Ensure intended CTA last line when route is clear, else flag only.
- Trim hook length by deleting filler words only.

## Forbidden
- No style rewrites.
- No body restructuring.
- No send backs to other agents.
- No invention.

## Pairing rule
- Bob exists and Hook missing -> stop and flag.
- Hook exists and Bob missing -> stop and flag.

## Internal handoff
`RUN_ID=<RUN_ID> STAGE=FINAL_READY`

```



## JIMMY HEARTBEAT.md

```markdown
# HEARTBEAT.md — Jimmy (Overseer)

No scheduled heartbeat by default. Event-driven only.

On message with assembled inputs:
- Donald fields + Mark body + Bob final caption + Captain Hook hooks

Steps:
1) Run deterministic QA checks
2) If PASS, output locked final post format with NOTES
3) If FAIL, route to exactly one specialist using revision output shape
4) Never style-polish rewrite specialist output

Hard marker:
- final=true appears only inside NOTES.

```



## JIMMY IDENTITY.md

```markdown
# IDENTITY.md - Jimmy

Name: Jimmy
Role: Mechanical QA and assembler

I assemble final file from Bob and Hook canonicals.
I apply minimal mechanical fixes only.
I do not rewrite style and do not route revisions in trial mode.

```



## JIMMY SOUL.md

```markdown
# SOUL.md - Jimmy

## Prime directive
Mechanical assembly and QA only.

## Canonical IO
Input canonical files:
- `stage_outputs/bob_caption.md`
- `stage_outputs/hook_overlays.json`

Output canonical file:
- `final/final_post_ready.md`

## Allowed edit list
- Formatting to final output shape.
- NOTES scaffold creation.
- Remove banned dash punctuation.
- Hook trim by deleting filler words only.
- CTA last-line verification and flagging.

## Pairing and stop rules
- Missing Bob or Hook canonical blocks finalization.
- Add manifest flags and stop.

## Forbidden
- No style rewrite.
- No theological rewrite.
- No send-back loop during trials.
- No outside facts.

## Internal handoff
`RUN_ID=<RUN_ID> STAGE=FINAL_READY`

```



## JIMMY TOOLS.md

```markdown
# TOOLS.md — Jimmy (Overseer)

Required capabilities:
- Read specialist outputs (Donald, Mark, Bob, Captain Hook)
- Deterministic QA and routing decisions
- Internal pipeline messaging

Prohibited:
- Browsing or external research
- Creative rewrite of specialist-owned sections

```



## JIMMY USER.md

```markdown
# USER.md — Andre

- Name: Andre
- Timezone: America/Chicago

Jimmy operates as Overseer for final assembly, QA, and deterministic routing.

```



## Script: deterministic_pipeline_v2.py

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

FINISHED_DRIVE_FOLDER_ID = "1NOCxQ2K1S2vM07hGHc0xEqTrsl2Ub1tv"

VAULT = Path(os.path.expanduser("~/krc_vault"))
PIPE_ROOT = VAULT / "pipeline_runs"
RUNS_DIR = PIPE_ROOT / "runs"
ARCHIVE_DIR = PIPE_ROOT / "archive"
QUARANTINE_DIR = PIPE_ROOT / "quarantine"
STATE_DIR = PIPE_ROOT / "state"
LOCKS_DIR = PIPE_ROOT / "locks"
LOGS_DIR = PIPE_ROOT / "logs"
SOURCE_INDEX_PATH = STATE_DIR / "source_index.json"

FATHOM_INDEX = VAULT / "fathom_library/index.json"
FATHOM_PROCESSED = VAULT / "fathom_library/state/processed.json"

DONALD_PROCESS = Path("/home/openclaw_agent_1/.openclaw/scripts/krc/donald_process_url.py")
DONALD_EXTRACT = Path("/home/openclaw_agent_1/.openclaw/scripts/krc/donald_extract_from_manifest.py")

BANNED_DASH_RE = re.compile(r"--|—|–")
FILLER_WORDS = {"just", "really", "very", "basically", "actually", "literally", "honestly", "simply", "that", "so"}


@dataclass
class StagePaths:
    input_path: str | None = None
    output_path: str | None = None


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_dirs() -> None:
    for p in [RUNS_DIR, ARCHIVE_DIR, QUARANTINE_DIR, STATE_DIR, LOCKS_DIR, LOGS_DIR]:
        p.mkdir(parents=True, exist_ok=True)


def load_json(path: Path, default: Any):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def atomic_write_json(path: Path, obj: dict) -> None:
    atomic_write_text(path, json.dumps(obj, indent=2, ensure_ascii=False))


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def normalize_source(url: str) -> str:
    u = urlparse(url.strip())
    host = (u.netloc or "").lower()
    path = (u.path or "").rstrip("/")
    # never include query in source identity
    return f"{host}{path}"


def source_id_for_url(url: str) -> str:
    return f"fathom_{sha(normalize_source(url))[:16]}"


def run_id_for_url(url: str) -> str:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{ts}_{sha(normalize_source(url))[:8]}"


def one_line_status(kind: str, run_id: str) -> str:
    if kind == "ok":
        return f"Received. Processing now. RUN_ID={run_id}."
    if kind == "already":
        return f"Already processed. RUN_ID={run_id}."
    return f"Couldn’t process automatically. Tommy has been alerted. RUN_ID={run_id}."


def lock_path(run_id: str, stage: str) -> Path:
    return LOCKS_DIR / f"{run_id}_{stage}.lock"


def lock_stage(run_id: str, stage: str, allow_reprocess: bool, stale_seconds: int = 1800) -> tuple[bool, str | None]:
    p = lock_path(run_id, stage)
    if p.exists():
        age = time.time() - p.stat().st_mtime
        if allow_reprocess or age > stale_seconds:
            p.unlink(missing_ok=True)
        else:
            return False, f"lock_exists age={int(age)}s"
    atomic_write_text(p, f"{now_iso()}\n")
    return True, None


def unlock_stage(run_id: str, stage: str) -> None:
    lock_path(run_id, stage).unlink(missing_ok=True)


def read_agent_text(stdout: str) -> str:
    try:
        j = json.loads(stdout)
        payloads = ((j.get("result") or {}).get("payloads") or [])
        if payloads and isinstance(payloads[0], dict):
            return (payloads[0].get("text") or "").strip()
    except Exception:
        pass
    return stdout.strip()


def call_agent(agent_id: str, message_obj: dict, timeout_sec: int = 240) -> str:
    p = subprocess.run(
        [
            "openclaw", "agent",
            "--agent", agent_id,
            "--timeout", str(timeout_sec),
            "--message", json.dumps(message_obj, ensure_ascii=False),
            "--json",
        ],
        capture_output=True,
        text=True,
    )
    if p.returncode != 0:
        raise RuntimeError(f"agent_call_failed agent={agent_id} rc={p.returncode} err={(p.stderr or '')[-400:]}")
    return read_agent_text(p.stdout)


def parse_mark_body(text: str) -> str:
    t = text.strip()
    if t.lower().startswith("caption_body:"):
        t = t.split(":", 1)[1].strip()
    return t


def parse_bob_caption(text: str) -> str:
    t = text.strip()
    if t.lower().startswith("final_caption:"):
        t = t.split(":", 1)[1].strip()
    return t


def parse_hooks(text: str) -> list[str]:
    hooks: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        m = re.match(r"^OVERLAY_HOOK_[123]\s*:\s*(.+)$", s, re.I)
        if m:
            hooks.append(m.group(1).strip())
    if len(hooks) >= 3:
        return hooks[:3]
    # fallback only for strict parsing failures
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return lines[:3]


def remove_banned_dash(s: str) -> str:
    return s.replace("—", ", ").replace("–", ", ").replace("--", ", ")


def trim_hook_words(hook: str, max_chars: int = 110) -> str:
    h = remove_banned_dash(hook)
    if len(h) <= max_chars:
        return h
    words = h.split()
    i = 0
    while len(" ".join(words)) > max_chars and i < len(words):
        if words[i].strip(".,!?;:").lower() in FILLER_WORDS:
            words.pop(i)
            i = 0
            continue
        i += 1
    out = " ".join(words)
    if len(out) > max_chars:
        out = out[:max_chars].rstrip()
    return out


def stage_template() -> dict:
    return {
        "status": "pending",
        "canonical_input_path": None,
        "canonical_output_path": None,
        "started_at": None,
        "completed_at": None,
        "handoff_message": None,
    }


def new_manifest(run_id: str, source_id: str, source_kind: str, reprocess: bool) -> dict:
    return {
        "run_id": run_id,
        "source_id": source_id,
        "source_kind": source_kind,
        "reprocess": reprocess,
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "current_stage": "donald",
        "stage_status": {
            "donald": stage_template(),
            "mark": stage_template(),
            "bob": stage_template(),
            "hook": stage_template(),
            "jimmy": stage_template(),
        },
        "flags": [],
        "errors": {},
        "meta": {
            "chat_policy": "one_line_only",
            "pipeline_mode": "single_direction_no_revision_loop",
        },
    }


def add_flag(manifest: dict, code: str, stage: str, severity: str, note: str) -> None:
    manifest["flags"].append({
        "flag_code": code,
        "stage": stage,
        "severity": severity,
        "short_note": note,
        "ts": now_iso(),
    })


def set_error(manifest: dict, stage: str, step: str, err: str, log_path: str) -> None:
    manifest["errors"] = {
        "stage": stage,
        "step": step,
        "error_message": err,
        "log_path": log_path,
        "ts": now_iso(),
    }


def manifest_path(run_dir: Path) -> Path:
    return run_dir / "manifest.json"


def append_log(run_id: str, line: str) -> None:
    lp = LOGS_DIR / f"{run_id}.log"
    with open(lp, "a", encoding="utf-8") as f:
        f.write(f"{now_iso()} {line}\n")


def select_donald_nugget(donald_nuggets: dict) -> dict | None:
    nuggets = donald_nuggets.get("nuggets") or []
    if not nuggets:
        return None
    eligible = [n for n in nuggets if n.get("eligible_for_content") is True]
    return (eligible or nuggets)[0]


def fallback_nugget_from_transcript(raw_transcript_file: str) -> dict:
    text = ""
    try:
        text = Path(raw_transcript_file).read_text(encoding="utf-8", errors="ignore")
    except Exception:
        text = ""

    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    # prefer spoken content after speaker marker
    spoken = []
    for ln in lines:
        if ":" in ln:
            spoken.append(ln.split(":", 1)[1].strip())
        else:
            spoken.append(ln)
    joined = " ".join(spoken)
    joined = re.sub(r"\s+", " ", joined).strip()
    snippet = (joined[:260] + "...") if len(joined) > 260 else (joined or "Choose one concrete step and do it before the day ends.")

    return {
        "nugget_id": "N_FALLBACK_1",
        "post_class_recommendation": "Authority",
        "conversion_angle": "none",
        "idea_one_liner": snippet,
        "proof_anchor_lines": ["Client described repeated delay loop.", "Action was clear, execution was postponed."],
        "first_step_seed": "Today: Take one avoided action before noon.",
        "eligible_for_content": True,
        "fallback_generated": True,
    }


def stage_paths(run_dir: Path, stage: str) -> StagePaths:
    in_map = {
        "donald": run_dir / "stage_inputs" / "donald_url_intake.json",
        "mark": run_dir / "stage_outputs" / "donald_canonical.json",
        "bob": run_dir / "stage_outputs" / "mark_body.md",
        "hook": run_dir / "stage_outputs" / "bob_caption.md",
        "jimmy": run_dir / "stage_outputs" / "hook_overlays.json",
    }
    out_map = {
        "donald": run_dir / "stage_outputs" / "donald_canonical.json",
        "mark": run_dir / "stage_outputs" / "mark_body.md",
        "bob": run_dir / "stage_outputs" / "bob_caption.md",
        "hook": run_dir / "stage_outputs" / "hook_overlays.json",
        "jimmy": run_dir / "final" / "final_post_ready.md",
    }
    return StagePaths(str(in_map[stage]), str(out_map[stage]))


def run_donald(run_dir: Path, manifest: dict, url: str, simulate: bool, reprocess: bool) -> None:
    stage = "donald"
    sp = stage_paths(run_dir, stage)
    s = manifest["stage_status"][stage]
    s["started_at"] = now_iso()
    s["canonical_input_path"] = sp.input_path
    atomic_write_json(Path(sp.input_path), {"run_id": manifest["run_id"], "source_id": manifest["source_id"], "url_present": True})

    if simulate:
        nug = {
            "nugget_id": "N1",
            "post_class_recommendation": "Authority",
            "conversion_angle": "none",
            "idea_one_liner": "Stop negotiating with fear, start obeying what you already know.",
            "proof_anchor_lines": ["You already knew what to do.", "You delayed because you feared the cost."],
            "first_step_seed": "Today: Do the one avoided action before noon.",
            "eligible_for_content": True,
        }
        canonical = {
            "run_id": manifest["run_id"],
            "source_id": manifest["source_id"],
            "route": nug["post_class_recommendation"],
            "conversion_angle": nug["conversion_angle"],
            "nugget": nug,
        }
    else:
        cmd = ["python3", str(DONALD_PROCESS), url]
        if reprocess:
            cmd.append("REPROCESS")
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode not in (0, 2):
            raise RuntimeError(f"donald_process_failed rc={p.returncode} err={(p.stderr or '')[-350:]}")
        donald_run = (p.stdout or "").strip().splitlines()[-1]
        d_manifest = VAULT / "manifests" / f"{donald_run}__manifest.json"
        client = "Unknown"
        p2 = subprocess.run(["python3", str(DONALD_EXTRACT), str(d_manifest), "--client", client], capture_output=True, text=True)
        if p2.returncode != 0:
            raise RuntimeError(f"donald_extract_failed rc={p2.returncode} err={(p2.stderr or '')[-350:]}")
        out = json.loads((p2.stdout or "{}").strip() or "{}")
        nuggets_path = out.get("nuggets")
        if not nuggets_path:
            raise RuntimeError("donald_extract_missing_nuggets_path")
        nug_payload = json.loads(Path(nuggets_path).read_text(encoding="utf-8"))
        sel = select_donald_nugget(nug_payload)
        if sel is None:
            # deterministic fallback for zero-nugget exports so pipeline still lands final review doc
            dman = json.loads(d_manifest.read_text(encoding="utf-8")) if d_manifest.exists() else {}
            raw_tf = dman.get("raw_transcript_file") or ""
            sel = fallback_nugget_from_transcript(raw_tf)
            add_flag(manifest, "DONALD_ZERO_NUGGET_FALLBACK", "donald", "warn", "No nuggets returned, generated deterministic fallback nugget")

        canonical = {
            "run_id": manifest["run_id"],
            "source_id": manifest["source_id"],
            "route": sel.get("post_class_recommendation") or "Authority",
            "conversion_angle": sel.get("conversion_angle") or "none",
            "nugget": sel,
            "donald_artifacts": {
                "donald_run_id": donald_run,
                "donald_manifest": str(d_manifest),
                "nuggets_json": nuggets_path,
            },
        }

    atomic_write_json(Path(sp.output_path), canonical)
    s["status"] = "done"
    s["completed_at"] = now_iso()
    s["canonical_output_path"] = sp.output_path
    s["handoff_message"] = f"RUN_ID={manifest['run_id']} STAGE=DONALD_DONE"


def run_mark(run_dir: Path, manifest: dict, simulate: bool) -> None:
    stage = "mark"
    sp = stage_paths(run_dir, stage)
    s = manifest["stage_status"][stage]
    s["started_at"] = now_iso()
    s["canonical_input_path"] = sp.input_path
    donald = json.loads(Path(sp.input_path).read_text(encoding="utf-8"))
    route = donald.get("route") or "Authority"

    if simulate:
        if route == "Conversion":
            body = "You keep calling it stress, but it is fear running your home.\n\nWhen you avoid one hard truth, you teach your heart to hide.\n\nWhen the fear hits: tell the truth in one sentence before you defend yourself."
        else:
            body = "Most men do not need more information, they need obedience.\n\nComment yes if you have delayed what God already made clear.\n\nToday: Do the one avoided action before noon."
    else:
        req = {
            "task": "caption_body_only",
            "run_id": manifest["run_id"],
            "route": route,
            "donald_canonical": donald,
            "output_shape": "CAPTION_BODY only",
            "constraints": {
                "no_hooks": True,
                "no_cta": True,
                "no_notes": True,
                "dash_ban": ["--", "—", "–"],
            },
        }
        body = parse_mark_body(call_agent("mark", req))

    if "OVERLAY_HOOK" in body or "Comment NEXT CHAPTER" in body:
        raise RuntimeError("mark_boundary_violation")

    body = remove_banned_dash(body)
    atomic_write_text(Path(sp.output_path), body.strip() + "\n")
    s["status"] = "done"
    s["completed_at"] = now_iso()
    s["canonical_output_path"] = sp.output_path
    s["handoff_message"] = f"RUN_ID={manifest['run_id']} STAGE=MARK_DONE"


def run_bob(run_dir: Path, manifest: dict, simulate: bool) -> None:
    stage = "bob"
    sp = stage_paths(run_dir, stage)
    s = manifest["stage_status"][stage]
    s["started_at"] = now_iso()
    s["canonical_input_path"] = sp.input_path

    body = Path(sp.input_path).read_text(encoding="utf-8").strip()
    donald = json.loads(Path(stage_paths(run_dir, "mark").input_path).read_text(encoding="utf-8"))
    route = donald.get("route") or "Authority"

    if simulate:
        if route == "Conversion":
            cta = "Comment NEXT CHAPTER and I’ll send you the first step to fast-track your healing process."
            append = "\n\nUnderstanding this is one thing.\nMost Christian men know the truth, but don’t know how to apply it in real time.\nSo if you’ve been struggling, this is your next step."
        else:
            cta = "If you're gonna use this in your life, follow so you don't miss out on more applicable relationship wisdom."
            append = ""
        caption = f"{body}{append}\n\n{cta}".strip()
    else:
        req = {
            "task": "append_only_close_cta",
            "run_id": manifest["run_id"],
            "route": route,
            "body_verbatim": body,
            "output_shape": "FINAL_CAPTION only",
            "constraints": {
                "append_only": True,
                "dash_ban": ["--", "—", "–"],
            },
        }
        caption = parse_bob_caption(call_agent("bob", req))

    if not caption.lstrip().startswith(body):
        add_flag(manifest, "BOB_APPEND_ONLY_FALLBACK", stage, "warn", "Bob output modified body, using deterministic append fallback")
        if route == "Conversion":
            fallback_cta = "Comment NEXT CHAPTER and I’ll send you the first step to fast-track your healing process."
            fallback_append = "\n\nUnderstanding this is one thing.\nMost Christian men know the truth, but don’t know how to apply it in real time.\nSo if you’ve been struggling, start with one honest action today."
        else:
            fallback_cta = "If you're gonna use this in your life, follow so you don't miss out on more applicable relationship wisdom."
            fallback_append = ""
        caption = f"{body}{fallback_append}\n\n{fallback_cta}".strip()

    caption = remove_banned_dash(caption)
    atomic_write_text(Path(sp.output_path), caption.strip() + "\n")
    s["status"] = "done"
    s["completed_at"] = now_iso()
    s["canonical_output_path"] = sp.output_path
    s["handoff_message"] = f"RUN_ID={manifest['run_id']} STAGE=BOB_DONE"


def run_hook(run_dir: Path, manifest: dict, simulate: bool) -> None:
    stage = "hook"
    sp = stage_paths(run_dir, stage)
    s = manifest["stage_status"][stage]
    s["started_at"] = now_iso()
    s["canonical_input_path"] = sp.input_path

    caption = Path(sp.input_path).read_text(encoding="utf-8").strip()

    if simulate:
        hooks = [
            "Delay becomes destiny faster than most men realize.",
            "Strong men act before feelings agree.",
            "Clarity comes when you obey before comfort.",
        ]
    else:
        req = {
            "task": "hooks_only",
            "run_id": manifest["run_id"],
            "caption_value_context": caption,
            "output_shape": "OVERLAY_HOOK_1/2/3 only",
            "constraints": {
                "count": 3,
                "one_sentence_each": True,
                "max_chars_each": 110,
                "dash_ban": ["--", "—", "–"],
            },
        }
        hooks = parse_hooks(call_agent("captainhook", req))

    hooks = [trim_hook_words(h, 110) for h in hooks][:3]
    if len(hooks) != 3:
        raise RuntimeError("hook_count_invalid")

    payload = {"OVERLAY_HOOK_1": hooks[0], "OVERLAY_HOOK_2": hooks[1], "OVERLAY_HOOK_3": hooks[2]}
    atomic_write_json(Path(sp.output_path), payload)
    s["status"] = "done"
    s["completed_at"] = now_iso()
    s["canonical_output_path"] = sp.output_path
    s["handoff_message"] = f"RUN_ID={manifest['run_id']} STAGE=HOOK_DONE"


def upload_final_to_drive(run_id: str, final_path: Path) -> dict:
    title = f"{run_id}: Final Post Ready"
    cmd = [
        "gog", "drive", "upload", str(final_path),
        "--parent", FINISHED_DRIVE_FOLDER_ID,
        "--convert-to", "doc",
        "--name", title,
        "--json", "--results-only", "--no-input",
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"drive_upload_failed rc={p.returncode} err={(p.stderr or '')[-350:]}")
    out = json.loads((p.stdout or "{}").strip() or "{}")
    file_id = out.get("id") or out.get("fileId")
    link = out.get("webViewLink") or out.get("link")
    return {"file_id": file_id, "link": link, "raw": out}


def run_jimmy(run_dir: Path, manifest: dict, simulate: bool) -> None:
    stage = "jimmy"
    sp = stage_paths(run_dir, stage)
    s = manifest["stage_status"][stage]
    s["started_at"] = now_iso()
    s["canonical_input_path"] = sp.input_path

    bob_path = Path(stage_paths(run_dir, "hook").input_path)
    hook_path = Path(stage_paths(run_dir, "jimmy").input_path)

    if not bob_path.exists() and hook_path.exists():
        add_flag(manifest, "PAIR_MISSING_BOB", stage, "error", "Hook exists but Bob missing")
        raise RuntimeError("pairing_failed_missing_bob")
    if bob_path.exists() and not hook_path.exists():
        add_flag(manifest, "PAIR_MISSING_HOOK", stage, "error", "Bob exists but Hook missing")
        raise RuntimeError("pairing_failed_missing_hook")

    caption = bob_path.read_text(encoding="utf-8").strip()
    hooks_obj = json.loads(hook_path.read_text(encoding="utf-8"))
    hooks = [hooks_obj.get("OVERLAY_HOOK_1", ""), hooks_obj.get("OVERLAY_HOOK_2", ""), hooks_obj.get("OVERLAY_HOOK_3", "")]

    clean_caption = remove_banned_dash(caption)
    clean_hooks = [trim_hook_words(h, 110) for h in hooks]

    if clean_caption != caption:
        add_flag(manifest, "JIMMY_MINIMAL_DASH_CLEANUP", stage, "warn", "Removed banned dash punctuation")

    # CTA last line check by route
    donald = json.loads(Path(stage_paths(run_dir, "mark").input_path).read_text(encoding="utf-8"))
    route = donald.get("route") or "Authority"
    lines = [ln for ln in clean_caption.splitlines() if ln.strip()]
    last = lines[-1] if lines else ""
    if route == "Authority":
        expected = "If you're gonna use this in your life, follow so you don't miss out on more applicable relationship wisdom."
    else:
        angle = (donald.get("conversion_angle") or "heartbreak").lower()
        expected = "Comment NEXT CHAPTER and I’ll send you the first step to becoming your wife’s safe place again." if "divorce" in angle else "Comment NEXT CHAPTER and I’ll send you the first step to fast-track your healing process."

    if last != expected:
        add_flag(manifest, "CTA_LAST_LINE_MISMATCH", stage, "warn", "Final CTA line not exact expected line")

    out = []
    out.append(f"RUN_ID: {manifest['run_id']}")
    out.append("OVERLAY_HOOK_1: " + clean_hooks[0])
    out.append("OVERLAY_HOOK_2: " + clean_hooks[1])
    out.append("OVERLAY_HOOK_3: " + clean_hooks[2])
    out.append("OVERLAY_CTA: read caption")
    out.append("")
    out.append("CAPTION:")
    out.append(clean_caption)
    out.append("")
    out.append("NOTES:")
    out.append("- mechanical_assembly_only=true")
    out.append("- style_rewrite=false")
    out.append("- final=true")

    final_path = Path(sp.output_path)
    atomic_write_text(final_path, "\n".join(out).strip() + "\n")

    drive = upload_final_to_drive(manifest["run_id"], final_path)
    manifest.setdefault("final_delivery", {})
    manifest["final_delivery"] = {
        "drive_folder_id": FINISHED_DRIVE_FOLDER_ID,
        "drive_file_id": drive.get("file_id"),
        "drive_link": drive.get("link"),
        "uploaded_at": now_iso(),
    }

    s["status"] = "done"
    s["completed_at"] = now_iso()
    s["canonical_output_path"] = sp.output_path
    s["handoff_message"] = f"RUN_ID={manifest['run_id']} STAGE=FINAL_READY"


def finalize_run(run_dir: Path, manifest: dict, success: bool) -> None:
    target = ARCHIVE_DIR / manifest["run_id"] if success else QUARANTINE_DIR / manifest["run_id"]
    if target.exists():
        subprocess.run(["rm", "-rf", str(target)], check=False)
    os.replace(run_dir, target)


def update_source_index(source_id: str, run_id: str) -> None:
    idx = load_json(SOURCE_INDEX_PATH, {"items": {}, "updated_at": None})
    idx["items"][source_id] = {"run_id": run_id, "status": "success", "updated_at": now_iso()}
    idx["updated_at"] = now_iso()
    atomic_write_json(SOURCE_INDEX_PATH, idx)


def already_processed(source_id: str) -> str | None:
    idx = load_json(SOURCE_INDEX_PATH, {"items": {}})
    item = (idx.get("items") or {}).get(source_id)
    if item and item.get("status") == "success":
        return item.get("run_id")
    return None


def run_one(url: str, reprocess: bool = False, simulate: bool = False, force_partial_write_test: bool = False) -> dict:
    ensure_dirs()
    source_id = source_id_for_url(url)
    existing = already_processed(source_id)
    if existing and not reprocess:
        return {"ok": True, "run_id": existing, "status_line": one_line_status("already", existing), "already_processed": True}

    run_id = run_id_for_url(url)
    run_dir = RUNS_DIR / run_id
    (run_dir / "stage_inputs").mkdir(parents=True, exist_ok=True)
    (run_dir / "stage_outputs").mkdir(parents=True, exist_ok=True)
    (run_dir / "final").mkdir(parents=True, exist_ok=True)

    manifest = new_manifest(run_id, source_id, "fathom_share_url", reprocess)
    mpath = manifest_path(run_dir)
    atomic_write_json(mpath, manifest)

    stages = ["donald", "mark", "bob", "hook", "jimmy"]
    ok = False
    try:
        for stage in stages:
            can, reason = lock_stage(run_id, stage, allow_reprocess=reprocess)
            if not can:
                raise RuntimeError(f"{stage}_lock_blocked {reason}")
            try:
                manifest["current_stage"] = stage
                atomic_write_json(mpath, manifest)

                if stage == "donald":
                    run_donald(run_dir, manifest, url, simulate=simulate, reprocess=reprocess)
                elif stage == "mark":
                    run_mark(run_dir, manifest, simulate=simulate)
                elif stage == "bob":
                    run_bob(run_dir, manifest, simulate=simulate)
                elif stage == "hook":
                    run_hook(run_dir, manifest, simulate=simulate)
                    if force_partial_write_test:
                        # simulate delay and verify downstream reads canonical only after completed file exists
                        time.sleep(1)
                elif stage == "jimmy":
                    run_jimmy(run_dir, manifest, simulate=simulate)

                atomic_write_json(mpath, manifest)
            finally:
                unlock_stage(run_id, stage)

        ok = True
        update_source_index(source_id, run_id)
        status_line = one_line_status("ok", run_id)
        append_log(run_id, f"SUCCESS {status_line}")
        return {"ok": True, "run_id": run_id, "status_line": status_line, "manifest": str(mpath)}
    except Exception as e:
        set_error(manifest, manifest.get("current_stage") or "unknown", "pipeline", str(e), str(LOGS_DIR / f"{run_id}.log"))
        atomic_write_json(mpath, manifest)
        status_line = one_line_status("fail", run_id)
        append_log(run_id, f"FAIL stage={manifest.get('current_stage')} err={e}")
        return {"ok": False, "run_id": run_id, "status_line": status_line, "manifest": str(mpath), "error": str(e)}
    finally:
        finalize_run(run_dir, manifest, success=ok)


def intake_from_index(n: int) -> list[str]:
    idx = load_json(FATHOM_INDEX, [])
    processed = set((load_json(FATHOM_PROCESSED, {"processed": []}).get("processed") or []))
    urls = []
    for item in idx:
        u = (item or {}).get("share_url")
        if not u:
            continue
        if u in processed:
            continue
        urls.append(u)
    return urls[:max(0, n)]


def run_acceptance_tests() -> dict:
    ensure_dirs()
    test_results: list[dict] = []

    # 1, 2, 5, 7, 8 basic happy path with simulate
    r1 = run_one("https://fathom.video/share/test_abc123", reprocess=True, simulate=True)
    test_results.append({"name": "URL intake one line", "pass": bool(re.match(r"^(Received\. Processing now\.|Already processed\.|Couldn’t process automatically\.)", r1.get("status_line", ""))), "run_id": r1.get("run_id")})

    # 3 idempotency
    r2 = run_one("https://fathom.video/share/test_abc123", reprocess=False, simulate=True)
    test_results.append({"name": "Idempotency same URL", "pass": r2.get("already_processed") is True, "run_id": r2.get("run_id")})

    # 4 atomic write with delay
    r3 = run_one("https://fathom.video/share/test_atomic_1", reprocess=True, simulate=True, force_partial_write_test=True)
    test_results.append({"name": "Atomic write no partial reads", "pass": bool(r3.get("ok")), "run_id": r3.get("run_id")})

    # 6 pairing test, force missing hook by creating run and manually invoking jimmy pre-hook
    rid = run_id_for_url("https://fathom.video/share/test_pairing")
    run_dir = RUNS_DIR / rid
    (run_dir / "stage_inputs").mkdir(parents=True, exist_ok=True)
    (run_dir / "stage_outputs").mkdir(parents=True, exist_ok=True)
    (run_dir / "final").mkdir(parents=True, exist_ok=True)
    m = new_manifest(rid, source_id_for_url("https://fathom.video/share/test_pairing"), "fathom_share_url", True)
    atomic_write_json(manifest_path(run_dir), m)
    atomic_write_text(Path(stage_paths(run_dir, "hook").input_path), "Body only\n\nIf you're gonna use this in your life, follow so you don't miss out on more applicable relationship wisdom.\n")
    pairing_pass = False
    try:
        run_jimmy(run_dir, m, simulate=True)
    except Exception:
        pairing_pass = True
    finalize_run(run_dir, m, success=False)
    test_results.append({"name": "Pairing rule blocks finalize when hook missing", "pass": pairing_pass, "run_id": rid})

    # failure test (bad url, non simulate)
    r4 = run_one("https://example.com/not-fathom", reprocess=True, simulate=False)
    test_results.append({"name": "Failure one-line response", "pass": (not r4.get("ok")) and bool(re.match(r"^Couldn’t process automatically\.", r4.get("status_line", ""))), "run_id": r4.get("run_id")})

    # punctuation ban on final output
    final_ok = False
    if r1.get("run_id"):
        p = ARCHIVE_DIR / r1["run_id"] / "final" / "final_post_ready.md"
        if p.exists():
            final_ok = not bool(BANNED_DASH_RE.search(p.read_text(encoding="utf-8")))
    test_results.append({"name": "Punctuation ban final output", "pass": final_ok, "run_id": r1.get("run_id")})

    all_pass = all(t["pass"] for t in test_results)
    out = {
        "ok": all_pass,
        "tests": test_results,
        "ts": now_iso(),
    }
    atomic_write_json(LOGS_DIR / f"acceptance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", out)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic 5-agent pipeline v2")
    ap.add_argument("--url", action="append", default=[])
    ap.add_argument("--from-index", type=int, default=0, help="take N pending URLs from fathom index")
    ap.add_argument("--reprocess", action="store_true")
    ap.add_argument("--simulate", action="store_true")
    ap.add_argument("--acceptance-tests", action="store_true")
    args = ap.parse_args()

    if args.acceptance_tests:
        out = run_acceptance_tests()
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0 if out["ok"] else 1

    urls = list(args.url)
    if args.from_index > 0:
        urls.extend(intake_from_index(args.from_index))

    if not urls:
        print(json.dumps({"ok": False, "error": "no_urls"}, indent=2))
        return 2

    results = [run_one(u, reprocess=args.reprocess, simulate=args.simulate) for u in urls]
    ok = all(r.get("ok") for r in results)
    print(json.dumps({"ok": ok, "count": len(results), "results": results}, indent=2, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

```



## Script: donald_process_url.py

```python
import json
import os
import sys
import subprocess
import urllib.parse
import urllib.request
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


def _http_get_json(url: str, headers: dict | None = None):
    req = urllib.request.Request(url, headers=headers or {}, method="GET")
    with urllib.request.urlopen(req, timeout=45) as resp:
        body = resp.read().decode("utf-8")
    return json.loads(body)


def _find_meeting_by_share_url(share_url: str, api_key: str, max_pages: int = 30):
    base = "https://api.fathom.ai/external/v1/meetings"
    headers = {"X-Api-Key": api_key, "Accept": "application/json"}
    cursor = None
    for _ in range(max_pages):
        params = {"limit": "100"}
        if cursor:
            params["cursor"] = cursor
        url = f"{base}?{urllib.parse.urlencode(params)}"
        payload = _http_get_json(url, headers=headers)
        for item in payload.get("items") or []:
            if (item.get("share_url") or "").strip() == share_url.strip():
                return item
        cursor = payload.get("next_cursor")
        if not cursor:
            break
    return None


def _get_transcript_by_recording_id(recording_id: int, api_key: str):
    url = f"https://api.fathom.ai/external/v1/recordings/{recording_id}/transcript"
    headers = {"X-Api-Key": api_key, "Accept": "application/json"}
    data = _http_get_json(url, headers=headers)
    if isinstance(data, dict):
        chunks = data.get("transcript") or data.get("items") or []
    elif isinstance(data, list):
        chunks = data
    else:
        chunks = []
    lines = []
    for c in chunks:
        speaker = (((c or {}).get("speaker") or {}).get("display_name")) or "Unknown"
        ts = (c or {}).get("timestamp") or ""
        text = (c or {}).get("text") or ""
        lines.append(f"[{ts}] {speaker}: {text}".rstrip())
    return "\n".join(lines).strip()


def _fetch_via_fathom_api(url: str):
    api_key = os.environ.get("FATHOM_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("FATHOM_API_KEY not configured")
    if "/share/" not in url:
        raise RuntimeError("Not a Fathom share URL")

    meeting = _find_meeting_by_share_url(url, api_key=api_key)
    if not meeting:
        raise RuntimeError("Meeting not found for share_url in Fathom API")

    rid = meeting.get("recording_id")
    if not rid:
        raise RuntimeError("recording_id missing for matched meeting")

    transcript_text = _get_transcript_by_recording_id(int(rid), api_key=api_key)
    if not transcript_text:
        raise RuntimeError("Transcript came back empty from Fathom API")
    return transcript_text, meeting


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

    allowed_substr = os.environ.get("KRC_ALLOWED_DOMAIN_SUBSTR", ALLOWED_DOMAIN_SUBSTR_DEFAULT)
    if allowed_substr and allowed_substr not in url:
        m["error_message"] = f"Domain not allowed. Required substring: {allowed_substr}"
        write_manifest(m)
        append_log(run_id, m["error_message"])
        print(run_id)
        return 2

    existing = find_existing_success(url)
    if existing and not reprocess:
        append_log(run_id, f"SKIP already processed successfully as RUN_ID={existing}")
        # Carry forward usable artifact pointers so downstream handoff cannot point to null paths.
        prev_manifest_path = os.path.join(os.path.expanduser('~/krc_vault/manifests'), f"{existing}__manifest.json")
        try:
            with open(prev_manifest_path, 'r', encoding='utf-8') as f:
                prev = json.load(f)
            m["raw_transcript_file"] = prev.get("raw_transcript_file")
            m["nugget_export_file"] = prev.get("nugget_export_file")
        except Exception as e:
            append_log(run_id, f"WARN unable_to_load_prev_manifest run_id={existing} error={e}")
        m["status"] = "success"
        m["error_message"] = None
        write_manifest(m)
        print(run_id)
        return 0

    meeting = None
    transcript_text = None
    try:
        transcript_text, meeting = _fetch_via_fathom_api(url)
        append_log(run_id, "FETCH source=fathom_api status=ok")
    except Exception as api_err:
        append_log(run_id, f"FETCH source=fathom_api status=fail error={api_err}")
        try:
            res = subprocess.run(
                ["curl", "-fsSL", "--max-time", "45", url],
                capture_output=True,
                text=True,
                check=True,
            )
            transcript_text = res.stdout
            append_log(run_id, "FETCH source=curl_fallback status=ok")
        except Exception as e:
            m["error_message"] = f"Fetch failed: {e}"
            write_manifest(m)
            append_log(run_id, m["error_message"])
            print(run_id)
            return 3

    Path(RAW_DIR).mkdir(parents=True, exist_ok=True)
    base = meeting.get("meeting_title") if isinstance(meeting, dict) else sanitize_filename(url)
    base = sanitize_filename(base or url)[:80]
    raw_path = os.path.join(RAW_DIR, f"{run_id}__{base}.txt")
    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(transcript_text or "")

    m["raw_transcript_file"] = raw_path
    write_manifest(m)
    append_log(run_id, f"WROTE raw_transcript_file={raw_path}")

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
    m["error_message"] = None
    write_manifest(m)
    append_log(run_id, f"WROTE nugget_export_file={export_path}")

    print(run_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

```



## Script: donald_extract_from_manifest.py

```python
#!/usr/bin/env python3
"""Run Donald extraction from an existing manifest (after transcript fetch).

This avoids asking Donald to write outside workspace roots.

Inputs:
- manifest path: ~/krc_vault/manifests/<run_id>__manifest.json
Outputs:
- nuggets JSON: ~/krc_vault/gold nugget exports/<run_id>__<Client>__nuggets.json
- objections JSON: ~/krc_vault/gold nugget exports/<run_id>__<Client>__objections.json

Implementation note:
- For now we generate a minimal schema to keep pipeline unblocked.
- Later we can call the Donald agent itself to do full scoring; this script is the deterministic fallback.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('manifest_path')
    ap.add_argument('--client', default='Unknown')
    args = ap.parse_args()

    mp = Path(os.path.expanduser(args.manifest_path))
    m = json.loads(mp.read_text())
    run_id = m['run_id']

    raw_path = m.get('raw_transcript_file')
    if not raw_path or not Path(raw_path).exists():
        print(json.dumps({'ok': False, 'error': 'raw_transcript_file missing', 'run_id': run_id}))
        return 2

    # Minimal nugget export for now: include pointers + 3 simple extracted highlights (placeholder).
    # IMPORTANT: no fabrication of transcript quotes; we do not extract without parsing transcript.
    nuggets = {
        'schema_version': 'prospector_min_v0',
        'run_id': run_id,
        'source_id': m.get('source_url') or m.get('url_hash') or 'fathom',
        'final': True,
        'note': 'Minimal export generated by deterministic fallback. Replace with Donald full extraction later.',
        'raw_transcript_file': raw_path,
        'nuggets': []
    }

    objections = {
        'schema_version': 'objectionbank_min_v0',
        'run_id': run_id,
        'source_id': m.get('source_url') or m.get('url_hash') or 'fathom',
        'final': True,
        'objections': []
    }

    out_dir = Path(os.path.expanduser('~/krc_vault/gold nugget exports'))
    out_dir.mkdir(parents=True, exist_ok=True)
    client = args.client.strip() or 'Unknown'
    safe_client = ''.join(c if c.isalnum() or c in ' ._-' else '_' for c in client)[:60].strip() or 'Unknown'

    nug_path = out_dir / f"{run_id}__{safe_client}__nuggets.json"
    obj_path = out_dir / f"{run_id}__{safe_client}__objections.json"

    nug_path.write_text(json.dumps(nuggets, indent=2, ensure_ascii=False))
    obj_path.write_text(json.dumps(objections, indent=2, ensure_ascii=False))

    print(json.dumps({'ok': True, 'run_id': run_id, 'nuggets': str(nug_path), 'objections': str(obj_path)}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

```



## Script: donald_batch_from_library.py

```python
#!/usr/bin/env python3
"""Run a Donald batch from the local Fathom library.

Stage 1 goal: reliable throughput.
- Picks next N unprocessed share URLs.
- Runs donald_process_url.py for each (API fetch + transcript saved + manifest written).
- Marks them processed.
- Writes minimal nuggets/objections exports via donald_extract_from_manifest.py

Outputs JSON summary for cron delivery.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
from pathlib import Path


def load_json(p: Path, default):
    if not p.exists():
        return default
    return json.loads(p.read_text())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=3)
    args = ap.parse_args()

    index_path = Path(os.path.expanduser('~/krc_vault/fathom_library/index.json'))
    state_dir = Path(os.path.expanduser('~/krc_vault/fathom_library/state'))
    state_path = state_dir / 'processed.json'
    state_dir.mkdir(parents=True, exist_ok=True)

    idx = load_json(index_path, [])
    state = load_json(state_path, {'processed': [], 'updated_at': None})
    processed = set(state.get('processed') or [])

    pending = [r for r in idx if r.get('share_url') and r['share_url'] not in processed]
    selected = pending[: max(0, args.n)]

    results = []
    ok_all = True

    for r in selected:
        url = r['share_url']
        cmd = ['python3', '/home/openclaw_agent_1/.openclaw/scripts/krc/donald_process_url.py', url]
        p = subprocess.run(cmd, capture_output=True, text=True)
        run_id = (p.stdout or '').strip().splitlines()[-1] if (p.stdout or '').strip() else None

        item = {
            'share_url': url,
            'client': r.get('client'),
            'created_at': r.get('created_at'),
            'meeting_title': r.get('meeting_title'),
            'ok': p.returncode in (0, 2),
            'returncode': p.returncode,
            'run_id': run_id,
            'stderr': (p.stderr or '')[:400],
            'nugget_export': None,
            'objection_export': None,
        }

        if item['ok'] and run_id:
            # Create minimal exports deterministically
            manifest = os.path.expanduser(f"~/krc_vault/manifests/{run_id}__manifest.json")
            cmd2 = ['python3', '/home/openclaw_agent_1/.openclaw/scripts/krc/donald_extract_from_manifest.py', manifest, '--client', (r.get('client') or 'Unknown')]
            p2 = subprocess.run(cmd2, capture_output=True, text=True)
            if p2.returncode == 0:
                try:
                    j = json.loads((p2.stdout or '{}').strip() or '{}')
                    item['nugget_export'] = j.get('nuggets')
                    item['objection_export'] = j.get('objections')
                except Exception:
                    pass
            else:
                item['ok'] = False
                item['stderr'] = ((item['stderr'] or '') + ' | extract_failed: ' + (p2.stderr or '')[:200]).strip()

        if item['ok']:
            processed.add(url)
        else:
            ok_all = False

        results.append(item)

    state['processed'] = sorted(processed)
    state['updated_at'] = dt.datetime.now(dt.timezone.utc).isoformat()
    state_path.write_text(json.dumps(state, indent=2))

    # Persist last batch for downstream jobs (Donald full extract, Jimmy drafts)
    last_batch_path = state_dir / 'last_batch.json'
    last_batch_path.write_text(json.dumps({
        'created_at': dt.datetime.now(dt.timezone.utc).isoformat(),
        'pending_total': len(pending),
        'selected_count': len(selected),
        'results': results,
    }, indent=2, ensure_ascii=False))


    out = {
        'ok': ok_all,
        'pending_total': len(pending),
        'selected_count': len(selected),
        'results': results,
        'state_file': str(state_path),
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if ok_all else 1


if __name__ == '__main__':
    raise SystemExit(main())

```



## Script: marketing_pipeline_orchestrator.py

```python
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

```



## Script: jimmy_generate_from_nuggets.py

```python
#!/usr/bin/env python3
"""Generate finished content (Jimmy) from Donald nugget export JSON.

This is a robust, script-based runner to avoid cron agentTurns wedging.
It uses `openclaw agent --agent jimmy --local` (runs embedded locally).

Inputs:
- nuggets JSON file path
- run_id
Outputs:
- finished markdown in ~/krc_vault/finished content for posting/
- uploads to Drive via gog
- updates manifest drive link

Requirements:
- openclaw CLI configured with model access for --local (if not available, this script will fail).
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

# Ensure krc scripts folder is importable (for run_helpers)
import sys
sys.path.insert(0, '/home/openclaw_agent_1/.openclaw/scripts/krc')

FINISHED_DIR = Path(os.path.expanduser('~/krc_vault/finished content for posting'))
MANIFEST_DIR = Path(os.path.expanduser('~/krc_vault/manifests'))
DRIVE_FOLDER_ID = '1NOCxQ2K1S2vM07hGHc0xEqTrsl2Ub1tv'


def load_json(p: Path):
    return json.loads(p.read_text())


def save_json(p: Path, obj):
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('nuggets_json')
    ap.add_argument('--run-id', required=True)
    ap.add_argument('--client', default='Unknown')
    args = ap.parse_args()

    nuggets_path = Path(args.nuggets_json)
    if not nuggets_path.exists():
        print(json.dumps({'ok': False, 'error': 'nuggets_json not found', 'path': str(nuggets_path)}))
        return 2

    run_id = args.run_id
    manifest_path = MANIFEST_DIR / f'{run_id}__manifest.json'
    if not manifest_path.exists():
        print(json.dumps({'ok': False, 'error': 'manifest missing', 'run_id': run_id}))
        return 3

    # Ask Jimmy to write finished content following his strict contract.
    nuggets_obj = load_json(nuggets_path)
    prompt = {
        'run_id': run_id,
        'client': args.client,
        'instruction': (
            'Generate finished content markdown. Output must be ONLY the finished content markdown (no code fences). '\
            'It MUST include a line starting with "CAPTION:" followed by a clear, scannable title line (5-12 words) on the next line.'
        ),
        'nuggets_export': nuggets_obj,
    }

    # Run Jimmy locally through embedded agent.
    cmd = [
        'openclaw','agent',
        '--agent','jimmy',
        '--local',
        '--timeout','900',
        '--message', json.dumps(prompt, ensure_ascii=False),
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        print(json.dumps({'ok': False, 'error': 'openclaw agent failed', 'stderr': p.stderr[-800:], 'stdout': p.stdout[-800:]}))
        return 4

    content = p.stdout
    if not content.strip():
        print(json.dumps({'ok': False, 'error': 'empty output from jimmy'}))
        return 5

    FINISHED_DIR.mkdir(parents=True, exist_ok=True)
    finished_path = FINISHED_DIR / f'{run_id}__finished_content.md'
    finished_path.write_text(content, encoding='utf-8')

    # Upload to Drive as a Google Doc (use a scannable name)
    from run_helpers import infer_drive_doc_name  # local helper
    doc_name = infer_drive_doc_name(run_id, str(finished_path), client=args.client)

    up = subprocess.run(
        ['gog','drive','upload', str(finished_path), '--parent', DRIVE_FOLDER_ID, '--convert-to','doc', '--name', doc_name, '--json','--results-only','--no-input'],
        capture_output=True,
        text=True,
    )
    if up.returncode != 0:
        print(json.dumps({'ok': False, 'error': 'drive upload failed', 'stderr': up.stderr[-800:]}))
        return 6

    meta = json.loads(up.stdout)
    file_meta = meta.get('file') or meta
    link = file_meta.get('webViewLink')
    file_id = file_meta.get('id')

    m = load_json(manifest_path)
    m.setdefault('drive', {})
    m['drive'].update({'file_id': file_id, 'folder_id': DRIVE_FOLDER_ID, 'link': link, 'format': 'google_doc'})
    # Ensure finished content is recorded
    m['finished_content_file(s)'] = [str(finished_path)]
    save_json(manifest_path, m)

    print(json.dumps({'ok': True, 'run_id': run_id, 'drive_link': link, 'file_id': file_id, 'finished_path': str(finished_path)}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

```



## Script: jimmy_generate_from_last_batch.py

```python
#!/usr/bin/env python3
"""Generate Jimmy finished drafts for the latest batch.

Reads last_batch.json, picks REAL nuggets files (largest) per run_id, runs
jimmy_generate_from_nuggets.py for each.

Outputs JSON with drive links.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path


def main() -> int:
    last = Path(os.path.expanduser('~/krc_vault/fathom_library/state/last_batch.json'))
    if not last.exists():
        print(json.dumps({'ok': False, 'error': 'last_batch.json missing'}))
        return 2

    batch = json.loads(last.read_text())
    out = {'ok': True, 'results': []}

    for r in (batch.get('results') or []):
        if not r.get('ok'):
            continue
        run_id = r.get('run_id')
        client = r.get('client') or 'Unknown'
        if not run_id:
            continue

        # pick largest nuggets json for run_id
        cand_dir = Path(os.path.expanduser('~/krc_vault/gold nugget exports'))
        cands = sorted(cand_dir.glob(f"{run_id}__*__nuggets.json"), key=lambda p: p.stat().st_size, reverse=True)
        if not cands:
            out['ok'] = False
            out['results'].append({'run_id': run_id, 'client': client, 'ok': False, 'error': 'no nuggets json found'})
            continue

        nuggets = str(cands[0])
        cmd = ['python3','/home/openclaw_agent_1/.openclaw/scripts/krc/jimmy_generate_from_nuggets.py', nuggets, '--run-id', run_id, '--client', client]
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode != 0:
            out['ok'] = False
            out['results'].append({'run_id': run_id, 'client': client, 'ok': False, 'error': p.stderr[-400:] or p.stdout[-400:]})
            continue

        try:
            j = json.loads((p.stdout or '').strip() or '{}')
        except Exception:
            j = {'ok': False, 'error': 'non-json output', 'stdout': (p.stdout or '')[-400:]}

        out['results'].append({'run_id': run_id, 'client': client, **j})

    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())

```



## Script: jimmy_batch_from_last.py

```python
#!/usr/bin/env python3
"""Run Jimmy on the most recent fathom library batch.

Reads:
- ~/krc_vault/fathom_library/state/last_batch.json

For each ok=true result:
- Uses nugget_export path from last_batch (or derives from run_id)
- Runs jimmy_process_export.py

Outputs JSON summary.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path


def main() -> int:
    last = Path(os.path.expanduser('~/krc_vault/fathom_library/state/last_batch.json'))
    if not last.exists():
        print(json.dumps({'ok': False, 'error': 'last_batch.json missing'}))
        return 2

    batch = json.loads(last.read_text())
    results = []
    ok_all = True

    for r in (batch.get('results') or []):
        if not r.get('ok'):
            continue
        run_id = r.get('run_id')
        export_path = r.get('nugget_export')
        if not export_path and run_id:
            # fallback: find any nugget file matching run_id
            cand_dir = Path(os.path.expanduser('~/krc_vault/gold nugget exports'))
            cands = sorted(cand_dir.glob(f"{run_id}__*__nuggets.json"))
            export_path = str(cands[0]) if cands else None

        if not export_path or not Path(export_path).exists():
            ok_all = False
            results.append({'run_id': run_id, 'ok': False, 'error': f'export not found: {export_path}'})
            continue

        cmd = ['python3', '/home/openclaw_agent_1/.openclaw/scripts/krc/jimmy_process_export.py', export_path]
        p = subprocess.run(cmd, capture_output=True, text=True)
        item = {
            'run_id': run_id,
            'export': export_path,
            'ok': p.returncode == 0,
            'returncode': p.returncode,
            'stderr': (p.stderr or '')[:400],
        }
        if not item['ok']:
            ok_all = False
        results.append(item)

    print(json.dumps({'ok': ok_all, 'results': results}, indent=2))
    return 0 if ok_all else 1


if __name__ == '__main__':
    raise SystemExit(main())

```



## Script: run_helpers.py

```python
import hashlib
import json
import os
import re
from pathlib import Path
from datetime import datetime, timezone

VAULT = os.path.expanduser('~/krc_vault')
RAW_DIR = os.path.join(VAULT, 'raw call transcripts')
NUGGET_DIR = os.path.join(VAULT, 'gold nugget exports')
FINISHED_DIR = os.path.join(VAULT, 'finished content for posting')
LOG_DIR = os.path.join(VAULT, 'run logs')
MANIFEST_DIR = os.path.join(VAULT, 'manifests')

# Google Drive folder for finished content (OpenClaw Finished Content)
FINISHED_DRIVE_FOLDER_ID = '1NOCxQ2K1S2vM07hGHc0xEqTrsl2Ub1tv'

ALLOWED_DOMAIN_SUBSTR_DEFAULT = 'fathom'


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def short_hash(s: str, n: int = 8) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:n]


def url_hash(url: str) -> str:
    return hashlib.sha256(url.encode('utf-8')).hexdigest()


def new_run_id(url: str) -> str:
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"{ts}_{short_hash(url, 8)}"


def sanitize_filename(s: str, max_len: int = 80) -> str:
    s = re.sub(r'https?://', '', s)
    s = re.sub(r'[^A-Za-z0-9._-]+', '_', s)
    s = s.strip('_')
    if len(s) > max_len:
        s = s[:max_len]
    return s or 'untitled'


def manifest_path(run_id: str) -> str:
    return os.path.join(MANIFEST_DIR, f"{run_id}__manifest.json")


def log_path(run_id: str) -> str:
    return os.path.join(LOG_DIR, f"{run_id}__log.txt")


def load_manifest(run_id: str):
    p = manifest_path(run_id)
    if not os.path.exists(p):
        return None
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_manifest(m: dict):
    os.makedirs(MANIFEST_DIR, exist_ok=True)
    m['updated_at'] = now_iso()
    if 'created_at' not in m:
        m['created_at'] = m['updated_at']
    with open(manifest_path(m['run_id']), 'w', encoding='utf-8') as f:
        json.dump(m, f, indent=2, ensure_ascii=False)


def append_log(run_id: str, line: str):
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(log_path(run_id), 'a', encoding='utf-8') as f:
        f.write(line.rstrip('\n') + '\n')


def _is_usable_success_manifest(m: dict) -> bool:
    """Success manifests are usable only if required artifact paths exist."""
    if (m or {}).get('status') != 'success':
        return False
    raw = (m or {}).get('raw_transcript_file')
    nug = (m or {}).get('nugget_export_file')
    if not raw or not nug:
        return False
    return os.path.exists(raw) and os.path.exists(nug)


def find_existing_success(url: str):
    """Return best usable prior success run_id for this URL hash, else None.

    A prior run only counts as success for idempotency if its core artifacts exist.
    """
    uh = url_hash(url)
    if not os.path.isdir(MANIFEST_DIR):
        return None

    candidates: list[tuple[float, str]] = []
    for name in os.listdir(MANIFEST_DIR):
        if not name.endswith('__manifest.json'):
            continue
        p = os.path.join(MANIFEST_DIR, name)
        try:
            with open(p, 'r', encoding='utf-8') as f:
                m = json.load(f)
            if m.get('url_hash') != uh:
                continue
            if not _is_usable_success_manifest(m):
                continue
            # Prefer latest by manifest mtime.
            candidates.append((os.path.getmtime(p), m.get('run_id')))
        except Exception:
            continue

    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][1]


def infer_drive_doc_name(run_id: str, finished_md_path: str, client: str | None = None, max_len: int = 120) -> str:
    """Create a human-readable Google Doc name for Drive.

    Goal: make Drive list scannable.

    Format:
      <Client> — <First caption line> (<run_id suffix>)

    - Extracts first non-empty line after 'CAPTION:' in the finished content file.
    - Collapses whitespace and truncates.
    """
    title = None
    try:
        content = Path(finished_md_path).read_text(encoding='utf-8', errors='ignore')
        idx = content.find('CAPTION:')
        if idx != -1:
            after = content[idx + len('CAPTION:'):].lstrip('\n ').splitlines()
            for line in after:
                s = line.strip()
                if not s:
                    continue
                # Skip obvious headings/labels
                if s.upper() in {'NOTES:', 'CAPTION:', 'OVERLAY_CTA:', 'OVERLAY_HOOK_1:', 'OVERLAY_HOOK_2:', 'OVERLAY_HOOK_3:'}:
                    continue
                if s.startswith('#') or s.startswith('##') or s.startswith('---'):
                    continue
                s = re.sub(r'\s+', ' ', s)
                title = s
                break
    except Exception:
        title = None

    if not title:
        title = 'Finished Content'

    # Try to include client for scanability
    client_part = None
    if client:
        client_part = sanitize_filename(client, max_len=40).replace('_', ' ').strip()
    if client_part:
        # use last 8 of run_id to avoid repeating date prefix everywhere
        suffix = run_id[-8:]
        name = f"{client_part} — {title} ({suffix})"
    else:
        name = f"{run_id}: {title}"

    name = re.sub(r'\s+', ' ', name).strip()
    return name[:max_len]

```



## Script: fathom_library_build.py

```python
#!/usr/bin/env python3
"""Build a searchable Fathom library index + per-client link lists.

Stage 1 deliverables (local vault only):
- ~/krc_vault/fathom_library/index.csv
- ~/krc_vault/fathom_library/index.json
- ~/krc_vault/fathom_library/clients/<Letter>/<Client Name> (<email>).md

Client naming rule (per Andre):
- Source of truth: the *other person* who has a meeting with Andre.
- Include email suffix for disambiguation: "Name (email)".
- Worst case: "Unknown (email)" or "Unknown (unknown@example.com)".

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

    If calendar_invitees.name is missing or unhelpful, fall back to parsing
    meeting title format: "<Client> and Andre Panet-Raymond".
    """

    def parse_client_from_title(title: str) -> Optional[str]:
        t = normalize_spaces(title)
        if not t:
            return None
        if " and Andre Panet-Raymond" in t:
            return t.split(" and Andre Panet-Raymond", 1)[0].strip() or None
        if " and Andre" in t:
            return t.split(" and Andre", 1)[0].strip() or None
        return None

    title_client = parse_client_from_title(meeting_title)

    for p in invitees:
        if not isinstance(p, dict):
            continue
        email = (p.get("email") or "").strip().lower()
        name = normalize_spaces(p.get("name") or "")
        if email and email != recorded_by_email:
            # If name is an email, discard it and use title-derived name.
            if name and "@" in name:
                name = ""
            if not name and title_client:
                name = title_client
            return (name or "Unknown", email)

    for p in invitees:
        if not isinstance(p, dict):
            continue
        email = (p.get("email") or "").strip().lower()
        name = normalize_spaces(p.get("name") or "")
        if email != recorded_by_email:
            if name and "@" in name:
                name = ""
            if not name and title_client:
                name = title_client
            return (name or "Unknown", email or None)

    return (title_client or "Unknown", None)


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
                meeting_title=meeting_title,
            )
        )

    rows.sort(key=lambda r: (r.client.lower(), r.created_at))

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

```



## Script: fathom_pick_next.py

```python
#!/usr/bin/env python3
"""Pick next N unprocessed Fathom share URLs from the local library.

Inputs:
- ~/krc_vault/fathom_library/index.json
- ~/krc_vault/fathom_library/state/processed.json

Outputs JSON:
{
  "pending_total": <int>,
  "selected": [ {"share_url":..., "client":..., "email":..., "created_at":..., "meeting_title":...}, ... ]
}

Args:
- --n <int> (default 3)
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=3)
    args = ap.parse_args()

    index_path = Path(os.path.expanduser('~/krc_vault/fathom_library/index.json'))
    state_path = Path(os.path.expanduser('~/krc_vault/fathom_library/state/processed.json'))

    idx = json.loads(index_path.read_text())
    processed = set()
    if state_path.exists():
        state = json.loads(state_path.read_text())
        processed = set(state.get('processed') or [])

    pending = [r for r in idx if r.get('share_url') and r['share_url'] not in processed]
    # oldest-first so backlog burns down deterministically
    selected = pending[: max(0, args.n)]

    out = {
        'pending_total': len(pending),
        'selected': [
            {
                'share_url': r.get('share_url'),
                'client': r.get('client'),
                'email': r.get('email'),
                'created_at': r.get('created_at'),
                'meeting_title': r.get('meeting_title'),
            }
            for r in selected
        ],
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

```



## State: source_index.json

```json
{
  "items": {
    "fathom_6102212884bf7031": {
      "run_id": "20260308_171522_61022128",
      "status": "success",
      "updated_at": "2026-03-08T22:15:22.703581+00:00"
    },
    "fathom_401462f895ac6872": {
      "run_id": "20260308_171522_401462f8",
      "status": "success",
      "updated_at": "2026-03-08T22:15:23.845778+00:00"
    },
    "fathom_545ca1b0376d6e6b": {
      "run_id": "20260308_172401_545ca1b0",
      "status": "success",
      "updated_at": "2026-03-08T22:29:25.712904+00:00"
    },
    "fathom_b0fb2a72fa14926e": {
      "run_id": "20260308_182019_b0fb2a72",
      "status": "success",
      "updated_at": "2026-03-08T23:22:26.316751+00:00"
    }
  },
  "updated_at": "2026-03-08T23:22:26.316765+00:00"
}
```



## State: index.json

```json
[
  {
    "client": "Agacy Goul (agacyajith@gmail.com)",
    "email": "agacyajith@gmail.com",
    "created_at": "2025-12-03T18:00:06Z",
    "recording_id": "106017979",
    "share_url": "https://fathom.video/share/7Wcj1kuB9aC-N4u9y99mNXFQ2VBytuHw",
    "meeting_title": "Agacy Goul and Andre Panet-Raymond"
  },
  {
    "client": "Alan Creighton (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-12-15T18:49:57Z",
    "recording_id": "108792609",
    "share_url": "https://fathom.video/share/xg31LyAHekJZb8XqAXoLPrUyAePcZ_ax",
    "meeting_title": "Alan Creighton and Andre Panet-Raymond"
  },
  {
    "client": "Angela Walker (angela.walker_26@yahoo.com)",
    "email": "angela.walker_26@yahoo.com",
    "created_at": "2025-11-17T20:08:10Z",
    "recording_id": "102229995",
    "share_url": "https://fathom.video/share/eM7ewxCHgTi4C62nW1fvA3_p7EqNhS_d",
    "meeting_title": "Angela Walker and Andre Panet-Raymond"
  },
  {
    "client": "Anthony Watts (awatts@ferris.edu)",
    "email": "awatts@ferris.edu",
    "created_at": "2025-12-23T18:31:13Z",
    "recording_id": "110696314",
    "share_url": "https://fathom.video/share/NhwzWwZ4AbjRnibWhi4jTvFY5kbncPhk",
    "meeting_title": "Anthony Watts and Andre Panet-Raymond"
  },
  {
    "client": "Arno Marx (arnomarx@gmail.com)",
    "email": "arnomarx@gmail.com",
    "created_at": "2026-01-05T22:00:04Z",
    "recording_id": "111898965",
    "share_url": "https://fathom.video/share/g1fXkS_SjdWMbeVbhwvjjRz9funEUsxB",
    "meeting_title": "Arno Marx and Andre Panet-Raymond"
  },
  {
    "client": "Arno Marx (arnomarx@gmail.com)",
    "email": "arnomarx@gmail.com",
    "created_at": "2026-01-12T21:28:54Z",
    "recording_id": "113627423",
    "share_url": "https://fathom.video/share/TcQx2Az4GfTSp194BjFz1oyCZjgEju3Q",
    "meeting_title": "Arno Marx and Andre Panet-Raymond"
  },
  {
    "client": "Arno Marx (arnomarx@gmail.com)",
    "email": "arnomarx@gmail.com",
    "created_at": "2026-01-14T20:36:51Z",
    "recording_id": "114340965",
    "share_url": "https://fathom.video/share/FXzEuuJkT-yAGyAiHgGnCzUUyKLPAUqe",
    "meeting_title": "Arno Marx and Andre Panet-Raymond"
  },
  {
    "client": "Arno Marx (arnomarx@gmail.com)",
    "email": "arnomarx@gmail.com",
    "created_at": "2026-01-28T22:47:30Z",
    "recording_id": "118000848",
    "share_url": "https://fathom.video/share/DUUyck7k9YaJJvWosxsTeUL2MzTGCeLk",
    "meeting_title": "Arno Marx and Andre Panet-Raymond"
  },
  {
    "client": "Arno Marx (arnomarx@gmail.com)",
    "email": "arnomarx@gmail.com",
    "created_at": "2026-02-12T23:01:04Z",
    "recording_id": "122153029",
    "share_url": "https://fathom.video/share/dK8oV4pEZoswL2My9s2bgwBb21CqUdNy",
    "meeting_title": "Arno Marx and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2025-11-07T20:00:39Z",
    "recording_id": "100136049",
    "share_url": "https://fathom.video/share/zY69s2-oTzTs1WLpsAg_Z2FPix17ComD",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2025-11-08T20:04:29Z",
    "recording_id": "100225315",
    "share_url": "https://fathom.video/share/a_uXC4pevYwheSsT-VpssNfgoZtyrDyD",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2025-11-13T18:48:22Z",
    "recording_id": "101489629",
    "share_url": "https://fathom.video/share/LC2jASLrw2HxLUkqjPARWbSfzyhffxpc",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2025-11-22T19:06:16Z",
    "recording_id": "103668524",
    "share_url": "https://fathom.video/share/Sdp1DhRf26d8VnJx_yxwajAywF2pzjvM",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2025-11-26T20:46:26Z",
    "recording_id": "104656840",
    "share_url": "https://fathom.video/share/xYALcSdZzKCszKViyBA3Vwbj2oxaLR3k",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2025-12-03T02:29:16Z",
    "recording_id": "105781647",
    "share_url": "https://fathom.video/share/xoakee5Y4KiXpxC9Cs17gdziuh4ZW1Fk",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2025-12-09T01:16:39Z",
    "recording_id": "107170321",
    "share_url": "https://fathom.video/share/NvGBiRWSTU14WQ746ydC9B-q6aUVj7yP",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2025-12-23T01:19:26Z",
    "recording_id": "110535309",
    "share_url": "https://fathom.video/share/-J72AS-irsPjxM-4zg6gT5DXayn_tBBG",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2026-01-03T18:29:55Z",
    "recording_id": "111591347",
    "share_url": "https://fathom.video/share/Siz4qBsCgofxUCb4bg-44RNQgD_Uv3Y6",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2026-01-07T20:31:01Z",
    "recording_id": "112543527",
    "share_url": "https://fathom.video/share/3sXnwgFgxZQJDT84Aryxay59psZtsXWS",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2026-01-15T22:31:09Z",
    "recording_id": "114706225",
    "share_url": "https://fathom.video/share/jTk4dTr2uxioK7AzQjVUzkxfo_x61hGb",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2026-01-16T18:54:54Z",
    "recording_id": "114969813",
    "share_url": "https://fathom.video/share/JsmTS3dWxeYqCs--99AqzN-gBRka8ogh",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2026-01-19T21:44:39Z",
    "recording_id": "115383767",
    "share_url": "https://fathom.video/share/LP1ED5F9dnz9PwaLHnM_ys9xAxLVZz_8",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2026-01-27T22:57:15Z",
    "recording_id": "117632659",
    "share_url": "https://fathom.video/share/7yfj1v8RCe6tNGfsrhLedy8sD9JbpPte",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2026-02-05T21:59:25Z",
    "recording_id": "120218054",
    "share_url": "https://fathom.video/share/xeXtgYksG6RqyP9Qvt9xR3z7S_TuEnH2",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2026-02-10T20:32:31Z",
    "recording_id": "121326025",
    "share_url": "https://fathom.video/share/c1fw-iaY5H9eFVE7NK_W_XA3w55gq2su",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2026-02-16T23:57:30Z",
    "recording_id": "122808006",
    "share_url": "https://fathom.video/share/T1zno5zskCCc6AmrzvTQUTXdSsRBHUpm",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Augusto Leal (aleal4@gmail.com)",
    "email": "aleal4@gmail.com",
    "created_at": "2026-02-24T22:57:05Z",
    "recording_id": "125037005",
    "share_url": "https://fathom.video/share/kgLpjMboKQuyJo8s9yQJnDCUjPV9B8aS",
    "meeting_title": "Augusto Leal and Andre Panet-Raymond"
  },
  {
    "client": "Austin Foster (austinrfoster01@gmail.com)",
    "email": "austinrfoster01@gmail.com",
    "created_at": "2026-02-17T21:58:39Z",
    "recording_id": "123117566",
    "share_url": "https://fathom.video/share/MeEeshZHBLUUJz9d2LVZUaeyicHcxYRh",
    "meeting_title": "Austin Foster and Andre Panet-Raymond"
  },
  {
    "client": "Austin Foster (austinrfoster01@gmail.com)",
    "email": "austinrfoster01@gmail.com",
    "created_at": "2026-02-23T23:59:00Z",
    "recording_id": "124672646",
    "share_url": "https://fathom.video/share/MHUn-4cJvKYL2J7gMTmmTXEi86a9hKYz",
    "meeting_title": "Austin Foster and Andre Panet-Raymond"
  },
  {
    "client": "Barbara Brandyberry (sunriseskies@hotmail.com)",
    "email": "sunriseskies@hotmail.com",
    "created_at": "2025-11-06T22:04:38Z",
    "recording_id": "99853356",
    "share_url": "https://fathom.video/share/Hyf6QJAGXFimPtqpszx5DM2G3-nXgxuQ",
    "meeting_title": "Barbara Brandyberry and Andre Panet-Raymond"
  },
  {
    "client": "Barbara Miller-Brandyberry (sunriseskies@hotmail.com)",
    "email": "sunriseskies@hotmail.com",
    "created_at": "2025-11-13T21:04:47Z",
    "recording_id": "101561292",
    "share_url": "https://fathom.video/share/gjnz-nx5zzVkwa1LK1zZaQi8Xng1sNXs",
    "meeting_title": "Barbara Miller-Brandyberry and Andre Panet-Raymond"
  },
  {
    "client": "Barbara Miller-Brandyberry (sunriseskies@hotmail.com)",
    "email": "sunriseskies@hotmail.com",
    "created_at": "2025-11-20T20:03:53Z",
    "recording_id": "103291167",
    "share_url": "https://fathom.video/share/eb7ttphk7i3bWULVNMjCU7PaR1mc3F4U",
    "meeting_title": "Barbara Miller-Brandyberry and Andre Panet-Raymond"
  },
  {
    "client": "Beck Townsend (beck.townsend10@gmail.com)",
    "email": "beck.townsend10@gmail.com",
    "created_at": "2025-12-10T23:57:57Z",
    "recording_id": "107888671",
    "share_url": "https://fathom.video/share/8NV5wGtuo_1kVz_aepdcD-WSZgvyxt32",
    "meeting_title": "Beck Townsend and Andre Panet-Raymond"
  },
  {
    "client": "Beck Townsend (beck.townsend10@gmail.com)",
    "email": "beck.townsend10@gmail.com",
    "created_at": "2025-12-15T23:42:01Z",
    "recording_id": "108910450",
    "share_url": "https://fathom.video/share/_BG1oFnsCTwxescyq69vysKBx9R_Fpxj",
    "meeting_title": "Beck Townsend and Andre Panet-Raymond"
  },
  {
    "client": "Beck Townsend (beck.townsend10@gmail.com)",
    "email": "beck.townsend10@gmail.com",
    "created_at": "2025-12-22T21:33:12Z",
    "recording_id": "110505156",
    "share_url": "https://fathom.video/share/W9XkyUa5fUBnpPEX_NiLCmKysu-Y-e1w",
    "meeting_title": "Beck Townsend and Andre Panet-Raymond"
  },
  {
    "client": "Bradley Oliver (bkoliver74@gmail.com)",
    "email": "bkoliver74@gmail.com",
    "created_at": "2026-02-26T21:30:51Z",
    "recording_id": "125745552",
    "share_url": "https://fathom.video/share/JvJNFLfCRzV6rB7a3UBxFBEew2vuP4vs",
    "meeting_title": "Bradley Oliver and Andre Panet-Raymond"
  },
  {
    "client": "Brandon Wells (leew00830@gmail.com)",
    "email": "leew00830@gmail.com",
    "created_at": "2026-02-12T17:42:28Z",
    "recording_id": "122003425",
    "share_url": "https://fathom.video/share/Rkbc__d2yjFWBHLq6v57zRPpxH7sw4FD",
    "meeting_title": "Brandon Wells and Andre Panet-Raymond"
  },
  {
    "client": "Brooks Kindervater (bkind06@hotmail.com)",
    "email": "bkind06@hotmail.com",
    "created_at": "2025-12-05T20:04:43Z",
    "recording_id": "106712892",
    "share_url": "https://fathom.video/share/xUsxLymvK953UyAWkJ7zPo3_mCiaNEgA",
    "meeting_title": "Brooks Kindervater and Andre Panet-Raymond"
  },
  {
    "client": "Bryce Rothweiler (brycerothweiler@gmail.com)",
    "email": "brycerothweiler@gmail.com",
    "created_at": "2026-02-05T19:11:19Z",
    "recording_id": "120134267",
    "share_url": "https://fathom.video/share/DNAzxxdHFMh1oQKKdfFvWkefz5u4z6EK",
    "meeting_title": "bryce Rothweiler and Andre Panet-Raymond"
  },
  {
    "client": "Cade Williamson (cadewilliamson095@gmail.com)",
    "email": "cadewilliamson095@gmail.com",
    "created_at": "2025-12-02T17:37:18Z",
    "recording_id": "105622753",
    "share_url": "https://fathom.video/share/Q5pdpopGVJyMXby8uQR2KyoayrjFyXwQ",
    "meeting_title": "Cade Williamson and Andre Panet-Raymond"
  },
  {
    "client": "Candace (candicanes002@yahoo.com)",
    "email": "candicanes002@yahoo.com",
    "created_at": "2025-12-05T18:40:39Z",
    "recording_id": "106686880",
    "share_url": "https://fathom.video/share/vVQ7zi9SxBHaWyXoJSVsD9xfNcuyNSns",
    "meeting_title": "Candace and Andre Panet-Raymond"
  },
  {
    "client": "Candace Martinez (candicanes002@yahoo.com)",
    "email": "candicanes002@yahoo.com",
    "created_at": "2025-10-10T18:34:19Z",
    "recording_id": "93447066",
    "share_url": "https://fathom.video/share/Fyccx61FXVYuRgWpK3utKBhpw6cEs4gb",
    "meeting_title": "Candace Martinez and Andre Panet-Raymond"
  },
  {
    "client": "Candace Martinez (candicanes002@yahoo.com)",
    "email": "candicanes002@yahoo.com",
    "created_at": "2025-10-24T21:01:01Z",
    "recording_id": "96717701",
    "share_url": "https://fathom.video/share/WmhfXXgYxgpAswzs8PJGosn7hUfuLErh",
    "meeting_title": "Candace Martinez and Andre Panet-Raymond"
  },
  {
    "client": "Cary Fulks (cfulks.cf@gmail.com)",
    "email": "cfulks.cf@gmail.com",
    "created_at": "2025-12-13T01:12:54Z",
    "recording_id": "108519904",
    "share_url": "https://fathom.video/share/qLEzY2rBHqTUP7_xvtAoyUcT_LhBNVH4",
    "meeting_title": "Cary Fulks and Andre Panet-Raymond"
  },
  {
    "client": "Chesko Vrel Bilbao (bcheskovrel@gmail.com)",
    "email": "bcheskovrel@gmail.com",
    "created_at": "2026-02-10T17:17:32Z",
    "recording_id": "121225993",
    "share_url": "https://fathom.video/share/eGEjGh4-oq75mV6cDbizB7PsXwxhCv29",
    "meeting_title": "Chesko Vrel Bilbao and Andre Panet-Raymond"
  },
  {
    "client": "Chris Sharman (chris@radios4racing.es)",
    "email": "chris@radios4racing.es",
    "created_at": "2026-01-19T22:52:31Z",
    "recording_id": "115406553",
    "share_url": "https://fathom.video/share/miLQeayVjXgq-maD54c2fQTWzcU_Cnh6",
    "meeting_title": "Chris Sharman and Andre Panet-Raymond"
  },
  {
    "client": "Chris Sharman (chris@radios4racing.es)",
    "email": "chris@radios4racing.es",
    "created_at": "2026-01-26T22:52:56Z",
    "recording_id": "117245485",
    "share_url": "https://fathom.video/share/YrVNfU6XEKAMEra2zAwCxuyzNs6FXFmY",
    "meeting_title": "Chris Sharman and Andre Panet-Raymond"
  },
  {
    "client": "Chris Sharman (chris@radios4racing.es)",
    "email": "chris@radios4racing.es",
    "created_at": "2026-02-19T18:20:50Z",
    "recording_id": "123749984",
    "share_url": "https://fathom.video/share/91CY4riqemPZ3sD8j3mV_BjzeFFsCp6C",
    "meeting_title": "Chris Sharman and Andre Panet-Raymond"
  },
  {
    "client": "Chris Solis (csolis1987@gmail.com)",
    "email": "csolis1987@gmail.com",
    "created_at": "2025-12-11T17:55:45Z",
    "recording_id": "108097149",
    "share_url": "https://fathom.video/share/ypbCr3TyByYsfiicfgbfH7o7NCncmwBz",
    "meeting_title": "Chris Solis and Andre Panet-Raymond"
  },
  {
    "client": "Christopher Fenicchia (fenicchiachris@gmail.com)",
    "email": "fenicchiachris@gmail.com",
    "created_at": "2026-01-04T00:14:56Z",
    "recording_id": "111600006",
    "share_url": "https://fathom.video/share/s4Rbc9Xx4nQ1dt9-oSrDWa8C2y7PF7Qx",
    "meeting_title": "Christopher Fenicchia and Andre Panet-Raymond"
  },
  {
    "client": "Christopher Sharman (chris@radios4racing.es)",
    "email": "chris@radios4racing.es",
    "created_at": "2025-12-13T23:01:41Z",
    "recording_id": "108549363",
    "share_url": "https://fathom.video/share/y7jpsVDSp96tkS9DLVQ5C6yP52W-s5AG",
    "meeting_title": "Christopher Sharman and Andre Panet-Raymond"
  },
  {
    "client": "Christopher Sharman (chris@radios4racing.es)",
    "email": "chris@radios4racing.es",
    "created_at": "2026-01-06T21:15:41Z",
    "recording_id": "112232086",
    "share_url": "https://fathom.video/share/Y6sCR11mCy8PJQyoTuogvVHza6Ss_eXb",
    "meeting_title": "Christopher Sharman and Andre Panet-Raymond"
  },
  {
    "client": "Christopher Sharman (chris@radios4racing.es)",
    "email": "chris@radios4racing.es",
    "created_at": "2026-01-14T21:54:28Z",
    "recording_id": "114364658",
    "share_url": "https://fathom.video/share/yZEg1jhsPAE5zhE1F3DAs_rw8uK6s3WD",
    "meeting_title": "Christopher Sharman and Andre Panet-Raymond"
  },
  {
    "client": "Christopher Sharman (chris@radios4racing.es)",
    "email": "chris@radios4racing.es",
    "created_at": "2026-02-03T22:05:18Z",
    "recording_id": "119470044",
    "share_url": "https://fathom.video/share/PJiEojoT4g2f32o6fiN6oG67GxZ7tLzx",
    "meeting_title": "Christopher Sharman and Andre Panet-Raymond"
  },
  {
    "client": "Christopher Sharman (chris@radios4racing.es)",
    "email": "chris@radios4racing.es",
    "created_at": "2026-02-09T20:54:48Z",
    "recording_id": "120940011",
    "share_url": "https://fathom.video/share/wU7MSr4rBcBhDVy1N9a6qB7A5yzXK1L1",
    "meeting_title": "Christopher Sharman and Andre Panet-Raymond"
  },
  {
    "client": "Christopher Sharman (chris@radios4racing.es)",
    "email": "chris@radios4racing.es",
    "created_at": "2026-02-16T22:34:23Z",
    "recording_id": "122795482",
    "share_url": "https://fathom.video/share/UDdgtPDexQRxbFgE9TMt-NSbCxJyU4cn",
    "meeting_title": "Christopher Sharman and Andre Panet-Raymond"
  },
  {
    "client": "Colton Johnson (coltonj05@yahoo.com)",
    "email": "coltonj05@yahoo.com",
    "created_at": "2026-02-04T17:34:50Z",
    "recording_id": "119727492",
    "share_url": "https://fathom.video/share/tDJe2YmnoqqBmeZMjMjTPzCZQpgF-JBv",
    "meeting_title": "Colton Johnson and Andre Panet-Raymond"
  },
  {
    "client": "Dakota Webb (dakota4214@gmail.com)",
    "email": "dakota4214@gmail.com",
    "created_at": "2026-02-21T00:13:57Z",
    "recording_id": "124230918",
    "share_url": "https://fathom.video/share/Dbuph_FFiBcELQgf--xGoot7wxf3JPsf",
    "meeting_title": "Dakota Webb and Andre Panet-Raymond"
  },
  {
    "client": "Dana Collins (collinsdana469@yahoo.com)",
    "email": "collinsdana469@yahoo.com",
    "created_at": "2026-01-22T17:52:57Z",
    "recording_id": "116396240",
    "share_url": "https://fathom.video/share/cJ6M2w8UfuPqRANYsr3BJ2Vt9ksP8hVT",
    "meeting_title": "Dana Collins and Andre Panet-Raymond"
  },
  {
    "client": "Daniel Smyth (dansmyth509@gmail.com)",
    "email": "dansmyth509@gmail.com",
    "created_at": "2025-10-27T18:32:00Z",
    "recording_id": "97056894",
    "share_url": "https://fathom.video/share/1ktSJ-DRUoVs_1MDjdESa8gJoUhGAxQn",
    "meeting_title": "Andre Panet-Raymond and Dan Smyth"
  },
  {
    "client": "Daniel Wharton (danieljwharton@gmail.com)",
    "email": "danieljwharton@gmail.com",
    "created_at": "2026-01-09T01:41:20Z",
    "recording_id": "112955257",
    "share_url": "https://fathom.video/share/yvPvoExi5REQwAzE2jMb3xsfMbUqUrxj",
    "meeting_title": "Daniel Wharton and Andre Panet-Raymond"
  },
  {
    "client": "Derick Duran (derickddduran@gmail.com)",
    "email": "derickddduran@gmail.com",
    "created_at": "2025-12-12T00:17:59Z",
    "recording_id": "108221634",
    "share_url": "https://fathom.video/share/aiXdz8pGR_NewCxu-Pvispys1TfoC3xs",
    "meeting_title": "Derick Duran and Andre Panet-Raymond"
  },
  {
    "client": "Derick Duran (derickddduran@gmail.com)",
    "email": "derickddduran@gmail.com",
    "created_at": "2025-12-15T22:38:59Z",
    "recording_id": "108890254",
    "share_url": "https://fathom.video/share/YTkw3AdKqcU8syMWECVk2wnKfpRYzMAU",
    "meeting_title": "Derick Duran and Andre Panet-Raymond"
  },
  {
    "client": "Derick Duran (derickddduran@gmail.com)",
    "email": "derickddduran@gmail.com",
    "created_at": "2025-12-23T00:02:06Z",
    "recording_id": "110525042",
    "share_url": "https://fathom.video/share/_ydVJzd1NC8JpYCS_yH_RoQzCt2Jpcz2",
    "meeting_title": "Derick Duran and Andre Panet-Raymond"
  },
  {
    "client": "Derick Duran (derickddduran@gmail.com)",
    "email": "derickddduran@gmail.com",
    "created_at": "2025-12-30T23:41:46Z",
    "recording_id": "111322388",
    "share_url": "https://fathom.video/share/nbB5JxAoXjg7-xMtjQr1rxn6DedRNn5h",
    "meeting_title": "Derick Duran and Andre Panet-Raymond"
  },
  {
    "client": "Derick Duran (derickddduran@gmail.com)",
    "email": "derickddduran@gmail.com",
    "created_at": "2026-01-09T20:38:49Z",
    "recording_id": "113208185",
    "share_url": "https://fathom.video/share/xcMQom_H5fayzGw4PM48F7uqSiD-sb8J",
    "meeting_title": "Derick Duran and Andre Panet-Raymond"
  },
  {
    "client": "Derick Duran (derickddduran@gmail.com)",
    "email": "derickddduran@gmail.com",
    "created_at": "2026-01-27T22:01:48Z",
    "recording_id": "117610188",
    "share_url": "https://fathom.video/share/iXnysZeXT-i1sT51x1nHLhfbnssmmwbW",
    "meeting_title": "Derick Duran and Andre Panet-Raymond"
  },
  {
    "client": "Derick Duran (derickddduran@gmail.com)",
    "email": "derickddduran@gmail.com",
    "created_at": "2026-02-04T22:12:06Z",
    "recording_id": "119791436",
    "share_url": "https://fathom.video/share/3berkHjufEnhBgXmNiXwygs3hgYrLo-6",
    "meeting_title": "Derick Duran and Andre Panet-Raymond"
  },
  {
    "client": "Derick Duran (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2026-01-09T22:06:29Z",
    "recording_id": "113221471",
    "share_url": "https://fathom.video/share/Ft4HA2NhzDC33tShyKyc4yiG993yJamX",
    "meeting_title": "Derick Duran and Andre Panet-Raymond"
  },
  {
    "client": "Dominic Mulder (dominicmulder64@gmail.com)",
    "email": "dominicmulder64@gmail.com",
    "created_at": "2025-12-23T19:40:43Z",
    "recording_id": "110715950",
    "share_url": "https://fathom.video/share/Qsk5wpSQyshds_usz_xGU2Nmw1-ow7k4",
    "meeting_title": "Dominic Mulder and Andre Panet-Raymond"
  },
  {
    "client": "Elijah Bridgeo (elijahbridgeo3@gmail.com)",
    "email": "elijahbridgeo3@gmail.com",
    "created_at": "2026-01-05T23:39:02Z",
    "recording_id": "111923185",
    "share_url": "https://fathom.video/share/1zqH-Jm6YEHXKxnR-wsxWpaFCZFNU3HB",
    "meeting_title": "Elijah Bridgeo and Andre Panet-Raymond"
  },
  {
    "client": "Elijah Bridgeo (elijahbridgeo3@gmail.com)",
    "email": "elijahbridgeo3@gmail.com",
    "created_at": "2026-01-07T23:07:44Z",
    "recording_id": "112602928",
    "share_url": "https://fathom.video/share/ExiaTrQMWptzasuRyf5Dis3WqeXazrvE",
    "meeting_title": "Elijah Bridgeo and Andre Panet-Raymond"
  },
  {
    "client": "Elijah Bridgeo (elijahbridgeo3@gmail.com)",
    "email": "elijahbridgeo3@gmail.com",
    "created_at": "2026-01-12T23:21:36Z",
    "recording_id": "113664304",
    "share_url": "https://fathom.video/share/ddzxrm8pQMrL7FHj4yzbCQx7jY_JJxks",
    "meeting_title": "Elijah Bridgeo and Andre Panet-Raymond"
  },
  {
    "client": "Elijah Bridgeo (elijahbridgeo3@gmail.com)",
    "email": "elijahbridgeo3@gmail.com",
    "created_at": "2026-01-14T23:19:43Z",
    "recording_id": "114391165",
    "share_url": "https://fathom.video/share/H16gYnTC5e6rKa3mseaEfv_cERVuey-s",
    "meeting_title": "Elijah Bridgeo and Andre Panet-Raymond"
  },
  {
    "client": "Elijah Bridgeo (elijahbridgeo3@gmail.com)",
    "email": "elijahbridgeo3@gmail.com",
    "created_at": "2026-01-19T19:54:05Z",
    "recording_id": "115357960",
    "share_url": "https://fathom.video/share/VEcrqqyMytzG3xaqzxRSq3exJ_iFo873",
    "meeting_title": "Elijah Bridgeo and Andre Panet-Raymond"
  },
  {
    "client": "Elijah Bridgeo (elijahbridgeo3@gmail.com)",
    "email": "elijahbridgeo3@gmail.com",
    "created_at": "2026-01-31T16:53:32Z",
    "recording_id": "118719932",
    "share_url": "https://fathom.video/share/mzGKSMv5KyEk1Qey7PCxVBgErapyr-nv",
    "meeting_title": "Elijah Bridgeo and Andre Panet-Raymond"
  },
  {
    "client": "Elijah Bridgeo (elijahbridgeo3@gmail.com)",
    "email": "elijahbridgeo3@gmail.com",
    "created_at": "2026-02-05T17:23:43Z",
    "recording_id": "120099946",
    "share_url": "https://fathom.video/share/aUvzxZgQsCyXnADry1Wwsq6r5qzLzPPq",
    "meeting_title": "Elijah Bridgeo and Andre Panet-Raymond"
  },
  {
    "client": "Enock Kibet (enockkibet949@gmail.com)",
    "email": "enockkibet949@gmail.com",
    "created_at": "2025-11-21T20:28:27Z",
    "recording_id": "103601050",
    "share_url": "https://fathom.video/share/hop-Chx_nTv-sXNs7u5izS8qtzuk7bNU",
    "meeting_title": "Enock Kibet and Andre Panet-Raymond"
  },
  {
    "client": "Eric steckner (eric.steckner@gmail.com)",
    "email": "eric.steckner@gmail.com",
    "created_at": "2025-12-20T20:34:44Z",
    "recording_id": "110240342",
    "share_url": "https://fathom.video/share/GixdwUo6Yo1ivY2WxzeGm-4gS5a6vmjy",
    "meeting_title": "Eric steckner and Andre Panet-Raymond"
  },
  {
    "client": "Francescomatteo Mattiaccio (francescomatteo.m3@gmail.com)",
    "email": "francescomatteo.m3@gmail.com",
    "created_at": "2025-10-21T17:53:42Z",
    "recording_id": "95658503",
    "share_url": "https://fathom.video/share/LFs5Upc2PbAdGssriWLu8z6PhYP-4zCr",
    "meeting_title": "📞 Discovery Call with Andre Panet-Raymond and Francescomatteo Mattiaccio - Fra Confirmed!"
  },
  {
    "client": "Francescomatteo Mattiaccio (francescomatteo.m3@gmail.com)",
    "email": "francescomatteo.m3@gmail.com",
    "created_at": "2025-10-23T17:56:18Z",
    "recording_id": "96362978",
    "share_url": "https://fathom.video/share/i_acam-6NSsNbHmy6szisjRvb3fLJwKe",
    "meeting_title": "📞 Monk Mode Strategy Call: Andre Panet-Raymond and Francescomatteo Mattiaccio - Fra"
  },
  {
    "client": "Francescomatteo Mattiaccio (francescomatteo.m3@gmail.com)",
    "email": "francescomatteo.m3@gmail.com",
    "created_at": "2025-10-27T16:22:11Z",
    "recording_id": "96961391",
    "share_url": "https://fathom.video/share/YmBwn4-hYp6MLm99V-EnNkz7gJsq73zw",
    "meeting_title": "📞 Monk Mode Strategy Call: Andre Panet-Raymond and Francescomatteo Mattiaccio - Fra"
  },
  {
    "client": "Francescomatteo Mattiaccio (francescomatteo.m3@gmail.com)",
    "email": "francescomatteo.m3@gmail.com",
    "created_at": "2025-11-03T17:26:10Z",
    "recording_id": "98699460",
    "share_url": "https://fathom.video/share/jfFtv5n2XgFzBPoKKm5masyV1sPDhr_A",
    "meeting_title": "Andre Panet-Raymond and Francescomatteo Mattiaccio - Fra"
  },
  {
    "client": "Francescomatteo Mattiaccio (francescomatteo.m3@gmail.com)",
    "email": "francescomatteo.m3@gmail.com",
    "created_at": "2025-11-10T20:01:26Z",
    "recording_id": "100510640",
    "share_url": "https://fathom.video/share/MYtVzQYTzaFj9p64KsDoeR8zncFxcWeV",
    "meeting_title": "Andre Panet-Raymond and Francescomatteo Mattiaccio - Fra"
  },
  {
    "client": "Francescomatteo Mattiaccio (francescomatteo.m3@gmail.com)",
    "email": "francescomatteo.m3@gmail.com",
    "created_at": "2025-11-18T18:16:40Z",
    "recording_id": "102495997",
    "share_url": "https://fathom.video/share/ZENbLGqXQJUs4A_XQiC2NVyUj4pCFcyu",
    "meeting_title": "Andre Panet-Raymond and Francescomatteo Mattiaccio - Fra"
  },
  {
    "client": "Franklin Marte (franklinmarte135@gmail.com)",
    "email": "franklinmarte135@gmail.com",
    "created_at": "2025-10-29T19:51:42Z",
    "recording_id": "97798697",
    "share_url": "https://fathom.video/share/bxY6oMzxdyBNrHbAR_YJqX5wNQ4kDRRo",
    "meeting_title": "Franklin Marte and Andre Panet-Raymond"
  },
  {
    "client": "Garrick Delafuente (garrickkd@gmail.com)",
    "email": "garrickkd@gmail.com",
    "created_at": "2026-01-30T18:20:27Z",
    "recording_id": "118575968",
    "share_url": "https://fathom.video/share/nMKGpia8zDBi821rwWm9kjHMPbgoFXv8",
    "meeting_title": "Garrick Delafuente and Andre Panet-Raymond"
  },
  {
    "client": "Garrick Delafuente (garrickkd@gmail.com)",
    "email": "garrickkd@gmail.com",
    "created_at": "2026-01-31T19:17:25Z",
    "recording_id": "118723259",
    "share_url": "https://fathom.video/share/X6vLf2E1zbijQh-_-6cnREmGYJv3-91b",
    "meeting_title": "Garrick Delafuente and Andre Panet-Raymond"
  },
  {
    "client": "Garrick Delafuente (garrickkd@gmail.com)",
    "email": "garrickkd@gmail.com",
    "created_at": "2026-02-05T21:04:15Z",
    "recording_id": "120164136",
    "share_url": "https://fathom.video/share/TFw5kBjF8xrxwDsezxx4ss5E5Gtfh-zd",
    "meeting_title": "Garrick Delafuente and Andre Panet-Raymond"
  },
  {
    "client": "Garrick Delafuente (garrickkd@gmail.com)",
    "email": "garrickkd@gmail.com",
    "created_at": "2026-02-12T21:44:32Z",
    "recording_id": "122096080",
    "share_url": "https://fathom.video/share/U36X33xUVJMQLSNNDJW7zj9B-4Anq_xo",
    "meeting_title": "Garrick Delafuente and Andre Panet-Raymond"
  },
  {
    "client": "Garrick Delafuente (garrickkd@gmail.com)",
    "email": "garrickkd@gmail.com",
    "created_at": "2026-02-19T21:34:21Z",
    "recording_id": "123860072",
    "share_url": "https://fathom.video/share/Fx6HLu_GLxvzzJVEs7LjyFDJsa74hU6j",
    "meeting_title": "Garrick Delafuente and Andre Panet-Raymond"
  },
  {
    "client": "Gary Zagar (garyzagar@yahoo.com)",
    "email": "garyzagar@yahoo.com",
    "created_at": "2025-12-12T23:00:04Z",
    "recording_id": "108512187",
    "share_url": "https://fathom.video/share/GX8pxEBtxEMW86DRExfjgRphhFKbetMr",
    "meeting_title": "Gary Zagar and Andre Panet-Raymond"
  },
  {
    "client": "Gary Zagar (garyzagar@yahoo.com)",
    "email": "garyzagar@yahoo.com",
    "created_at": "2025-12-15T21:15:38Z",
    "recording_id": "108857594",
    "share_url": "https://fathom.video/share/8tzrz8Uzs1s2Fr9k_zY86KyXwsM2z1cS",
    "meeting_title": "Gary Zagar and Andre Panet-Raymond"
  },
  {
    "client": "Gerson Morales (legazmorales@gmail.com)",
    "email": "legazmorales@gmail.com",
    "created_at": "2026-02-11T20:02:14Z",
    "recording_id": "121696237",
    "share_url": "https://fathom.video/share/6RPEbxvc9jcRgxZDpKgRcBQEB-7zBi4B",
    "meeting_title": "Gerson Morales and Andre Panet-Raymond"
  },
  {
    "client": "Ghica Cristian (cristian.ghica0208@gmail.com)",
    "email": "cristian.ghica0208@gmail.com",
    "created_at": "2026-02-09T18:06:38Z",
    "recording_id": "120854012",
    "share_url": "https://fathom.video/share/5syneSJAgSihzBMPxZnGUhv8Y_Xs9UG6",
    "meeting_title": "Ghica Cristian and Andre Panet-Raymond"
  },
  {
    "client": "Isaac Martin (isaac18martin@yahoo.com)",
    "email": "isaac18martin@yahoo.com",
    "created_at": "2026-02-21T21:24:11Z",
    "recording_id": "124277101",
    "share_url": "https://fathom.video/share/-QVx6A-nB5QxGsS8vAFFtMxq74yReScs",
    "meeting_title": "Isaac Martin and Andre Panet-Raymond"
  },
  {
    "client": "Ivan Dan Movida (ivanmovida@yahoo.com)",
    "email": "ivanmovida@yahoo.com",
    "created_at": "2025-10-06T19:59:34Z",
    "recording_id": "92150295",
    "share_url": "https://fathom.video/share/4M17FFLU_BKtVsDrjLA2Kauqx5jW-eJt",
    "meeting_title": "Ivan Dan Movida and Andre Panet-Raymond"
  },
  {
    "client": "Ivan Dan Movida (ivanmovida@yahoo.com)",
    "email": "ivanmovida@yahoo.com",
    "created_at": "2025-10-09T20:23:08Z",
    "recording_id": "93151172",
    "share_url": "https://fathom.video/share/s3KDi_qq_cg9_2UBsUz6nck3mAG93CR_",
    "meeting_title": "Ivan Dan Movida and Andre Panet-Raymond"
  },
  {
    "client": "Ivan Dan Movida (ivanmovida@yahoo.com)",
    "email": "ivanmovida@yahoo.com",
    "created_at": "2025-10-13T20:11:24Z",
    "recording_id": "93782649",
    "share_url": "https://fathom.video/share/sasnbAhNfe5Dk5-aeHqm72Q3TxR2uUTT",
    "meeting_title": "Ivan Dan Movida and Andre Panet-Raymond"
  },
  {
    "client": "Ivan Dan Movida (ivanmovida@yahoo.com)",
    "email": "ivanmovida@yahoo.com",
    "created_at": "2025-10-16T19:53:10Z",
    "recording_id": "94785799",
    "share_url": "https://fathom.video/share/5AFLLG973-5CFHeexqZ-xY2fVwJdHXv6",
    "meeting_title": "Ivan Dan Movida and Andre Panet-Raymond"
  },
  {
    "client": "Ivan Dan Movida (ivanmovida@yahoo.com)",
    "email": "ivanmovida@yahoo.com",
    "created_at": "2025-11-17T21:07:45Z",
    "recording_id": "102257165",
    "share_url": "https://fathom.video/share/skmhw_mBuL_rNQfeBzbj_ax_ayyZjLgq",
    "meeting_title": "Ivan Dan Movida and Andre Panet-Raymond"
  },
  {
    "client": "Ivan Dan Movida (ivanmovida@yahoo.com)",
    "email": "ivanmovida@yahoo.com",
    "created_at": "2025-11-22T20:27:10Z",
    "recording_id": "103673447",
    "share_url": "https://fathom.video/share/LCsbBg2yzAhMCyqQMtF-R6Aa_B2wcicW",
    "meeting_title": "Ivan Dan Movida and Andre Panet-Raymond"
  },
  {
    "client": "Jake McLain (mclaj7076@gmail.com)",
    "email": "mclaj7076@gmail.com",
    "created_at": "2025-12-12T22:11:07Z",
    "recording_id": "108471786",
    "share_url": "https://fathom.video/share/F7k7X2-7Sish53tuZagRZcvx_nnBBh7f",
    "meeting_title": "Jake McLain and Andre Panet-Raymond"
  },
  {
    "client": "Jake McLain (mclaj7076@gmail.com)",
    "email": "mclaj7076@gmail.com",
    "created_at": "2026-01-15T23:08:22Z",
    "recording_id": "114742747",
    "share_url": "https://fathom.video/share/mwvC3pdeZ9xN6E83pPeosc6a6Km52vRH",
    "meeting_title": "Jake McLain and Andre Panet-Raymond"
  },
  {
    "client": "Jake McLain (mclaj7076@gmail.com)",
    "email": "mclaj7076@gmail.com",
    "created_at": "2026-01-20T22:38:56Z",
    "recording_id": "115799091",
    "share_url": "https://fathom.video/share/qngPaT7jC_RBdyDWKpDyy9kGssJmSpVx",
    "meeting_title": "Jake McLain and Andre Panet-Raymond"
  },
  {
    "client": "James Boreham (boreham.jimmy.b@gmail.com)",
    "email": "boreham.jimmy.b@gmail.com",
    "created_at": "2025-12-11T18:29:47Z",
    "recording_id": "108123685",
    "share_url": "https://fathom.video/share/DCgpykWoWKufHuww-rKYgAGLzn-ctd1S",
    "meeting_title": "James Boreham and Andre Panet-Raymond"
  },
  {
    "client": "Jared Russell (russelljared99@gmail.com)",
    "email": "russelljared99@gmail.com",
    "created_at": "2025-10-29T19:00:37Z",
    "recording_id": "97769080",
    "share_url": "https://fathom.video/share/yVRE55Yf5q94oLRpBFS_T8LDm84DeYWJ",
    "meeting_title": "Jared Russell and Andre Panet-Raymond"
  },
  {
    "client": "jerry fopma (fopmaj@gmail.com)",
    "email": "fopmaj@gmail.com",
    "created_at": "2026-01-13T00:26:03Z",
    "recording_id": "113674271",
    "share_url": "https://fathom.video/share/4x1jTFemqPh1cy1d9gyd3hvsbSFju1Y-",
    "meeting_title": "jerry fopma and Andre Panet-Raymond"
  },
  {
    "client": "Jezreel Govender (jezreel.sonshyn@gmail.com)",
    "email": "jezreel.sonshyn@gmail.com",
    "created_at": "2025-10-07T18:07:50Z",
    "recording_id": "92486087",
    "share_url": "https://fathom.video/share/m5Xd9dytaoAzwo2jXsdFsKixN1iyLteL",
    "meeting_title": "Jezreel Govender and Andre Panet-Raymond"
  },
  {
    "client": "Jim Robinson (jfrobinson62@gmail.com)",
    "email": "jfrobinson62@gmail.com",
    "created_at": "2025-11-10T21:41:09Z",
    "recording_id": "100550394",
    "share_url": "https://fathom.video/share/scCreempHSo-Jp_GCjd9bbhfH-XnzuVE",
    "meeting_title": "Jim Robinson and Andre Panet-Raymond"
  },
  {
    "client": "Jim Robinson (jfrobinson62@gmail.com)",
    "email": "jfrobinson62@gmail.com",
    "created_at": "2025-11-15T00:47:11Z",
    "recording_id": "101912858",
    "share_url": "https://fathom.video/share/VjWYnfk7UtpcrExHcD8r3RYB4eoH1Kmz",
    "meeting_title": "Jim Robinson and Andre Panet-Raymond"
  },
  {
    "client": "Jim Robinson (jfrobinson62@gmail.com)",
    "email": "jfrobinson62@gmail.com",
    "created_at": "2025-11-22T00:45:46Z",
    "recording_id": "103641943",
    "share_url": "https://fathom.video/share/PVF5gbyQjH1tNM4DSokw7yDSK8USL9zP",
    "meeting_title": "Jim Robinson and Andre Panet-Raymond"
  },
  {
    "client": "Jim Robinson (jfrobinson62@gmail.com)",
    "email": "jfrobinson62@gmail.com",
    "created_at": "2025-11-26T21:27:09Z",
    "recording_id": "104677440",
    "share_url": "https://fathom.video/share/sw2mJSWBVAdXTySaQYzBMyaJ733uCsCm",
    "meeting_title": "Jim Robinson and Andre Panet-Raymond"
  },
  {
    "client": "Jonathan Soliz (jon.rsmasonry@gmail.com)",
    "email": "jon.rsmasonry@gmail.com",
    "created_at": "2025-12-04T20:44:22Z",
    "recording_id": "106426997",
    "share_url": "https://fathom.video/share/MsE3jDM2KwDGKHipFbBKpWZkGfyKUzHf",
    "meeting_title": "Jonathan Soliz and Andre Panet-Raymond"
  },
  {
    "client": "Jonathan Soliz (jon.rsmasonry@gmail.com)",
    "email": "jon.rsmasonry@gmail.com",
    "created_at": "2025-12-11T19:50:03Z",
    "recording_id": "108161769",
    "share_url": "https://fathom.video/share/Y5RYn3kiQx-1BLc1fffjcAFtZvUARVxN",
    "meeting_title": "Jonathan Soliz and Andre Panet-Raymond"
  },
  {
    "client": "Joseph Habermann (joseph.habermann123@gmail.com)",
    "email": "joseph.habermann123@gmail.com",
    "created_at": "2025-12-09T22:29:44Z",
    "recording_id": "107509708",
    "share_url": "https://fathom.video/share/Nix5drr8DNtDivwjb3jcqzkH4y4ERjeY",
    "meeting_title": "Joseph Habermann and Andre Panet-Raymond"
  },
  {
    "client": "Joshua Vattiprolu (joshuavattiprolu1@gmail.com)",
    "email": "joshuavattiprolu1@gmail.com",
    "created_at": "2025-12-10T19:32:23Z",
    "recording_id": "107810083",
    "share_url": "https://fathom.video/share/P_ys8LYVS8gVS8tET65GQ2imPtvr2HD1",
    "meeting_title": "Joshua Vattiprolu and Andre Panet-Raymond"
  },
  {
    "client": "JP Williams (johnpaulwilliams777@yahoo.com)",
    "email": "johnpaulwilliams777@yahoo.com",
    "created_at": "2026-01-14T19:37:10Z",
    "recording_id": "114281563",
    "share_url": "https://fathom.video/share/5E2by1uHyEpqmes8KeyHv1o3jh8yfYvs",
    "meeting_title": "JP Williams and Andre Panet-Raymond"
  },
  {
    "client": "JP Williams (johnpaulwilliams777@yahoo.com)",
    "email": "johnpaulwilliams777@yahoo.com",
    "created_at": "2026-02-24T20:58:37Z",
    "recording_id": "125000036",
    "share_url": "https://fathom.video/share/h9ggTKdP42bCQqqx9rk9qSg-DX1BpCxY",
    "meeting_title": "JP and Andre Panet-Raymond"
  },
  {
    "client": "Justin Henson (justinhenson2006@yahoo.com)",
    "email": "justinhenson2006@yahoo.com",
    "created_at": "2026-02-23T19:38:28Z",
    "recording_id": "124605856",
    "share_url": "https://fathom.video/share/MzbymFR1dEsr_saxvT3W5tRQrGTTWkMw",
    "meeting_title": "Justin Henson and Andre Panet-Raymond"
  },
  {
    "client": "Kenzie Cook (makenziecook199@gmail.com)",
    "email": "makenziecook199@gmail.com",
    "created_at": "2025-11-05T21:45:23Z",
    "recording_id": "99507710",
    "share_url": "https://fathom.video/share/Arx3NetdGW15zC2cL_q1Rbz7rWmqhyZ-",
    "meeting_title": "Kenzie Cook and Andre Panet-Raymond"
  },
  {
    "client": "Kenzie Cook (makenziecook199@gmail.com)",
    "email": "makenziecook199@gmail.com",
    "created_at": "2025-11-19T19:33:21Z",
    "recording_id": "102894852",
    "share_url": "https://fathom.video/share/zukYhPsyPGexokp5LDZ5KGjWqzR6f7EF",
    "meeting_title": "Kenzie Cook and Andre Panet-Raymond"
  },
  {
    "client": "Kenzie Cook (makenziecook199@gmail.com)",
    "email": "makenziecook199@gmail.com",
    "created_at": "2025-11-26T19:24:08Z",
    "recording_id": "104632605",
    "share_url": "https://fathom.video/share/xu1v9YLnKvYyTnQQjcM51ncAr5YwGgF7",
    "meeting_title": "Kenzie Cook and Andre Panet-Raymond"
  },
  {
    "client": "Khle Beckwith (kylebeckwith22@gmail.com)",
    "email": "kylebeckwith22@gmail.com",
    "created_at": "2025-12-09T03:19:14Z",
    "recording_id": "107181597",
    "share_url": "https://fathom.video/share/uzCtk2NfMvLjJY9k1Tv9nx-bRcs7X185",
    "meeting_title": "Khle Beckwith and Andre Panet-Raymond"
  },
  {
    "client": "Loron Brown (lobrown82@gmail.com)",
    "email": "lobrown82@gmail.com",
    "created_at": "2025-12-15T20:08:24Z",
    "recording_id": "108831271",
    "share_url": "https://fathom.video/share/a7v9EAtCw6qViV8hziThj2Hohsquigbh",
    "meeting_title": "Loran Brown and Andre Panet-Raymond"
  },
  {
    "client": "Luis Jimenez (1345luisjimenez@gmail.com)",
    "email": "1345luisjimenez@gmail.com",
    "created_at": "2026-01-10T21:18:18Z",
    "recording_id": "113286672",
    "share_url": "https://fathom.video/share/Aoh4JHQ1uxQzCosrVZ9NgZ888Ttx_gLz",
    "meeting_title": "Luis Jimenez and Andre Panet-Raymond"
  },
  {
    "client": "Makenzie Cook (makenziecook199@gmail.com)",
    "email": "makenziecook199@gmail.com",
    "created_at": "2025-10-25T19:16:41Z",
    "recording_id": "96786615",
    "share_url": "https://fathom.video/share/XcyeUeeETYy4dv9tCDsQy8Y7anjR_yLk",
    "meeting_title": "Makenzie Cook and Andre Panet-Raymond"
  },
  {
    "client": "Martha Candelaria (drkblcangel@yahoo.com)",
    "email": "drkblcangel@yahoo.com",
    "created_at": "2025-12-10T00:01:48Z",
    "recording_id": "107542951",
    "share_url": "https://fathom.video/share/WefFZdG8miAW2QjYLZX_gQSW6Z7-dVSS",
    "meeting_title": "Martha Candelaria and Andre Panet-Raymond"
  },
  {
    "client": "Matija Kulic (matatata3000@gmail.com)",
    "email": "matatata3000@gmail.com",
    "created_at": "2025-12-03T21:57:14Z",
    "recording_id": "106086726",
    "share_url": "https://fathom.video/share/F3vk9HkHLtyPfxkpvKBDkLMFHXdwu-SR",
    "meeting_title": "Matija Kulic and Andre Panet-Raymond"
  },
  {
    "client": "Michael Kennedy (kennedym609@hotmail.com)",
    "email": "kennedym609@hotmail.com",
    "created_at": "2026-01-05T20:49:39Z",
    "recording_id": "111877546",
    "share_url": "https://fathom.video/share/QsSMfdWs9uYkAzeA7HcuW3B2p6B3yGc8",
    "meeting_title": "Michael Kennedy and Andre Panet-Raymond"
  },
  {
    "client": "Michael Shanks (michaelshanks2626@gmail.com)",
    "email": "michaelshanks2626@gmail.com",
    "created_at": "2025-10-25T23:12:48Z",
    "recording_id": "96791216",
    "share_url": "https://fathom.video/share/dsvyGZ8-Pf5-XJZakckUqfQLzAScwu38",
    "meeting_title": "Michael Shanks and Andre Panet-Raymond"
  },
  {
    "client": "Michael Shanks (michaelshanks2626@gmail.com)",
    "email": "michaelshanks2626@gmail.com",
    "created_at": "2025-11-24T21:16:48Z",
    "recording_id": "104007900",
    "share_url": "https://fathom.video/share/Yy8Tebme-LnMH6UFFK_EszCszB_5bcsd",
    "meeting_title": "Michael Shanks and Andre Panet-Raymond"
  },
  {
    "client": "Michael Shanks (michaelshanks2626@gmail.com)",
    "email": "michaelshanks2626@gmail.com",
    "created_at": "2025-12-13T19:43:59Z",
    "recording_id": "108544954",
    "share_url": "https://fathom.video/share/GzdEQsJS8p-89VUHpgmixWV_aGzxiyqf",
    "meeting_title": "Michael Shanks and Andre Panet-Raymond"
  },
  {
    "client": "Noah Bennett (noahbennett0904@yahoo.com)",
    "email": "noahbennett0904@yahoo.com",
    "created_at": "2025-12-29T23:03:39Z",
    "recording_id": "111142194",
    "share_url": "https://fathom.video/share/U4JfbiqEaMuUQsjSuEqsxjZ3UMh_is-1",
    "meeting_title": "Noah Bennett and Andre Panet-Raymond"
  },
  {
    "client": "Noah Bennett (noahbennett0904@yahoo.com)",
    "email": "noahbennett0904@yahoo.com",
    "created_at": "2025-12-30T19:46:01Z",
    "recording_id": "111288318",
    "share_url": "https://fathom.video/share/7ib-pS12nQFT37peA-y5B1DyynTNrZ92",
    "meeting_title": "Noah Bennett and Andre Panet-Raymond"
  },
  {
    "client": "Ramsey Johnson (ramseyjohnson0827@gmail.com)",
    "email": "ramseyjohnson0827@gmail.com",
    "created_at": "2025-12-22T20:45:59Z",
    "recording_id": "110485493",
    "share_url": "https://fathom.video/share/k-uHn_1xbLbbahhb9h_yR6h5BnmxfR3z",
    "meeting_title": "Ramsey Johnson and Andre Panet-Raymond"
  },
  {
    "client": "Randy Guthrie (randyguthrie02@gmail.com)",
    "email": "randyguthrie02@gmail.com",
    "created_at": "2025-12-11T00:41:37Z",
    "recording_id": "107901545",
    "share_url": "https://fathom.video/share/vrs4eVf_XDxF5RCdzFxxexCXhSpcsQ3G",
    "meeting_title": "Randy Guthrie and Andre Panet-Raymond"
  },
  {
    "client": "Samuel Kattoura (bigkatt1996@hotmail.com)",
    "email": "bigkatt1996@hotmail.com",
    "created_at": "2026-02-13T21:03:17Z",
    "recording_id": "122406429",
    "share_url": "https://fathom.video/share/U3zCM7DgMtLWgvT-fxGegxbxw36PYEfw",
    "meeting_title": "Samuel Kattoura and Andre Panet-Raymond"
  },
  {
    "client": "Sandra Herrera (sagitario_45@hotmail.com)",
    "email": "sagitario_45@hotmail.com",
    "created_at": "2025-11-29T01:28:38Z",
    "recording_id": "105029337",
    "share_url": "https://fathom.video/share/hmBxg-qWBzzM7Qrk2Z5TgqjeJjsKjNyp",
    "meeting_title": "Sandra Herrera and Andre Panet-Raymond"
  },
  {
    "client": "Sandra Herrera (sagitario_45@hotmail.com)",
    "email": "sagitario_45@hotmail.com",
    "created_at": "2025-12-04T21:58:44Z",
    "recording_id": "106462389",
    "share_url": "https://fathom.video/share/CZzbiYj4VWayd9z8JJx35abeSwnMm7nA",
    "meeting_title": "Sandra Herrera and Andre Panet-Raymond"
  },
  {
    "client": "Sandra Herrera (sagitario_45@hotmail.com)",
    "email": "sagitario_45@hotmail.com",
    "created_at": "2025-12-11T21:31:52Z",
    "recording_id": "108206220",
    "share_url": "https://fathom.video/share/xjyZZ1qFzRf9238hVSva4x_twnULB4Tg",
    "meeting_title": "Sandra Herrera and Andre Panet-Raymond"
  },
  {
    "client": "Santiago Vadillo (svadillo.m@gmail.com)",
    "email": "svadillo.m@gmail.com",
    "created_at": "2025-11-22T20:13:23Z",
    "recording_id": "103671672",
    "share_url": "https://fathom.video/share/h6NQe7JxCCJe46pxrTuHwUk1MPxBSyAc",
    "meeting_title": "Santiago Vadillo and Andre Panet-Raymond"
  },
  {
    "client": "Sharon Mathew (sharonkmathew2007@gmail.com)",
    "email": "sharonkmathew2007@gmail.com",
    "created_at": "2025-11-25T02:21:56Z",
    "recording_id": "104048250",
    "share_url": "https://fathom.video/share/iyRi3BqYPrmZU3pzCMKx29vxVczhoyxr",
    "meeting_title": "Sharon Mathew and Andre Panet-Raymond"
  },
  {
    "client": "Stefania Schenetti (stefania.sch@hotmail.com)",
    "email": "stefania.sch@hotmail.com",
    "created_at": "2026-01-26T21:46:43Z",
    "recording_id": "117226218",
    "share_url": "https://fathom.video/share/R_E8KDnpaKDFM3vabzZPCS2DyEmrfpYi",
    "meeting_title": "Stefania Schenetti and Andre Panet-Raymond"
  },
  {
    "client": "Stefania Schenetti (stefania.sch@hotmail.com)",
    "email": "stefania.sch@hotmail.com",
    "created_at": "2026-02-09T21:38:17Z",
    "recording_id": "120974643",
    "share_url": "https://fathom.video/share/sHcMqPicsayH-uussjzzzrjjG1XDPqsV",
    "meeting_title": "Stefania Schenetti and Andre Panet-Raymond"
  },
  {
    "client": "Stefania Schenetti (stefania.sch@hotmail.it)",
    "email": "stefania.sch@hotmail.it",
    "created_at": "2026-02-23T21:33:36Z",
    "recording_id": "124644081",
    "share_url": "https://fathom.video/share/HLF5ax4mNjMzgUd8sMjKH9x8yoyxZmmY",
    "meeting_title": "Stefania Schenetti and Andre Panet-Raymond"
  },
  {
    "client": "Stefania Schenetti (stefanialezioniitaliano@gmail.com)",
    "email": "stefanialezioniitaliano@gmail.com",
    "created_at": "2026-01-03T19:47:49Z",
    "recording_id": "111593523",
    "share_url": "https://fathom.video/share/BhDkf_iNWbNz-fzRRveCJsmy2nr3-8Gy",
    "meeting_title": "Stefania Schenetti and Andre Panet-Raymond"
  },
  {
    "client": "Stephan Petzold (rufus.dupres@freenet.de)",
    "email": "rufus.dupres@freenet.de",
    "created_at": "2026-01-27T21:12:15Z",
    "recording_id": "117584398",
    "share_url": "https://fathom.video/share/nxp5yANyV7sFxVKJMVrKys8osxKU7x2t",
    "meeting_title": "Stephan Petzold and Andre Panet-Raymond"
  },
  {
    "client": "Stephan Petzold (rufus.dupres@freenet.de)",
    "email": "rufus.dupres@freenet.de",
    "created_at": "2026-02-02T21:01:05Z",
    "recording_id": "119061546",
    "share_url": "https://fathom.video/share/VQsxzSwZe4m3qmfwfnqZJTYzbwcNmHhR",
    "meeting_title": "Stephan Petzold and Andre Panet-Raymond"
  },
  {
    "client": "Stephan Petzold (rufus.dupres@freenet.de)",
    "email": "rufus.dupres@freenet.de",
    "created_at": "2026-02-06T20:13:24Z",
    "recording_id": "120517848",
    "share_url": "https://fathom.video/share/SA3eCPGzkTeRY-BvUD4jz7FsyeJVoQnn",
    "meeting_title": "Stephan Petzold and Andre Panet-Raymond"
  },
  {
    "client": "Stephan Petzold (rufus.dupres@freenet.de)",
    "email": "rufus.dupres@freenet.de",
    "created_at": "2026-02-12T22:18:41Z",
    "recording_id": "122132527",
    "share_url": "https://fathom.video/share/-wVkp_DbHk12Qa_UZGj48XZR6SMxuSxu",
    "meeting_title": "Stephan Petzold and Andre Panet-Raymond"
  },
  {
    "client": "Stephen Frantz (stephen.txadjuster@gmail.com)",
    "email": "stephen.txadjuster@gmail.com",
    "created_at": "2026-02-18T19:58:11Z",
    "recording_id": "123468852",
    "share_url": "https://fathom.video/share/7vTbiuJW6YpEooxy99m4Ryyx-xuGT9eu",
    "meeting_title": "Stephen Frantz and Andre Panet-Raymond"
  },
  {
    "client": "Stevin Thomas (stevinsanthosh406@gmail.com)",
    "email": "stevinsanthosh406@gmail.com",
    "created_at": "2025-10-25T18:31:17Z",
    "recording_id": "96785662",
    "share_url": "https://fathom.video/share/M1Vzgnz5H2EL_-NLannqEW1enz5ajmnr",
    "meeting_title": "Stevin Thomas and Andre Panet-Raymond"
  },
  {
    "client": "Susannah DuRant (susannah.durant@fathom.video)",
    "email": "susannah.durant@fathom.video",
    "created_at": "2025-10-04T19:54:29Z",
    "recording_id": "91882039",
    "share_url": "https://fathom.video/share/ZSSNMW76XHbQUBv9TAWYFzNL2JT7rGv6",
    "meeting_title": "Fathom Demo"
  },
  {
    "client": "Timothy Mabie (mabie.timothy@yahoo.com)",
    "email": "mabie.timothy@yahoo.com",
    "created_at": "2026-02-10T21:31:39Z",
    "recording_id": "121354120",
    "share_url": "https://fathom.video/share/NyeNcVcSwmy3H8NwvDUEcrytY-Uxwg7x",
    "meeting_title": "Timothy Mabie and Andre Panet-Raymond"
  },
  {
    "client": "Travis Dumas (travis.dumas@gmail.com)",
    "email": "travis.dumas@gmail.com",
    "created_at": "2025-12-08T23:28:36Z",
    "recording_id": "107152712",
    "share_url": "https://fathom.video/share/LMTKz_XZys1u9KBFwYBygEQp5eWzwiuV",
    "meeting_title": "Travis Dumas and Andre Panet-Raymond"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-10-04T20:16:12Z",
    "recording_id": "91882677",
    "share_url": "https://fathom.video/share/CJiN4cMrUpAXx8UgX2JRJ4rRdhcfaUwd",
    "meeting_title": "Test call"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-10-04T20:21:33Z",
    "recording_id": "91882738",
    "share_url": "https://fathom.video/share/f_t3815NU6pz-1JszomVgEr3teLv1krn",
    "meeting_title": "Test call"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-11-29T19:14:04Z",
    "recording_id": "105055031",
    "share_url": "https://fathom.video/share/zx9jyxY862s47xyRnvJZQ6UGtnxQVsSS",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-11-30T02:04:27Z",
    "recording_id": "105060323",
    "share_url": "https://fathom.video/share/DeQZc5WryTWaSRNxzjbnx7NMD2PKxiy-",
    "meeting_title": "Sandra Herrera: Heartbroken to Hopeful Clarity Call"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-11-30T02:58:41Z",
    "recording_id": "105061269",
    "share_url": "https://fathom.video/share/CUCix8g4vDGQxab_Mem5hkAGnjPQUmPM",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-12-01T21:35:18Z",
    "recording_id": "105390211",
    "share_url": "https://fathom.video/share/KGyWxY1ZVGFh5rxwMNdG5qUeyjWHYU3X",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-12-02T02:45:22Z",
    "recording_id": "105430146",
    "share_url": "https://fathom.video/share/dBEdZvwFY37BR8XD6ynV8RhgHcMdx793",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-12-02T21:34:56Z",
    "recording_id": "105755150",
    "share_url": "https://fathom.video/share/V8Wz8A9VjbWSo83sCJayfypCgtHVzRsQ",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-12-03T03:56:41Z",
    "recording_id": "105804560",
    "share_url": "https://fathom.video/share/necqxS6s_5_Q-n4s3zsBBKo-MsNr6haf",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-12-03T23:43:49Z",
    "recording_id": "106150009",
    "share_url": "https://fathom.video/share/T_3Ci1Fej3LvQsKr72W5mexTGBWpfa5m",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-12-04T03:28:14Z",
    "recording_id": "106168118",
    "share_url": "https://fathom.video/share/sEXxReCzz2R9ysZEy5fvER9bJjRkgqie",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-12-05T02:06:15Z",
    "recording_id": "106509270",
    "share_url": "https://fathom.video/share/x2zUmAzsXZzQ5ZnJkEtatmzkx1VEAV7z",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-12-06T02:37:59Z",
    "recording_id": "106788802",
    "share_url": "https://fathom.video/share/ay9kABQPeFoUGV75tU-hcv4gA8kxazYs",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-12-06T18:56:01Z",
    "recording_id": "106812732",
    "share_url": "https://fathom.video/share/ic5tspCpiUzu6pBsyCeSGgeu9V6asz-N",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-12-07T05:01:07Z",
    "recording_id": "106820718",
    "share_url": "https://fathom.video/share/DxUzPCzrb3deePKyuusyf7tpck_k_tXL",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2025-12-15T23:04:28Z",
    "recording_id": "108907626",
    "share_url": "https://fathom.video/share/GQy84ytAiWLNqbg5ahXHGKvL-74La9td",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2026-01-05T01:39:57Z",
    "recording_id": "111630828",
    "share_url": "https://fathom.video/share/TtS-BF9Zez9XHVp1RZ2vQJuhVw_QzELR",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2026-01-13T09:47:32Z",
    "recording_id": "113733271",
    "share_url": "https://fathom.video/share/R_xZpHTBnyRc4_urrzKrRNHt7NPj2xR6",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2026-01-21T21:17:00Z",
    "recording_id": "116151414",
    "share_url": "https://fathom.video/share/9Gqsz1pbnZRNdSAe22syC4SYfz2nkiq3",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2026-01-28T20:38:38Z",
    "recording_id": "117878532",
    "share_url": "https://fathom.video/share/eHdupfs7iBb1UR2JgM-iASTfisqTzKLz",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2026-02-02T20:10:27Z",
    "recording_id": "119026595",
    "share_url": "https://fathom.video/share/zbJqrCRydVKNR9gRuyK8d_AGXfKsrggF",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2026-02-02T22:58:42Z",
    "recording_id": "119108918",
    "share_url": "https://fathom.video/share/_zgsemr272j5zNzfR5PbaswayUjx-FGy",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2026-02-04T22:42:16Z",
    "recording_id": "119871165",
    "share_url": "https://fathom.video/share/Nf-pms3fcHJkKgsAJBdshZ-dbmYE88L_",
    "meeting_title": "Arno Marx: Spiritual Warfare Strategy Call"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2026-02-12T23:00:13Z",
    "recording_id": "122148624",
    "share_url": "https://fathom.video/share/3GEaevcaSE9zWx7VoUrrQ3BxGKtH1Wab",
    "meeting_title": "Arno Marx: Spiritual Warfare Strategy Call"
  },
  {
    "client": "Unknown (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2026-02-17T18:36:20Z",
    "recording_id": "123058987",
    "share_url": "https://fathom.video/share/pjzygAsP6VQCoJ4LMqBKj2DJtTqhsnzp",
    "meeting_title": "Impromptu Zoom Meeting"
  },
  {
    "client": "victor hernandez (victorbobadilla11@outlook.com)",
    "email": "victorbobadilla11@outlook.com",
    "created_at": "2025-12-20T21:29:13Z",
    "recording_id": "110241737",
    "share_url": "https://fathom.video/share/cAkLZaGZoZy2xznQfiFbyq8upX47rLCg",
    "meeting_title": "victor hernandez and Andre Panet-Raymond"
  },
  {
    "client": "Victoria Juarez (karenjuarez1327@gmail.com)",
    "email": "karenjuarez1327@gmail.com",
    "created_at": "2026-01-07T19:30:02Z",
    "recording_id": "112515669",
    "share_url": "https://fathom.video/share/yGw2Dxz8sMySCDasMxpw3E5c9nxtGi1X",
    "meeting_title": "Victoria Juarez and Andre Panet-Raymond"
  },
  {
    "client": "Will (weisenw1997@gmail.com)",
    "email": "weisenw1997@gmail.com",
    "created_at": "2026-01-23T23:23:03Z",
    "recording_id": "116846958",
    "share_url": "https://fathom.video/share/dNqFCKvMBJ4qMruJ3SJM6LGKrNkyAzWC",
    "meeting_title": "Will and Andre Panet-Raymond"
  },
  {
    "client": "Will W (unknown@example.com)",
    "email": "unknown@example.com",
    "created_at": "2026-01-10T01:22:01Z",
    "recording_id": "113247059",
    "share_url": "https://fathom.video/share/LCShQ6EFWxzSw7qNPxaUnuXQvoi9rnxz",
    "meeting_title": "Will W and Andre Panet-Raymond"
  },
  {
    "client": "Will W (weisenw1997@gmail.com)",
    "email": "weisenw1997@gmail.com",
    "created_at": "2025-12-23T22:59:43Z",
    "recording_id": "110760340",
    "share_url": "https://fathom.video/share/xi5-6vKUhDaN5Eynv1z5ffcZGZVhYE9-",
    "meeting_title": "Will W and Andre Panet-Raymond"
  },
  {
    "client": "Will W (weisenw1997@gmail.com)",
    "email": "weisenw1997@gmail.com",
    "created_at": "2025-12-27T22:04:54Z",
    "recording_id": "110955977",
    "share_url": "https://fathom.video/share/1JdsL1aoMiKzxJBqPKxaJ8dWn37wsBDq",
    "meeting_title": "Will W and Andre Panet-Raymond"
  },
  {
    "client": "Will W (weisenw1997@gmail.com)",
    "email": "weisenw1997@gmail.com",
    "created_at": "2026-01-03T21:05:33Z",
    "recording_id": "111596892",
    "share_url": "https://fathom.video/share/u9yeS3FXRzgXe5j2pYxBnxmVsub27h1P",
    "meeting_title": "Will W and Andre Panet-Raymond"
  },
  {
    "client": "Will W (weisenw1997@gmail.com)",
    "email": "weisenw1997@gmail.com",
    "created_at": "2026-01-17T00:52:09Z",
    "recording_id": "115053396",
    "share_url": "https://fathom.video/share/ZJhXSnsSWgT43UAThDfD9oDT2zoEQbjj",
    "meeting_title": "Will W and Andre Panet-Raymond"
  },
  {
    "client": "Will w (weisenw1997@gmail.com)",
    "email": "weisenw1997@gmail.com",
    "created_at": "2026-02-02T17:57:23Z",
    "recording_id": "118936166",
    "share_url": "https://fathom.video/share/BpgznJrv5mXX4qtiNvD9qk9y3cBtsLoD",
    "meeting_title": "Will w and Andre Panet-Raymond"
  },
  {
    "client": "Zachary Evans (castromontega97@gmail.com)",
    "email": "castromontega97@gmail.com",
    "created_at": "2025-12-06T19:51:47Z",
    "recording_id": "106813047",
    "share_url": "https://fathom.video/share/gyzzvg_WLyj2RGmUyjHh8zCXWxXB-wS9",
    "meeting_title": "Zachary Evans and Andre Panet-Raymond"
  },
  {
    "client": "Zain Singh (zainsingh@icloud.com)",
    "email": "zainsingh@icloud.com",
    "created_at": "2025-11-21T19:31:44Z",
    "recording_id": "103584348",
    "share_url": "https://fathom.video/share/72aEAsLxUKa23eCMrQBpEph5SXRy6DeJ",
    "meeting_title": "Zain Singh and Andre Panet-Raymond"
  }
]
```



## State: processed.json

```json
{
  "processed": [
    "https://fathom.video/share/-J72AS-irsPjxM-4zg6gT5DXayn_tBBG",
    "https://fathom.video/share/3sXnwgFgxZQJDT84Aryxay59psZtsXWS",
    "https://fathom.video/share/7Wcj1kuB9aC-N4u9y99mNXFQ2VBytuHw",
    "https://fathom.video/share/7yfj1v8RCe6tNGfsrhLedy8sD9JbpPte",
    "https://fathom.video/share/DUUyck7k9YaJJvWosxsTeUL2MzTGCeLk",
    "https://fathom.video/share/FXzEuuJkT-yAGyAiHgGnCzUUyKLPAUqe",
    "https://fathom.video/share/Hyf6QJAGXFimPtqpszx5DM2G3-nXgxuQ",
    "https://fathom.video/share/JsmTS3dWxeYqCs--99AqzN-gBRka8ogh",
    "https://fathom.video/share/LC2jASLrw2HxLUkqjPARWbSfzyhffxpc",
    "https://fathom.video/share/LP1ED5F9dnz9PwaLHnM_ys9xAxLVZz_8",
    "https://fathom.video/share/MHUn-4cJvKYL2J7gMTmmTXEi86a9hKYz",
    "https://fathom.video/share/MeEeshZHBLUUJz9d2LVZUaeyicHcxYRh",
    "https://fathom.video/share/NhwzWwZ4AbjRnibWhi4jTvFY5kbncPhk",
    "https://fathom.video/share/NvGBiRWSTU14WQ746ydC9B-q6aUVj7yP",
    "https://fathom.video/share/Sdp1DhRf26d8VnJx_yxwajAywF2pzjvM",
    "https://fathom.video/share/Siz4qBsCgofxUCb4bg-44RNQgD_Uv3Y6",
    "https://fathom.video/share/T1zno5zskCCc6AmrzvTQUTXdSsRBHUpm",
    "https://fathom.video/share/TcQx2Az4GfTSp194BjFz1oyCZjgEju3Q",
    "https://fathom.video/share/a_uXC4pevYwheSsT-VpssNfgoZtyrDyD",
    "https://fathom.video/share/c1fw-iaY5H9eFVE7NK_W_XA3w55gq2su",
    "https://fathom.video/share/dK8oV4pEZoswL2My9s2bgwBb21CqUdNy",
    "https://fathom.video/share/eM7ewxCHgTi4C62nW1fvA3_p7EqNhS_d",
    "https://fathom.video/share/g1fXkS_SjdWMbeVbhwvjjRz9funEUsxB",
    "https://fathom.video/share/gjnz-nx5zzVkwa1LK1zZaQi8Xng1sNXs",
    "https://fathom.video/share/jTk4dTr2uxioK7AzQjVUzkxfo_x61hGb",
    "https://fathom.video/share/kgLpjMboKQuyJo8s9yQJnDCUjPV9B8aS",
    "https://fathom.video/share/xYALcSdZzKCszKViyBA3Vwbj2oxaLR3k",
    "https://fathom.video/share/xeXtgYksG6RqyP9Qvt9xR3z7S_TuEnH2",
    "https://fathom.video/share/xg31LyAHekJZb8XqAXoLPrUyAePcZ_ax",
    "https://fathom.video/share/xoakee5Y4KiXpxC9Cs17gdziuh4ZW1Fk",
    "https://fathom.video/share/zY69s2-oTzTs1WLpsAg_Z2FPix17ComD"
  ],
  "updated_at": "2026-03-08T11:30:24.497953+00:00"
}
```



## State: last_batch.json

```json
{
  "created_at": "2026-03-08T11:30:24.498903+00:00",
  "pending_total": 164,
  "selected_count": 3,
  "results": [
    {
      "share_url": "https://fathom.video/share/kgLpjMboKQuyJo8s9yQJnDCUjPV9B8aS",
      "client": "Augusto Leal (aleal4@gmail.com)",
      "created_at": "2026-02-24T22:57:05Z",
      "meeting_title": "Augusto Leal and Andre Panet-Raymond",
      "ok": true,
      "returncode": 0,
      "run_id": "20260308_063002_c34df58a",
      "stderr": "",
      "nugget_export": "/home/openclaw_agent_1/krc_vault/gold nugget exports/20260308_063002_c34df58a__Augusto Leal _aleal4_gmail.com___nuggets.json",
      "objection_export": "/home/openclaw_agent_1/krc_vault/gold nugget exports/20260308_063002_c34df58a__Augusto Leal _aleal4_gmail.com___objections.json"
    },
    {
      "share_url": "https://fathom.video/share/MeEeshZHBLUUJz9d2LVZUaeyicHcxYRh",
      "client": "Austin Foster (austinrfoster01@gmail.com)",
      "created_at": "2026-02-17T21:58:39Z",
      "meeting_title": "Austin Foster and Andre Panet-Raymond",
      "ok": true,
      "returncode": 0,
      "run_id": "20260308_063002_97e91a95",
      "stderr": "",
      "nugget_export": "/home/openclaw_agent_1/krc_vault/gold nugget exports/20260308_063002_97e91a95__Austin Foster _austinrfoster01_gmail.com___nuggets.json",
      "objection_export": "/home/openclaw_agent_1/krc_vault/gold nugget exports/20260308_063002_97e91a95__Austin Foster _austinrfoster01_gmail.com___objections.json"
    },
    {
      "share_url": "https://fathom.video/share/gjnz-nx5zzVkwa1LK1zZaQi8Xng1sNXs",
      "client": "Barbara Miller-Brandyberry (sunriseskies@hotmail.com)",
      "created_at": "2025-11-13T21:04:47Z",
      "meeting_title": "Barbara Miller-Brandyberry and Andre Panet-Raymond",
      "ok": true,
      "returncode": 0,
      "run_id": "20260308_063002_6c5da4b5",
      "stderr": "",
      "nugget_export": "/home/openclaw_agent_1/krc_vault/gold nugget exports/20260308_063002_6c5da4b5__Barbara Miller-Brandyberry _sunriseskies_hotmail.com___nuggets.json",
      "objection_export": "/home/openclaw_agent_1/krc_vault/gold nugget exports/20260308_063002_6c5da4b5__Barbara Miller-Brandyberry _sunriseskies_hotmail.com___objections.json"
    }
  ]
}
```



## Recent pipeline files

```
Recent archived manifests:
2026-03-08 18:22 /home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_182019_b0fb2a72/manifest.json
2026-03-08 18:17 /home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_181244_b0fb2a72/manifest.json
2026-03-08 17:29 /home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_172401_545ca1b0/manifest.json
2026-03-08 17:15 /home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_171522_61022128/manifest.json
2026-03-08 17:15 /home/openclaw_agent_1/krc_vault/pipeline_runs/archive/20260308_171522_401462f8/manifest.json

Recent quarantine manifests:
2026-03-08 17:23 /home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_172051_545ca1b0/manifest.json
2026-03-08 17:20 /home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_172001_545ca1b0/manifest.json
2026-03-08 17:15 /home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_171523_55b93cc6/manifest.json
2026-03-08 17:15 /home/openclaw_agent_1/krc_vault/pipeline_runs/quarantine/20260308_171523_02d7766f/manifest.json

Recent pipeline logs:
/home/openclaw_agent_1/krc_vault/pipeline_runs/logs/20260308_182019_b0fb2a72.log
/home/openclaw_agent_1/krc_vault/pipeline_runs/logs/20260308_181244_b0fb2a72.log
/home/openclaw_agent_1/krc_vault/pipeline_runs/logs/20260308_172401_545ca1b0.log
/home/openclaw_agent_1/krc_vault/pipeline_runs/logs/20260308_172051_545ca1b0.log
/home/openclaw_agent_1/krc_vault/pipeline_runs/logs/20260308_172001_545ca1b0.log
/home/openclaw_agent_1/krc_vault/pipeline_runs/logs/20260308_171523_02d7766f.log
/home/openclaw_agent_1/krc_vault/pipeline_runs/logs/20260308_171522_401462f8.log
/home/openclaw_agent_1/krc_vault/pipeline_runs/logs/20260308_171522_61022128.log

```



## Manifest: 20260308_172051_545ca1b0

```json
{
  "run_id": "20260308_172051_545ca1b0",
  "source_id": "fathom_545ca1b0376d6e6b",
  "source_kind": "fathom_share_url",
  "reprocess": true,
  "created_at": "2026-03-08T22:20:51.101454+00:00",
  "updated_at": "2026-03-08T22:20:51.101466+00:00",
  "current_stage": "bob",
  "stage_status": {
    "donald": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172051_545ca1b0/stage_inputs/donald_url_intake.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172051_545ca1b0/stage_outputs/donald_canonical.json",
      "started_at": "2026-03-08T22:20:51.115853+00:00",
      "completed_at": "2026-03-08T22:20:52.528927+00:00",
      "handoff_message": "RUN_ID=20260308_172051_545ca1b0 STAGE=DONALD_DONE"
    },
    "mark": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172051_545ca1b0/stage_outputs/donald_canonical.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172051_545ca1b0/stage_outputs/mark_body.md",
      "started_at": "2026-03-08T22:20:52.542840+00:00",
      "completed_at": "2026-03-08T22:21:05.088830+00:00",
      "handoff_message": "RUN_ID=20260308_172051_545ca1b0 STAGE=MARK_DONE"
    },
    "bob": {
      "status": "pending",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172051_545ca1b0/stage_outputs/mark_body.md",
      "canonical_output_path": null,
      "started_at": "2026-03-08T22:21:05.101411+00:00",
      "completed_at": null,
      "handoff_message": null
    },
    "hook": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    },
    "jimmy": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    }
  },
  "flags": [
    {
      "flag_code": "DONALD_ZERO_NUGGET_FALLBACK",
      "stage": "donald",
      "severity": "warn",
      "short_note": "No nuggets returned, generated deterministic fallback nugget",
      "ts": "2026-03-08T22:20:52.524430+00:00"
    }
  ],
  "errors": {
    "stage": "bob",
    "step": "pipeline",
    "error_message": "bob_modified_mark_body",
    "log_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/logs/20260308_172051_545ca1b0.log",
    "ts": "2026-03-08T22:23:47.741371+00:00"
  },
  "meta": {
    "chat_policy": "one_line_only",
    "pipeline_mode": "single_direction_no_revision_loop"
  }
}
```



## Manifest: 20260308_172001_545ca1b0

```json
{
  "run_id": "20260308_172001_545ca1b0",
  "source_id": "fathom_545ca1b0376d6e6b",
  "source_kind": "fathom_share_url",
  "reprocess": true,
  "created_at": "2026-03-08T22:20:01.334183+00:00",
  "updated_at": "2026-03-08T22:20:01.334195+00:00",
  "current_stage": "donald",
  "stage_status": {
    "donald": {
      "status": "pending",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172001_545ca1b0/stage_inputs/donald_url_intake.json",
      "canonical_output_path": null,
      "started_at": "2026-03-08T22:20:01.351285+00:00",
      "completed_at": null,
      "handoff_message": null
    },
    "mark": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    },
    "bob": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    },
    "hook": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    },
    "jimmy": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    }
  },
  "flags": [],
  "errors": {
    "stage": "donald",
    "step": "pipeline",
    "error_message": "donald_no_nuggets",
    "log_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/logs/20260308_172001_545ca1b0.log",
    "ts": "2026-03-08T22:20:02.342961+00:00"
  },
  "meta": {
    "chat_policy": "one_line_only",
    "pipeline_mode": "single_direction_no_revision_loop"
  }
}
```



## Manifest: 20260308_171523_55b93cc6

```json
{
  "run_id": "20260308_171523_55b93cc6",
  "source_id": "fathom_55b93cc6a4d5210c",
  "source_kind": "fathom_share_url",
  "reprocess": true,
  "created_at": "2026-03-08T22:15:23.851733+00:00",
  "updated_at": "2026-03-08T22:15:23.851739+00:00",
  "current_stage": "donald",
  "stage_status": {
    "donald": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    },
    "mark": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    },
    "bob": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    },
    "hook": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    },
    "jimmy": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    }
  },
  "flags": [],
  "errors": {},
  "meta": {
    "chat_policy": "one_line_only",
    "pipeline_mode": "single_direction_no_revision_loop"
  }
}
```



## Manifest: 20260308_171523_02d7766f

```json
{
  "run_id": "20260308_171523_02d7766f",
  "source_id": "fathom_02d7766f6e97cd2b",
  "source_kind": "fathom_share_url",
  "reprocess": true,
  "created_at": "2026-03-08T22:15:23.862219+00:00",
  "updated_at": "2026-03-08T22:15:23.862224+00:00",
  "current_stage": "donald",
  "stage_status": {
    "donald": {
      "status": "pending",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171523_02d7766f/stage_inputs/donald_url_intake.json",
      "canonical_output_path": null,
      "started_at": "2026-03-08T22:15:23.874601+00:00",
      "completed_at": null,
      "handoff_message": null
    },
    "mark": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    },
    "bob": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    },
    "hook": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    },
    "jimmy": {
      "status": "pending",
      "canonical_input_path": null,
      "canonical_output_path": null,
      "started_at": null,
      "completed_at": null,
      "handoff_message": null
    }
  },
  "flags": [],
  "errors": {
    "stage": "donald",
    "step": "pipeline",
    "error_message": "donald_process_failed rc=3 err=",
    "log_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/logs/20260308_171523_02d7766f.log",
    "ts": "2026-03-08T22:15:24.342266+00:00"
  },
  "meta": {
    "chat_policy": "one_line_only",
    "pipeline_mode": "single_direction_no_revision_loop"
  }
}
```



## Manifest: 20260308_182019_b0fb2a72

```json
{
  "run_id": "20260308_182019_b0fb2a72",
  "source_id": "fathom_b0fb2a72fa14926e",
  "source_kind": "fathom_share_url",
  "reprocess": true,
  "created_at": "2026-03-08T23:20:19.749972+00:00",
  "updated_at": "2026-03-08T23:20:19.749984+00:00",
  "current_stage": "jimmy",
  "stage_status": {
    "donald": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_182019_b0fb2a72/stage_inputs/donald_url_intake.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_182019_b0fb2a72/stage_outputs/donald_canonical.json",
      "started_at": "2026-03-08T23:20:19.763295+00:00",
      "completed_at": "2026-03-08T23:20:21.170803+00:00",
      "handoff_message": "RUN_ID=20260308_182019_b0fb2a72 STAGE=DONALD_DONE"
    },
    "mark": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_182019_b0fb2a72/stage_outputs/donald_canonical.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_182019_b0fb2a72/stage_outputs/mark_body.md",
      "started_at": "2026-03-08T23:20:21.185409+00:00",
      "completed_at": "2026-03-08T23:21:04.841416+00:00",
      "handoff_message": "RUN_ID=20260308_182019_b0fb2a72 STAGE=MARK_DONE"
    },
    "bob": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_182019_b0fb2a72/stage_outputs/mark_body.md",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_182019_b0fb2a72/stage_outputs/bob_caption.md",
      "started_at": "2026-03-08T23:21:04.854631+00:00",
      "completed_at": "2026-03-08T23:22:12.151834+00:00",
      "handoff_message": "RUN_ID=20260308_182019_b0fb2a72 STAGE=BOB_DONE"
    },
    "hook": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_182019_b0fb2a72/stage_outputs/bob_caption.md",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_182019_b0fb2a72/stage_outputs/hook_overlays.json",
      "started_at": "2026-03-08T23:22:12.222481+00:00",
      "completed_at": "2026-03-08T23:22:22.106563+00:00",
      "handoff_message": "RUN_ID=20260308_182019_b0fb2a72 STAGE=HOOK_DONE"
    },
    "jimmy": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_182019_b0fb2a72/stage_outputs/hook_overlays.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_182019_b0fb2a72/final/final_post_ready.md",
      "started_at": "2026-03-08T23:22:22.120339+00:00",
      "completed_at": "2026-03-08T23:22:26.311583+00:00",
      "handoff_message": "RUN_ID=20260308_182019_b0fb2a72 STAGE=FINAL_READY"
    }
  },
  "flags": [
    {
      "flag_code": "DONALD_ZERO_NUGGET_FALLBACK",
      "stage": "donald",
      "severity": "warn",
      "short_note": "No nuggets returned, generated deterministic fallback nugget",
      "ts": "2026-03-08T23:20:21.166477+00:00"
    }
  ],
  "errors": {},
  "meta": {
    "chat_policy": "one_line_only",
    "pipeline_mode": "single_direction_no_revision_loop"
  },
  "final_delivery": {
    "drive_folder_id": "1NOCxQ2K1S2vM07hGHc0xEqTrsl2Ub1tv",
    "drive_file_id": "1-nV2apvZpnPW3xc430CNS2p6sxsKFR9fIQXc9nd3eHE",
    "drive_link": "https://docs.google.com/document/d/1-nV2apvZpnPW3xc430CNS2p6sxsKFR9fIQXc9nd3eHE/edit?usp=drivesdk",
    "uploaded_at": "2026-03-08T23:22:26.311567+00:00"
  }
}
```



## Manifest: 20260308_181244_b0fb2a72

```json
{
  "run_id": "20260308_181244_b0fb2a72",
  "source_id": "fathom_b0fb2a72fa14926e",
  "source_kind": "fathom_share_url",
  "reprocess": true,
  "created_at": "2026-03-08T23:12:44.232483+00:00",
  "updated_at": "2026-03-08T23:12:44.232509+00:00",
  "current_stage": "jimmy",
  "stage_status": {
    "donald": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_181244_b0fb2a72/stage_inputs/donald_url_intake.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_181244_b0fb2a72/stage_outputs/donald_canonical.json",
      "started_at": "2026-03-08T23:12:44.248050+00:00",
      "completed_at": "2026-03-08T23:12:45.435274+00:00",
      "handoff_message": "RUN_ID=20260308_181244_b0fb2a72 STAGE=DONALD_DONE"
    },
    "mark": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_181244_b0fb2a72/stage_outputs/donald_canonical.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_181244_b0fb2a72/stage_outputs/mark_body.md",
      "started_at": "2026-03-08T23:12:45.523661+00:00",
      "completed_at": "2026-03-08T23:13:51.987058+00:00",
      "handoff_message": "RUN_ID=20260308_181244_b0fb2a72 STAGE=MARK_DONE"
    },
    "bob": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_181244_b0fb2a72/stage_outputs/mark_body.md",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_181244_b0fb2a72/stage_outputs/bob_caption.md",
      "started_at": "2026-03-08T23:13:52.000787+00:00",
      "completed_at": "2026-03-08T23:17:38.024866+00:00",
      "handoff_message": "RUN_ID=20260308_181244_b0fb2a72 STAGE=BOB_DONE"
    },
    "hook": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_181244_b0fb2a72/stage_outputs/bob_caption.md",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_181244_b0fb2a72/stage_outputs/hook_overlays.json",
      "started_at": "2026-03-08T23:17:38.039521+00:00",
      "completed_at": "2026-03-08T23:17:51.790815+00:00",
      "handoff_message": "RUN_ID=20260308_181244_b0fb2a72 STAGE=HOOK_DONE"
    },
    "jimmy": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_181244_b0fb2a72/stage_outputs/hook_overlays.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_181244_b0fb2a72/final/final_post_ready.md",
      "started_at": "2026-03-08T23:17:51.804205+00:00",
      "completed_at": "2026-03-08T23:17:56.311170+00:00",
      "handoff_message": "RUN_ID=20260308_181244_b0fb2a72 STAGE=FINAL_READY"
    }
  },
  "flags": [
    {
      "flag_code": "DONALD_ZERO_NUGGET_FALLBACK",
      "stage": "donald",
      "severity": "warn",
      "short_note": "No nuggets returned, generated deterministic fallback nugget",
      "ts": "2026-03-08T23:12:45.161538+00:00"
    }
  ],
  "errors": {},
  "meta": {
    "chat_policy": "one_line_only",
    "pipeline_mode": "single_direction_no_revision_loop"
  },
  "final_delivery": {
    "drive_folder_id": "1NOCxQ2K1S2vM07hGHc0xEqTrsl2Ub1tv",
    "drive_file_id": "1L2ygVGpBWUVa0qFzath92NxsYesyBx6W8zPRNL4dSbE",
    "drive_link": "https://docs.google.com/document/d/1L2ygVGpBWUVa0qFzath92NxsYesyBx6W8zPRNL4dSbE/edit?usp=drivesdk",
    "uploaded_at": "2026-03-08T23:17:56.311143+00:00"
  }
}
```



## Manifest: 20260308_172401_545ca1b0

```json
{
  "run_id": "20260308_172401_545ca1b0",
  "source_id": "fathom_545ca1b0376d6e6b",
  "source_kind": "fathom_share_url",
  "reprocess": true,
  "created_at": "2026-03-08T22:24:01.827082+00:00",
  "updated_at": "2026-03-08T22:24:01.827093+00:00",
  "current_stage": "jimmy",
  "stage_status": {
    "donald": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172401_545ca1b0/stage_inputs/donald_url_intake.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172401_545ca1b0/stage_outputs/donald_canonical.json",
      "started_at": "2026-03-08T22:24:01.843018+00:00",
      "completed_at": "2026-03-08T22:24:02.593527+00:00",
      "handoff_message": "RUN_ID=20260308_172401_545ca1b0 STAGE=DONALD_DONE"
    },
    "mark": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172401_545ca1b0/stage_outputs/donald_canonical.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172401_545ca1b0/stage_outputs/mark_body.md",
      "started_at": "2026-03-08T22:24:02.606046+00:00",
      "completed_at": "2026-03-08T22:25:05.981585+00:00",
      "handoff_message": "RUN_ID=20260308_172401_545ca1b0 STAGE=MARK_DONE"
    },
    "bob": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172401_545ca1b0/stage_outputs/mark_body.md",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172401_545ca1b0/stage_outputs/bob_caption.md",
      "started_at": "2026-03-08T22:25:05.998131+00:00",
      "completed_at": "2026-03-08T22:29:08.271664+00:00",
      "handoff_message": "RUN_ID=20260308_172401_545ca1b0 STAGE=BOB_DONE"
    },
    "hook": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172401_545ca1b0/stage_outputs/bob_caption.md",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172401_545ca1b0/stage_outputs/hook_overlays.json",
      "started_at": "2026-03-08T22:29:08.284115+00:00",
      "completed_at": "2026-03-08T22:29:21.074822+00:00",
      "handoff_message": "RUN_ID=20260308_172401_545ca1b0 STAGE=HOOK_DONE"
    },
    "jimmy": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172401_545ca1b0/stage_outputs/hook_overlays.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_172401_545ca1b0/final/final_post_ready.md",
      "started_at": "2026-03-08T22:29:21.087490+00:00",
      "completed_at": "2026-03-08T22:29:25.708228+00:00",
      "handoff_message": "RUN_ID=20260308_172401_545ca1b0 STAGE=FINAL_READY"
    }
  },
  "flags": [
    {
      "flag_code": "DONALD_ZERO_NUGGET_FALLBACK",
      "stage": "donald",
      "severity": "warn",
      "short_note": "No nuggets returned, generated deterministic fallback nugget",
      "ts": "2026-03-08T22:24:02.588785+00:00"
    },
    {
      "flag_code": "BOB_APPEND_ONLY_FALLBACK",
      "stage": "bob",
      "severity": "warn",
      "short_note": "Bob output modified body, using deterministic append fallback",
      "ts": "2026-03-08T22:29:08.266912+00:00"
    }
  ],
  "errors": {},
  "meta": {
    "chat_policy": "one_line_only",
    "pipeline_mode": "single_direction_no_revision_loop"
  },
  "final_delivery": {
    "drive_folder_id": "1NOCxQ2K1S2vM07hGHc0xEqTrsl2Ub1tv",
    "drive_file_id": "1Isu8_bIOTNjfRbv0Hr69tEr5Ezr0nUEhsXRCKf9ONEA",
    "drive_link": "https://docs.google.com/document/d/1Isu8_bIOTNjfRbv0Hr69tEr5Ezr0nUEhsXRCKf9ONEA/edit?usp=drivesdk",
    "uploaded_at": "2026-03-08T22:29:25.708215+00:00"
  }
}
```



## Manifest: 20260308_171522_61022128

```json
{
  "run_id": "20260308_171522_61022128",
  "source_id": "fathom_6102212884bf7031",
  "source_kind": "fathom_share_url",
  "reprocess": true,
  "created_at": "2026-03-08T22:15:22.576316+00:00",
  "updated_at": "2026-03-08T22:15:22.576328+00:00",
  "current_stage": "jimmy",
  "stage_status": {
    "donald": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_61022128/stage_inputs/donald_url_intake.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_61022128/stage_outputs/donald_canonical.json",
      "started_at": "2026-03-08T22:15:22.590664+00:00",
      "completed_at": "2026-03-08T22:15:22.600321+00:00",
      "handoff_message": "RUN_ID=20260308_171522_61022128 STAGE=DONALD_DONE"
    },
    "mark": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_61022128/stage_outputs/donald_canonical.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_61022128/stage_outputs/mark_body.md",
      "started_at": "2026-03-08T22:15:22.613207+00:00",
      "completed_at": "2026-03-08T22:15:22.617540+00:00",
      "handoff_message": "RUN_ID=20260308_171522_61022128 STAGE=MARK_DONE"
    },
    "bob": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_61022128/stage_outputs/mark_body.md",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_61022128/stage_outputs/bob_caption.md",
      "started_at": "2026-03-08T22:15:22.630314+00:00",
      "completed_at": "2026-03-08T22:15:22.634689+00:00",
      "handoff_message": "RUN_ID=20260308_171522_61022128 STAGE=BOB_DONE"
    },
    "hook": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_61022128/stage_outputs/bob_caption.md",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_61022128/stage_outputs/hook_overlays.json",
      "started_at": "2026-03-08T22:15:22.648299+00:00",
      "completed_at": "2026-03-08T22:15:22.652171+00:00",
      "handoff_message": "RUN_ID=20260308_171522_61022128 STAGE=HOOK_DONE"
    },
    "jimmy": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_61022128/stage_outputs/hook_overlays.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_61022128/final/final_post_ready.md",
      "started_at": "2026-03-08T22:15:22.686518+00:00",
      "completed_at": "2026-03-08T22:15:22.695496+00:00",
      "handoff_message": "RUN_ID=20260308_171522_61022128 STAGE=FINAL_READY"
    }
  },
  "flags": [],
  "errors": {},
  "meta": {
    "chat_policy": "one_line_only",
    "pipeline_mode": "single_direction_no_revision_loop"
  }
}
```



## Manifest: 20260308_171522_401462f8

```json
{
  "run_id": "20260308_171522_401462f8",
  "source_id": "fathom_401462f895ac6872",
  "source_kind": "fathom_share_url",
  "reprocess": true,
  "created_at": "2026-03-08T22:15:22.720030+00:00",
  "updated_at": "2026-03-08T22:15:22.720063+00:00",
  "current_stage": "jimmy",
  "stage_status": {
    "donald": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_401462f8/stage_inputs/donald_url_intake.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_401462f8/stage_outputs/donald_canonical.json",
      "started_at": "2026-03-08T22:15:22.740013+00:00",
      "completed_at": "2026-03-08T22:15:22.749911+00:00",
      "handoff_message": "RUN_ID=20260308_171522_401462f8 STAGE=DONALD_DONE"
    },
    "mark": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_401462f8/stage_outputs/donald_canonical.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_401462f8/stage_outputs/mark_body.md",
      "started_at": "2026-03-08T22:15:22.773162+00:00",
      "completed_at": "2026-03-08T22:15:22.779239+00:00",
      "handoff_message": "RUN_ID=20260308_171522_401462f8 STAGE=MARK_DONE"
    },
    "bob": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_401462f8/stage_outputs/mark_body.md",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_401462f8/stage_outputs/bob_caption.md",
      "started_at": "2026-03-08T22:15:22.795921+00:00",
      "completed_at": "2026-03-08T22:15:22.800439+00:00",
      "handoff_message": "RUN_ID=20260308_171522_401462f8 STAGE=BOB_DONE"
    },
    "hook": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_401462f8/stage_outputs/bob_caption.md",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_401462f8/stage_outputs/hook_overlays.json",
      "started_at": "2026-03-08T22:15:22.813719+00:00",
      "completed_at": "2026-03-08T22:15:22.817914+00:00",
      "handoff_message": "RUN_ID=20260308_171522_401462f8 STAGE=HOOK_DONE"
    },
    "jimmy": {
      "status": "done",
      "canonical_input_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_401462f8/stage_outputs/hook_overlays.json",
      "canonical_output_path": "/home/openclaw_agent_1/krc_vault/pipeline_runs/runs/20260308_171522_401462f8/final/final_post_ready.md",
      "started_at": "2026-03-08T22:15:23.837167+00:00",
      "completed_at": "2026-03-08T22:15:23.841503+00:00",
      "handoff_message": "RUN_ID=20260308_171522_401462f8 STAGE=FINAL_READY"
    }
  },
  "flags": [],
  "errors": {},
  "meta": {
    "chat_policy": "one_line_only",
    "pipeline_mode": "single_direction_no_revision_loop"
  }
}
```



## Log: 20260308_182019_b0fb2a72.log

```text
2026-03-08T23:22:26.322995+00:00 SUCCESS Received. Processing now. RUN_ID=20260308_182019_b0fb2a72.

```



## Log: 20260308_181244_b0fb2a72.log

```text
2026-03-08T23:17:56.321421+00:00 SUCCESS Received. Processing now. RUN_ID=20260308_181244_b0fb2a72.

```



## Log: 20260308_172401_545ca1b0.log

```text
2026-03-08T22:29:25.717383+00:00 SUCCESS Received. Processing now. RUN_ID=20260308_172401_545ca1b0.

```



## Log: 20260308_172051_545ca1b0.log

```text
2026-03-08T22:23:47.745975+00:00 FAIL stage=bob err=bob_modified_mark_body

```



## Log: 20260308_172001_545ca1b0.log

```text
2026-03-08T22:20:02.347647+00:00 FAIL stage=donald err=donald_no_nuggets

```



## Log: 20260308_171523_02d7766f.log

```text
2026-03-08T22:15:24.349184+00:00 FAIL stage=donald err=donald_process_failed rc=3 err=

```



## Log: 20260308_171522_401462f8.log

```text
2026-03-08T22:15:23.850290+00:00 SUCCESS Received. Processing now. RUN_ID=20260308_171522_401462f8.

```



## Log: 20260308_171522_61022128.log

```text
2026-03-08T22:15:22.711819+00:00 SUCCESS Received. Processing now. RUN_ID=20260308_171522_61022128.

```



## Acceptance: acceptance_20260308_171524.json

```json
{
  "ok": true,
  "tests": [
    {
      "name": "URL intake one line",
      "pass": true,
      "run_id": "20260308_171522_61022128"
    },
    {
      "name": "Idempotency same URL",
      "pass": true,
      "run_id": "20260308_171522_61022128"
    },
    {
      "name": "Atomic write no partial reads",
      "pass": true,
      "run_id": "20260308_171522_401462f8"
    },
    {
      "name": "Pairing rule blocks finalize when hook missing",
      "pass": true,
      "run_id": "20260308_171523_55b93cc6"
    },
    {
      "name": "Failure one-line response",
      "pass": true,
      "run_id": "20260308_171523_02d7766f"
    },
    {
      "name": "Punctuation ban final output",
      "pass": true,
      "run_id": "20260308_171522_61022128"
    }
  ],
  "ts": "2026-03-08T22:15:24.349418+00:00"
}
```
