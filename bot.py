import logging
import os
from telegram import Update, InputFile
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Bot Token (use environment variable for security)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7833068674:AAG_PR50yIOFF7KtL_W0VJmF4KdRliD-Vr0")

# Predefined text responses
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hey there! 😊",
    "notes": "Here are your notes! Use /sendfile to get a sample PDF.",
    "thank you": "You're welcome!",
}

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! I can:\n"
        "- Chat with you\n"
        "- Send files (/sendfile)\n"
        "- Receive files (just upload one)"
    )

# Command: /sendfile - Send a PDF to user
async def send_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        file_path = "C:\Users\user\Desktop\4th yr\virology"  # Replace with your file path
        await update.message.reply_document(
            document=InputFile(file_path),
            caption="Here's your PDF! 📄"
        )
    except Exception as e:
        await update.message.reply_text("Failed to send file. Error: " + str(e))

# Handle uploaded files
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Create 'downloads' folder if it doesn't exist
        os.makedirs("downloads", exist_ok=True)

        # Download the file
        file = await update.message.document.get_file()
        file_name = update.message.document.file_name
        save_path = f"downloads/{file_name}"
        await file.download_to_drive(save_path)

        await update.message.reply_text(f"✅ File saved as: {file_name}")
    except Exception as e:
        await update.message.reply_text(f"❌ Error saving file: {str(e)}")

# Handle text messages
async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()
    response = responses.get(user_text, "I don't understand. Try /help")
    await update.message.reply_text(response)

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Update {update} caused error: {context.error}")

def main():
    # Create the Application
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sendfile", send_file))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))
    app.add_error_handler(error)

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    # Create necessary folders
    os.makedirs("files", exist_ok=True)
    os.makedirs("downloads", exist_ok=True)
    main()



