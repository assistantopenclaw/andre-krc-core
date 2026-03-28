#!/bin/bash
# Start TenacitOS Mission Control
pkill -f "npm start" 2>/dev/null || true
sleep 1
cd /home/openclaw_agent_1/.openclaw/workspace/mission-control
nohup npm start >> /home/openclaw_agent_1/.openclaw/tunnels/tenacitOS.log 2>&1 &
echo "Mission Control started PID $!"
