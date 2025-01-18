# bot.py
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from translation import translate_text  # Import translate_text from translation.py

# The echo function
async def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    loop = asyncio.get_event_loop()
    # Run the blocking translate_text function in a separate thread using run_in_executor
    translated_text = await loop.run_in_executor(None, translate_text, user_message)
    await update.message.reply_text(translated_text)

# Main function to run the bot
def main():
    application = Application.builder().token("7665147355:AAF4UgSgmHjdwZHaarp9oQfvtt0fbO6WsbM").build()

    # Register message handler for echoing messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
