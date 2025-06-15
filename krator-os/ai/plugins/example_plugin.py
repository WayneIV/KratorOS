"""Example Krator plugin that echoes a message."""

def run(task: str) -> str:
    return f"Plugin executed: {task}"
