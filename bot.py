import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Get token from .env

# Initialize bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'hello'])
async def send_welcome(message: types.Message):
    await message.reply("Hello! I'm your bot 🤖")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


