import sys
from pathlib import Path
import subprocess

AI_PATH = Path(__file__).resolve().parents[1] / 'krator-os' / 'ai'
if str(AI_PATH) not in sys.path:
    sys.path.insert(0, str(AI_PATH))

from krator_daemon import load_config, run_local_model


def test_load_config_default(tmp_path):
    cfg = load_config(tmp_path / 'missing.conf')
    assert cfg['general']['model'] == 'gpt4all'
    assert cfg['general']['openai_key'] == ''


def test_load_config_existing(tmp_path):
    path = tmp_path / 'krator.conf'
    path.write_text('[general]\nmodel=openai\nopenai_key=abc\n')
    cfg = load_config(path)
    assert cfg['general']['model'] == 'openai'
    assert cfg['general']['openai_key'] == 'abc'


def test_load_config_missing_section(tmp_path):
    path = tmp_path / 'krator.conf'
    path.write_text('[other]\nkey=value\n')
    cfg = load_config(path)
    assert cfg['general']['model'] == 'gpt4all'
    assert cfg['general']['openai_key'] == ''


def test_run_local_model_success(monkeypatch):
    def fake_run(args, capture_output, text, check):
        class Res:
            stdout = 'ok'
        fake_run.called = args
        return Res()

    monkeypatch.setattr(subprocess, 'run', fake_run)
    output = run_local_model('prompt', model_cmd='cmd')
    assert fake_run.called == ['cmd', '--prompt', 'prompt']
    assert output == 'ok'


def test_run_local_model_error(monkeypatch):
    def fake_run(*args, **kwargs):
        raise subprocess.CalledProcessError(returncode=1, cmd=kwargs.get('args', args[0]))

    monkeypatch.setattr(subprocess, 'run', fake_run)
    output = run_local_model('prompt', model_cmd='cmd')
    assert output.startswith('[error running local model:')
