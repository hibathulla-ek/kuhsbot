import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot Token
TOKEN = "7833068674:AAGYlqHpVABWyFipJtJoZ3g4d5QD5W3mMc8"

# Dictionary of questions and file paths
NOTES = {
    "anatomy of lung": "notes/anatomy_lung.pdf",
    "physiology of heart": "notes/physiology_heart.pdf",
    "biochemistry basics": "notes/biochem_basics.pdf",
}

# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Ask me for notes, and I'll send the correct PDF.")

# Function to reply to messages
async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()  # Convert to lowercase

    if user_text in NOTES:  # Check if the message matches a note
        file_path = NOTES[user_text]
        await update.message.reply_document(document=open(file_path, "rb"), caption=f"Here is your note on {user_text} 📚")
    else:
        await update.message.reply_text("Sorry, I don't have notes for that. Try asking something else!")

# Main function to run the bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

    # Start bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

