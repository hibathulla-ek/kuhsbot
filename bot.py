import logging
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

# ── Add your file_ids here after uploading PDFs ──────────────
# Format: "keyword": ("file_id", "Display Name")
NOTES = {
    "biochemistry":    ("", "Biochemistry Notes - Paper XIII"),
    "microbiology":    ("", "Microbiology Notes - Paper XIV"),
    "pathology":       ("", "Pathology Notes - Paper XV"),
    "histotechnology": ("", "Histotechnology Notes"),
    "cytogenetics":    ("", "Cytogenetics Notes"),
    "mycology":        ("", "Mycology Notes"),
    "virology":        ("", "Virology Notes"),
    "haematology":     ("", "Haematology Notes"),
    "qc":              ("", "Quality Control Notes"),
    "liver":           ("", "Liver Function Tests"),
    "renal":           ("", "Renal Function Tests"),
    "minerals":        ("", "Mineral Metabolism Notes"),
}

# ── /start ────────────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 *KUHS MLT Notes Bot*\n\n"
        "Commands:\n"
        "• /notes — see all available topics\n"
        "• /get biochemistry — get notes by topic\n"
        "• /get mycology — get mycology notes\n\n"
        "Or just type the topic name directly!",
        parse_mode="Markdown"
    )

# ── /notes ────────────────────────────────────────────────────
async def list_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "📚 *Available KUHS MLT Notes*\n\n"
    for keyword, (file_id, name) in NOTES.items():
        icon = "✅" if file_id else "⏳"
        msg += f"{icon} `/get {keyword}` — {name}\n"
    msg += "\n_⏳ = coming soon  ✅ = ready to download_"
    await update.message.reply_text(msg, parse_mode="Markdown")

# ── /get <keyword> ────────────────────────────────────────────
async def get_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Usage: `/get biochemistry`\n\nSend /notes to see all topics.",
            parse_mode="Markdown"
        )
        return
    keyword = " ".join(context.args).lower().strip()
    await send_note(update, keyword)

# ── Core: send note by keyword ────────────────────────────────
async def send_note(update: Update, keyword: str):
    if keyword not in NOTES:
        # Try partial match
        matches = [k for k in NOTES if keyword in k]
        if not matches:
            await update.message.reply_text(
                f"❌ No notes found for *{keyword}*\n\nSend /notes to see all available topics.",
                parse_mode="Markdown"
            )
            return
        keyword = matches[0]

    file_id, name = NOTES[keyword]

    if not file_id:
        await update.message.reply_text(
            f"⏳ *{name}* is not uploaded yet.\nCheck back soon!",
            parse_mode="Markdown"
        )
        return

    await update.message.reply_document(
        document=file_id,
        caption=f"📄 *{name}*\n_KUHS MLT Notes_",
        parse_mode="Markdown"
    )

# ── Handle plain text (keyword detection) ────────────────────
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()
    chat_type = update.message.chat.type
    bot_username = context.bot.username.lower()

    # Remove bot mention if present
    clean = text.replace(f"@{bot_username}", "").strip()

    # In groups: only respond if mentioned OR exact keyword match
    if chat_type != "private":
        mentioned = f"@{bot_username}" in text
        if not mentioned:
            if clean in NOTES and len(clean.split()) <= 2:
                await send_note(update, clean)
            return

    await send_note(update, clean)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("notes", list_notes))
    app.add_handler(CommandHandler("get", get_note))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
