#!/usr/bin/env python3
"""Krator AI assistant daemon.

This daemon loads configuration from /etc/krator/krator.conf and provides a
simple CLI interface for interacting with local language models or the OpenAI
API as a fallback.
"""
import configparser
import subprocess
import sys
import time
from pathlib import Path

CONFIG_PATH = Path('/etc/krator/krator.conf')


def load_config(path: Path) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    if path.exists():
        cfg.read(path)
    else:
        cfg['general'] = {'model': 'gpt4all', 'openai_key': ''}
    return cfg


def run_local_model(prompt: str, model_cmd: str = 'llama.cpp') -> str:
    """Run a local LLM command and return output."""
    try:
        result = subprocess.run([model_cmd, '--prompt', prompt], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as exc:
        return f"[error running local model: {exc}]"


def run_openai(prompt: str, api_key: str) -> str:
    try:
        import openai
    except ImportError:
        return '[openai module missing]'
    openai.api_key = api_key
    try:
        resp = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': prompt}])
        return resp.choices[0].message['content']
    except Exception as exc:
        return f"[openai error: {exc}]"


def main():
    cfg = load_config(CONFIG_PATH)
    model = cfg['general'].get('model', 'gpt4all')
    api_key = cfg['general'].get('openai_key', '')

    print('Krator AI daemon started. Type a prompt and press enter.')
    for line in sys.stdin:
        prompt = line.strip()
        if not prompt:
            continue
        if model == 'openai' and api_key:
            response = run_openai(prompt, api_key)
        else:
            response = run_local_model(prompt)
        print(response)
        sys.stdout.flush()
        time.sleep(0.1)


if __name__ == '__main__':
    main()
