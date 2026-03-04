# DevAutomationAssistantBot

Telegram bot that integrates with **VS Code** and **GitHub Copilot** for automated code generation and modification.

## Features

- ✅ Telegram `/run <prompt>` command interface
- ✅ Real code generation via **OpenAI API** (Copilot-like)
- ✅ Intelligent file insertion into your project
- ✅ **VS Code integration** — automatically opens modified files
- ✅ Screenshots of workspace changes sent back to Telegram
- ✅ Error handling and fallback responses

## Structure

```
telegram_vscode_assistant/
├── bot/
│   ├── telegram_bot.py
│   └── command_handler.py
├── ai/
│   └── ai_prompt_handler.py      # OpenAI API integration
├── executor/
│   ├── command_executor.py
│   ├── file_editor.py            # Smart code insertion
│   ├── screenshot.py
│   └── vscode_integration.py     # Opens files in VS Code
├── config.py
├── requirements.txt
├── main.py
└── README.md
```

## Quick Start

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Get OpenAI API key:**
   - Go to https://platform.openai.com/account/api-keys
   - Create and copy your key

3. **Configure bot:**
   - Edit `config.py`
   - Set `OPENAI_API_KEY` to your key
   - Verify `TELEGRAM_TOKEN` is set

4. **Run bot:**
   ```powershell
   python -m telegram_vscode_assistant.main
   ```

5. **Use in Telegram:**
   ```
   /run add login button to HomePage.jsx
   /run create password validation function
   /run write unit tests
   ```

## How It Works

1. User sends `/run <prompt>` in Telegram
2. Bot calls OpenAI API to generate real code
3. Bot finds target file in your project
4. Bot inserts code intelligently
5. Bot opens file in VS Code
6. Bot takes screenshot
7. Bot replies with status + screenshot

## Detailed Setup

See [VSCODE_COPILOT_SETUP.md](VSCODE_COPILOT_SETUP.md) for complete configuration and troubleshooting.

## Configuration

Edit `config.py`:

```python
TELEGRAM_TOKEN = "..."           # Your Telegram bot token
OPENAI_API_KEY = "sk-proj-..."   # Your OpenAI API key
OPENAI_MODEL = "gpt-4o-mini"     # or "gpt-4"
PROJECT_DIR = Path.cwd()         # Project to edit
VSCODE_EXECUTABLE = "code"       # VS Code CLI path
```

## Requirements

- Python 3.8+
- VS Code (for opening files)
- OpenAI API key (for real code generation)
- Active Telegram bot token

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Bot doesn't respond | Check Telegram token in config.py |
| ModuleNotFoundError: openai | `pip install openai` |
| VS Code doesn't open | Ensure `code` is in PATH or set `VSCODE_EXECUTABLE` |
| Poor code quality | Use `gpt-4` model instead of `gpt-4o-mini` |
| API errors | Check OpenAI API key validity |

## Next Steps

- Replace AI stub with real LLM (done via OpenAI)
- Add VS Code extension for deeper integration (optional)
- Implement code review/approval workflow
- Add support for multiple programming languages

---

**Ready to automate your coding workflow!** 🚀

