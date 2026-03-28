#!/bin/bash
# Keep Mission Control alive + update permanent redirect

LOG=/home/openclaw_agent_1/.openclaw/tunnels/keep-alive.log
PIDFILE=/home/openclaw_agent_1/.openclaw/tunnels/tunnel.pid
URLFILE=/home/openclaw_agent_1/.openclaw/tunnels/tunnel.url

echo "$(date): Check starting..." >> $LOG

# Restart app if down
if ! curl -s http://localhost:3000/login > /dev/null 2>&1; then
  echo "$(date): App down, restarting..." >> $LOG
  pkill -f "npm start" 2>/dev/null
  sleep 2
  cd /home/openclaw_agent_1/.openclaw/workspace/mission-control
  nohup npm start >> /home/openclaw_agent_1/.openclaw/tunnels/tenacitOS.log 2>&1 &
  sleep 4
  echo "$(date): App restarted" >> $LOG
fi

# Restart tunnel if process is dead
if ! pgrep -f "cloudflared tunnel" > /dev/null 2>&1; then
  echo "$(date): Tunnel process dead, restarting..." >> $LOG
  pkill -f "cloudflared" 2>/dev/null
  sleep 3
  cd /home/openclaw_agent_1/.openclaw/workspace/mission-control
  nohup cloudflared tunnel --url http://localhost:3000 > /home/openclaw_agent_1/.openclaw/tunnels/tenacitOS-tunnel.log 2>&1 &
  sleep 8
  NEW_URL=$(grep -o 'https://[^ ]*trycloudflare.com' /home/openclaw_agent_1/.openclaw/tunnels/tenacitOS-tunnel.log | tail -1)
  echo "$NEW_URL" > $URLFILE
  echo "$(date): Tunnel restarted at $NEW_URL" >> $LOG
  # Update GitHub redirect
  /home/openclaw_agent_1/.openclaw/scripts/update-redirect.sh
else
  # Tunnel running — verify it's reachable and update redirect if URL changed
  CURRENT_CF_URL=$(curl -s -o /dev/null -w "%{url_effective}" --max-time 5 "https://toys-cached-conjunction-palm.trycloudflare.com/login" 2>/dev/null | sed 's|/login||')
  STORED_URL=$(cat $URLFILE 2>/dev/null)
  if [ "$CURRENT_CF_URL" != "$STORED_URL" ] && [ -n "$CURRENT_CF_URL" ]; then
    echo "$(date): URL drift detected ($STORED_URL -> $CURRENT_CF_URL), updating redirect" >> $LOG
    echo "$CURRENT_CF_URL" > $URLFILE
    /home/openclaw_agent_1/.openclaw/scripts/update-redirect.sh
  fi
fi
