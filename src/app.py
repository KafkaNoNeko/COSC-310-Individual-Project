#!/usr/bin/env python

import yaml
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from utils.handle_messages import chat_bot_response


with open("env.yaml", "r") as env_file:
    ENV_VARIABLES = yaml.safe_load(env_file)
    TOKEN = ENV_VARIABLES["TOKEN"]


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def handle_message(update: Update, context: CallbackContext) -> None:
    """Handle the user message."""
    update.message.reply_text(
        chat_bot_response(update.message.text)
    )


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # /start - says hello
    dispatcher.add_handler(CommandHandler("start", start))

    # On every other message  - handle the message answering content about Elon Musk
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until proccess is closed (Ctrl-C)
    updater.idle()


if __name__ == '__main__':
    main()
