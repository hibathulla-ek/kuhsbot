import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,  # Change to DEBUG for more detailed logs
)
logger = logging.getLogger(__name__)

# Replace with your actual bot token (use environment variables for security)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7833068674:AAG_PR50yIOFF7KtL_W0VJmF4KdRliD-Vr0")

# Dictionary of responses
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hey there! 😊",
    "how are you": "I'm a bot, I’m always fine! How about you?",
    "thank you": "You're welcome! 😊",
    "bye": "Goodbye! See you soon.",
    "what is your name": "kundra jony!",
    "who created you": "arinjitt nthina myre! 😎",
    "tell me about kaleelinte andi": "kaleelinte andi cheruth aan nn ellarkm ariya! 😆",
    "what is gravity": "Gravity is the force that attracts objects toward the center of the Earth.",
    "can you dance": "I can't dance, but I can imagine it! 🕺",
    "do you sleep": "I don’t need sleep, I am always here for you!",
    "what's 2+2": "2+2 is 4! Easy math. 😃",
    "do you know math": "Yes! I can do basic math, try me!",
}

# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Chat with me, I can reply to many different messages!")

# Function to reply to messages
async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()  # Convert to lowercase
    response_text = responses.get(user_text, "I don’t understand that yet, but I'm learning!")
    await update.message.reply_text(response_text)

# Handler for unknown commands
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sorry, I don't recognize that command.")

# Error handler
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Update {update} caused error: {context.error}")
    await update.message.reply_text("Oops! Something went wrong. Please try again later.")

# Main function
def main():
    app = Application.builder().token(TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))  # Handle unknown commands
    app.add_error_handler(error_handler)  # Handle errors
    
    # Start polling
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()



