#!/bin/bash
# Simple project/goal planner using TaskWarrior if available
set -e

LOG=/var/log/mission_planner.log
exec >> "$LOG" 2>&1

echo "[mission] starting" $(date)

if command -v task >/dev/null; then
    task add "$*"
    echo "Task added"
else
    echo "Taskwarrior not installed" >&2
fi
