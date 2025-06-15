#!/usr/bin/env python3
"""Krator CLI interface to talk to the Krator AI daemon or local models."""
import argparse
import subprocess
import sys
from pathlib import Path

CONFIG_PATH = Path('/etc/krator/krator.conf')
DAEMON_CMD = ['krator-daemon']


def call_daemon(prompt: str) -> str:
    """Send prompt to running daemon via subprocess."""
    try:
        proc = subprocess.run(DAEMON_CMD, input=prompt, text=True,
                              capture_output=True, check=True)
        return proc.stdout.strip()
    except Exception as exc:
        return f"[daemon error: {exc}]"


def main() -> None:
    parser = argparse.ArgumentParser(description="Interact with Krator AI")
    parser.add_argument('prompt', nargs='*', help='Prompt to send')
    args = parser.parse_args()
    prompt = ' '.join(args.prompt).strip()
    if not prompt:
        prompt = sys.stdin.read().strip()
    if not prompt:
        print('No prompt given')
        return
    response = call_daemon(prompt)
    print(response)


if __name__ == '__main__':
    main()
