"""Krator AI assistant agent using the asyncio message bus."""
import asyncio
import configparser
import importlib.util
import subprocess
import sys
from pathlib import Path

from ..core.message_bus import MessageBus

CONFIG_PATH = Path('/etc/krator/krator.conf')
PLUGIN_DIR = Path(__file__).parent / 'plugins'
VERSION = '0.1'


def load_config(path: Path) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    if path.exists():
        cfg.read(path)
    else:
        cfg['general'] = {'model': 'gpt4all', 'openai_key': ''}
    return cfg


def run_local_model(prompt: str, model_cmd: str = 'llama.cpp') -> str:
    try:
        result = subprocess.run(
            [model_cmd, '--prompt', prompt], capture_output=True,
            text=True, check=True)
        return result.stdout.strip()
    except Exception as exc:
        return f"[error running local model: {exc}]"


def run_plugin(command: str, rest: str) -> str:
    module_path = f"{command}_plugin"
    try:
        spec = importlib.util.spec_from_file_location(
            module_path, PLUGIN_DIR / f"{module_path}.py")
        if spec and spec.loader:
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if hasattr(mod, 'run'):
                return mod.run(rest)
    except FileNotFoundError:
        pass
    return ''


def run_openai(prompt: str, api_key: str) -> str:
    try:
        import openai
    except ImportError:
        return '[openai module missing]'
    openai.api_key = api_key
    try:
        resp = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}])
        return resp.choices[0].message['content']
    except Exception as exc:
        return f"[openai error: {exc}]"


class AssistantAgent:
    def __init__(self, bus: MessageBus):
        self.bus = bus
        cfg = load_config(CONFIG_PATH)
        self.model = cfg['general'].get('model', 'gpt4all')
        self.api_key = cfg['general'].get('openai_key', '')

    async def handle_prompt(self, prompt: str) -> str:
        if prompt.startswith('!'):
            cmd, *rest = prompt[1:].split(maxsplit=1)
            output = run_plugin(cmd, rest[0] if rest else '')
            if output:
                return output
        if self.model == 'openai' and self.api_key:
            return run_openai(prompt, self.api_key)
        return run_local_model(prompt)

    async def run(self) -> None:
        queue = self.bus.subscribe('prompt')
        while True:
            prompt = await queue.get()
            response = await self.handle_prompt(prompt)
            await self.bus.publish('response', response)


async def main() -> None:
    if '--version' in sys.argv:
        print(VERSION)
        return

    bus = MessageBus()
    agent = AssistantAgent(bus)
    asyncio.create_task(agent.run())

    resp_queue = bus.subscribe('response')
    print('Krator AI daemon started. Type a prompt and press enter.')
    loop = asyncio.get_event_loop()
    while True:
        line = await loop.run_in_executor(None, sys.stdin.readline)
        if not line:
            break
        prompt = line.strip()
        if not prompt:
            continue
        await bus.publish('prompt', prompt)
        response = await resp_queue.get()
        print(response)
        sys.stdout.flush()
        await asyncio.sleep(0.1)


if __name__ == '__main__':
    asyncio.run(main())
