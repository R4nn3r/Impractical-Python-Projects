import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging 
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and context 
def start(update: Update, context: CallbackContext) -> None:
    """ send a message when the command start is issued """
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\\!',
        reply_markup = ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """ send a message when the command help is issued """
    update.message.reply_text("Help!")


def echo(update: Update, context: CallbackContext) -> None:
    """ Echo the user message. """
    update.message.reply_text(update.message.text)


def main() -> None:
    """ Start the bot. """
    # Create the updater and pass it your bot's token
    updater = Updater('5689199294:AAHxCGU6LgWkJRHNr2DfyM5n9AMY9168nwQ')

    # Get the dispatcher to register handlers 
    dispatcher = updater.dispatcher

    # On different commands - answer in Telegram 
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))


    # On non command i.e message - echo the message on Telegram 
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


    # Start the bot 
    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
