#!/usr/bin/env python3
"""First-boot configuration wizard."""
import getpass
import json
from pathlib import Path

ENV_PATH = Path('/etc/krator/.env')


def prompt(question: str, default: str = '') -> str:
    value = input(f"{question} [{default}]: ")
    return value.strip() or default


def main() -> None:
    print("Krator OS First Boot")
    role = prompt("Select role (Founder/Analyst/Engineer)", 'Engineer')
    security = prompt("Security mode (standard/hardened)", 'standard')
    assistant = prompt("Assistant type (local/API)", 'local')
    github = prompt("GitHub username for sync", '')
    api_key = getpass.getpass("OpenAI API Key (optional): ")

    cfg = {
        'ROLE': role,
        'SECURITY_MODE': security,
        'ASSISTANT': assistant,
        'GITHUB_USER': github,
        'OPENAI_KEY': api_key,
    }
    ENV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with ENV_PATH.open('w') as fh:
        for k, v in cfg.items():
            fh.write(f"{k}={v}\n")
    print(f"Configuration written to {ENV_PATH}")


if __name__ == '__main__':
    main()
