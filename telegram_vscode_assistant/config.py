from pathlib import Path

# Telegram bot token
TELEGRAM_TOKEN = "8704651998:AAEQoy8qC-RSYh-tqwyF3BdpRcNnis1ISMc"

# OpenAI API key (replaces stub AI with real Copilot-like code generation)
# Get your key from https://platform.openai.com/account/api-keys
OPENAI_API_KEY = "sk-proj-YOUR_OPENAI_API_KEY_HERE"
OPENAI_MODEL = "gpt-4o-mini"  # or "gpt-4" for better quality

# directory of the project to edit
PROJECT_DIR = Path.cwd()

# screenshot output file
SCREENSHOT_PATH = PROJECT_DIR / "vscode_screenshot.png"

# VS Code settings
VSCODE_EXECUTABLE = "code"  # path to VS Code CLI
VSCODE_WORKSPACE = Path.cwd()  # workspace folder to open in VS Code

