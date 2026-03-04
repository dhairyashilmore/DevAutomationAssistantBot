"""Parse incoming Telegram commands and delegate to executor."""
from telegram import Update
from telegram.ext import ContextTypes

from ..executor.command_executor import execute_prompt
import logging

logger = logging.getLogger(__name__)


async def handle_run_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt_text = " ".join(context.args) if context.args else ""
    if not prompt_text:
        await update.message.reply_text("Please provide a prompt after /run.")
        return

    logger.info("Received prompt: %s", prompt_text)
    status, screenshot_path = execute_prompt(prompt_text)

    await update.message.reply_text(status)
    if screenshot_path:
        await update.message.reply_photo(photo=open(screenshot_path, "rb"))
