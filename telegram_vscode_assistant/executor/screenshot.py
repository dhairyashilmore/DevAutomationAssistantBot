"""Screenshot helper using pyautogui."""
import pyautogui
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def take_screenshot(output_path: Path):
    try:
        logger.info("Taking screenshot to %s", output_path)
        img = pyautogui.screenshot()
        img.save(output_path)
        return output_path
    except Exception as e:
        logger.error("Screenshot error: %s", e)
        return None
