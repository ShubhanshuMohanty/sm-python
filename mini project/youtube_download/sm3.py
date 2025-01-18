from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from deep_translator import GoogleTranslator

# Start command function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Namaste! Mujhse kuch bhi likhiye, main usse Hindi me translate karke dunga!")

# Message handler function
async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    translated = GoogleTranslator(source='auto', target='hi').translate(text)
    await update.message.reply_text(f"Translated to Hindi: {translated}")

# Main function
def main():
    # Replace 'YOUR_BOT_API_TOKEN' with your bot's API token
    API_TOKEN = '7665147355:AAF4UgSgmHjdwZHaarp9oQfvtt0fbO6WsbM'

    # Application builder
    app = ApplicationBuilder().token(API_TOKEN).build()

    # Command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))

    # Start the bot
    app.run_polling()

if __name__ == "__main__":
    main()
