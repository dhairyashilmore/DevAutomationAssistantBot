"""VS Code integration helpers."""
import subprocess
import logging
from pathlib import Path
from ..config import VSCODE_EXECUTABLE, VSCODE_WORKSPACE

logger = logging.getLogger(__name__)


def open_file_in_vscode(file_path: Path) -> bool:
    """Open a file in VS Code."""
    try:
        logger.info("Opening %s in VS Code", file_path)
        subprocess.Popen([VSCODE_EXECUTABLE, str(file_path), "--new-window"])
        return True
    except Exception as e:
        logger.error("Failed to open file in VS Code: %s", e)
        return False


def open_workspace_in_vscode(workspace_path: Path = None) -> bool:
    """Open VS Code workspace."""
    try:
        path = workspace_path or VSCODE_WORKSPACE
        logger.info("Opening VS Code workspace: %s", path)
        subprocess.Popen([VSCODE_EXECUTABLE, str(path)])
        return True
    except Exception as e:
        logger.error("Failed to open workspace: %s", e)
        return False


def run_vscode_command(command: str) -> bool:
    """Run a VS Code command (e.g., editing via CLI)."""
    try:
        logger.info("Running VS Code command: %s", command)
        subprocess.run(command, shell=True, check=True)
        return True
    except Exception as e:
        logger.error("Command failed: %s", e)
        return False
