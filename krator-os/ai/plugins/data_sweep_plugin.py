"""Run the data_sweep.sh script and return its output."""

import subprocess
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[2] / 'scripts' / 'data_sweep.sh'


def run(args: str) -> str:
    cmd = [str(SCRIPT)]
    if args:
        cmd.extend(args.split())
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as exc:
        return f"[data sweep error: {exc}]"

