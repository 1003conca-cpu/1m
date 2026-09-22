from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
state = root / "project-control" / "PROJECT_STATE.md"
status_file = root / "status" / "CURRENT_STATUS.md"

project_state = "UNKNOWN"
if state.exists():
    for line in state.read_text(encoding="utf-8").splitlines():
        if line.startswith("STATUS:"):
            project_state = line.split(":", 1)[1].strip()
            break

now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

content = f"""# CURRENT STATUS

Last heartbeat: {now}

System: AGENT_CONTROL_CENTER
Overall status: {project_state}

Agents:
- Planner: READY
- Coder: READY
- Reviewer: READY
- Release Manager: READY
- Deploy Agent: READY
- State Monitor: RUNNING

Source of truth: GitHub
Heartbeat target: every 5 minutes

This file is generated automatically by the status heartbeat workflow.
"""
status_file.write_text(content, encoding="utf-8")
