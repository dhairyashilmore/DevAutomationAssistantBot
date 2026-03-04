"""Telegram bot entrypoint and handler registration."""
from telegram.ext import ApplicationBuilder, CommandHandler
from .command_handler import handle_run_command
import logging

from ..config import TELEGRAM_TOKEN

logger = logging.getLogger(__name__)


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("run", handle_run_command))

    logger.info("Bot started polling")
    app.run_polling()


if __name__ == "__main__":
    main()
