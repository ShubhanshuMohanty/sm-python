from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Command function to start the bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! Please type your name.')

# Function to handle the user's name input
async def handle_name(update: Update, context: CallbackContext) -> None:
    user_name = update.message.text
    await update.message.reply_text(f"Hello {user_name}!")

# Main function to run the bot
def main():
    print("Starting bot...")
    # Replace 'YOUR_BOT_TOKEN' with your bot's token
    application = Application.builder().token("7665147355:AAF4UgSgmHjdwZHaarp9oQfvtt0fbO6WsbM").build()

    # Register command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Register message handler for text messages (user's name)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_name))

    # Start the bot
    application.run_polling()
    print("Bot started!")

if __name__ == '__main__':
    main()
