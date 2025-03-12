import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Replace with your actual bot token from BotFather
TOKEN = "7833068674:AAG_PR50ylOFF7KtL_W0VJmF4KdRliD-Vr0"

# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot. Type 'hi' or 'hlo' to chat with me.")

# Message handler to reply with custom messages
async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()  # Convert to lowercase for better matching

    if user_text == "hi" or user_text == "hlo":
        await update.message.reply_text("Hey there! How can I help you?")
    elif user_text == "how are you":
        await update.message.reply_text("I'm just a bot, but I'm doing great! 😊 What about you?")
    elif user_text == "hibathulla aara?":
        await update.message.reply_text("Hibathulla is the king of KMCT CAHS 👑")
    else:
        await update.message.reply_text("I'm not sure how to respond to that. Try saying 'hi' or 'hlo'!")

# Error handler
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.warning(f"Update {update} caused error {context.error}")

# Main function to run the bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))
    
    # Error handler
    app.add_error_handler(error_handler)

    # Start polling
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
