# VS Code Copilot Integration Setup

This guide explains how to connect your Telegram bot with VS Code Copilot for real code generation.

## Overview

The bot now supports:
- **Real code generation** via OpenAI API (powers Copilot)
- **Intelligent file insertion** into your project
- **VS Code integration** to open modified files
- **Screenshots** of your workspace after edits

## Setup Steps

### Step 1: Get an OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/account/api-keys)
2. Sign up or log in
3. Create a new API key
4. Copy the key (starts with `sk-`)

### Step 2: Update Configuration

Edit `telegram_vscode_assistant/config.py` and replace:

```python
OPENAI_API_KEY = "sk-proj-YOUR_OPENAI_API_KEY_HERE"
```

with your actual key:

```python
OPENAI_API_KEY = "sk-proj-abc123xyz..."
```

### Step 3: Ensure VS Code is installed

The bot opens files in VS Code automatically. Make sure:

```powershell
code --version  # should display VS Code version
```

If not installed or not in PATH, update `VSCODE_EXECUTABLE` in config.py:

```python
VSCODE_EXECUTABLE = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
```

### Step 4: Install OpenAI Library

```powershell
pip install openai
```

### Step 5: Run the Bot

```powershell
python -m telegram_vscode_assistant.main
```

## How It Works

1. **User sends Telegram command:**
   ```
   /run add a login button to HomePage.jsx
   ```

2. **Bot processes:**
   - Sends prompt to OpenAI API
   - Receives real code (not placeholder)
   - Finds target file in your project
   - Inserts code intelligently
   - Opens file in VS Code
   - Takes screenshot

3. **Bot replies with:**
   - Status message (✅ success or ❌ error)
   - Screenshot of VS Code showing the changes

## Example Commands

```
/run add error handling to the api client
/run create a responsive navbar component
/run add unit tests for the login function
/run optimize database queries in models.py
/run create a config module for environment variables
```

## Configuration Options

In `config.py`:

```python
OPENAI_MODEL = "gpt-4o-mini"  # or "gpt-4" for better quality
OPENAI_API_KEY = "your-key"
PROJECT_DIR = Path.cwd()  # directory to scan for files
VSCODE_EXECUTABLE = "code"  # path to VS Code CLI
```

## Cost Estimation

- OpenAI API is usage-based (not free)
- GPT-4o-mini: ~$0.01-0.05 per request
- Set up monthly budget in OpenAI dashboard

## Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"
```powershell
pip install openai
```

### "API key not configured"
Check that your key in `config.py` doesn't start with `sk-proj-YOUR`

### "VS Code not opening files"
Ensure `code` command is in PATH:
```powershell
code --version
```

If not, set `VSCODE_EXECUTABLE` to full path.

### "Poor quality generated code"
Change model to better one in `config.py`:
```python
OPENAI_MODEL = "gpt-4"  # instead of gpt-4o-mini
```

## Advanced: Using GitHub Copilot Directly

If you prefer to use GitHub Copilot (which requires VS Code extension), you can:

1. Install GitHub Copilot extension in VS Code
2. Modify `vscode_integration.py` to send requests to a local VS Code server
3. Use the VS Code Extension API (requires Node.js development)

For now, OpenAI API provides the easiest integration.

## Next Steps

1. Set up your OpenAI API key
2. Start the bot
3. Open Telegram and send `/run ...` commands
4. Watch VS Code open and files get modified!

Happy coding! 🚀
