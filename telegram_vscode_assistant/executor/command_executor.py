"""Workflow orchestration: AI generation → file edit → VS Code → screenshot."""
from pathlib import Path
import logging
import time

from ..ai.ai_prompt_handler import generate_code
from .file_editor import find_target_file, insert_code_into_file
from .screenshot import take_screenshot
from .vscode_integration import open_file_in_vscode
from ..config import PROJECT_DIR, SCREENSHOT_PATH

logger = logging.getLogger(__name__)


def execute_prompt(prompt: str):
    """Execute a user prompt: generate code, modify files, open in VS Code, take screenshot."""
    try:
        # 1. Generate code using OpenAI/Copilot
        logger.info("Generating code for prompt: %s", prompt)
        generated = generate_code(prompt)
        
        if not generated or generated.startswith("//"):
            logger.warning("Code generation produced stub response")
        
        # 2. Find target file
        project_root = Path(PROJECT_DIR)
        target = find_target_file(prompt, project_root)
        logger.info("Target file: %s", target)
        
        # 3. Insert code into file
        insert_code_into_file(target, generated, position="end")
        
        # 4. Open file in VS Code
        time.sleep(0.5)  # brief delay
        opened = open_file_in_vscode(target)
        
        # 5. Wait for VS Code to appear
        time.sleep(2)
        
        # 6. Take screenshot
        screenshot = take_screenshot(SCREENSHOT_PATH)
        
        status = f"✅ Executed: '{prompt}'\n📝 Modified: {target.name}\n📸 Screenshot captured"
        return status, screenshot
    except Exception as e:
        logger.error("Execution error: %s", e)
        return f"❌ Execution failed: {e}", None

