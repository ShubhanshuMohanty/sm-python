from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from googletrans import Translator

# from translation import translate_text

# Function to echo the user's message
async def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    translator = Translator()
    translated = translator.translate(user_message, src='en', dest='hi')
    # translated_text = translate_text(user_message)  # Call the sync function directly
    await update.message.reply_text(translated.text)

# Main function to run the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your bot's token
    application = Application.builder().token("7665147355:AAF4UgSgmHjdwZHaarp9oQfvtt0fbO6WsbM").build()

    # Register message handler for echoing messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
