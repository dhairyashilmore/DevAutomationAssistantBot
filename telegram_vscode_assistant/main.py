"""Start the DevAutomationAssistantBot."""
import logging
from .bot.telegram_bot import main as run_bot


def setup_logging():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )


def main():
    setup_logging()
    run_bot()


if __name__ == "__main__":
    main()
