#!/bin/bash
# Run the Krator AI daemon
set -e

# Activate virtual environment if present
if [ -f "venv/bin/activate" ]; then
    . "venv/bin/activate"
elif [ -f ".venv/bin/activate" ]; then
    . ".venv/bin/activate"
fi

exec python3 krator-os/ai/krator_daemon.py "$@"
