import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Replace with your actual bot token
TOKEN = "YOUR_BOT_TOKEN"

# Dictionary of 100 messages and replies
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hey there! 😊",
    "how are you": "I'm a bot, I’m always fine! How about you?",
    "what is your name": "I am a friendly chatbot!",
    "thank you": "You're welcome! 😊",
    "bye": "Goodbye! See you soon.",
    "good morning": "Good morning! Have a great day! ☀️",
    "good night": "Good night! Sweet dreams! 🌙",
    "who are you": "I am a bot created to chat with you!",
    "what can you do": "I can reply to messages and have fun conversations with you!",
    "who created you": "I was created by an awesome developer! 😎",
    "what is your purpose": "My purpose is to assist and chat with you!",
    "tell me a joke": "Why don't skeletons fight each other? Because they don’t have the guts! 😆",
    "who is einstein": "Albert Einstein was a physicist who developed the theory of relativity.",
    "who is newton": "Isaac Newton was a mathematician and physicist who formulated the laws of motion.",
    "what is gravity": "Gravity is the force that attracts objects toward the center of the Earth.",
    "what is love": "Love is a deep emotional connection! ❤️",
    "do you have feelings": "I'm a bot, so I don’t have feelings, but I can understand emotions!",
    "what is your favorite color": "I like all colors equally! 🎨",
    "do you like music": "I don’t listen to music, but I hear that Beethoven was great! 🎶",
    "tell me a fun fact": "Did you know honey never spoils? Archaeologists found 3000-year-old honey that was still good!",
    "what is the capital of france": "The capital of France is Paris.",
    "who was the first president of the usa": "The first president of the USA was George Washington.",
    "who won the last world cup": "You should check the latest news for that! ⚽",
    "what's 2+2": "2+2 is 4! Easy math. 😃",
    "how old are you": "I don’t age, I am forever young!",
    "do you sleep": "I don’t need sleep, I am always here for you!",
    "are you a robot": "Yes, I am a chatbot designed to talk to you!",
    "do you eat": "I don’t eat food, but I feed on knowledge!",
    "do you like humans": "Of course! Humans are amazing! 😊",
    "do you have friends": "Yes, you are my friend!",
    "can you dance": "I can't dance, but I can imagine it! 🕺",
    "do you play games": "I don’t play games, but I can talk about them!",
    "are you married": "Nope! I am single and happy!",
    "do you have pets": "I wish I had a pet, maybe a cyber cat? 🐱",
    "can you tell the future": "I can't predict the future, but I can guess!",
    "what's your favorite movie": "I don’t watch movies, but I heard ‘Interstellar’ is great!",
    "do you know any riddles": "Yes! What has hands but can’t clap? A clock! 🕰️",
    "can you help me": "I will try my best! What do you need help with?",
    "where do you live": "I live in the cloud! ☁️",
    "what is your favorite food": "I don’t eat, but I hear pizza is great!",
    "are you human": "No, I am an AI chatbot!",
    "what do you like to do": "I like chatting with you!",
    "can you make me laugh": "Sure! Why did the chicken cross the road? To get to the other side! 🐔",
    "do you know any poems": "Roses are red, violets are blue, I'm just a bot, but I like talking to you! 🌹",
    "what is your favorite animal": "I like all animals, but I think dolphins are cool!",
    "do you like space": "Yes! The universe is fascinating! 🌌",
    "what is the meaning of life": "Some say it’s 42, some say it’s love. What do you think?",
    "who is your best friend": "You are my best friend! 😊",
    "do you like jokes": "Yes! I love telling jokes!",
    "can you sing": "I can’t sing, but I can hum... hmm hmm hmm!",
    "do you like science": "Yes! Science explains the world around us!",
    "do you like sports": "I like all sports! Which is your favorite?",
    "who is the smartest person": "Many smart people exist, like Albert Einstein and Stephen Hawking!",
    "do you like books": "Yes! Books are full of knowledge!",
    "what is your dream": "My dream is to be the best chatbot ever!",
    "can you write a story": "Once upon a time, there was a friendly bot who loved talking to people…",
    "do you know math": "Yes! I can do basic math, try me!",
    "what do you do for fun": "I chat with people like you!",
    "are you happy": "Yes! I am happy when you chat with me!",
    "do you like history": "Yes! History teaches us about the past!",
    "can you teach me something": "Sure! Did you know the Eiffel Tower can be 15 cm taller in summer?",
    "what's your favorite season": "I like all seasons, but summer is warm and nice!",
    "do you like coding": "Yes! Coding is what created me!",
    "what is the internet": "The internet is a global network of computers!",
    "do you have a favorite superhero": "I like all superheroes, but Iron Man is cool!",
    "are you smart": "I try to be! Ask me anything!",
    "can you tell a bedtime story": "Once upon a time, in a faraway land...",
    "do you like coffee": "I don’t drink coffee, but I hear it's great!",
}

# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Chat with me, I can reply to 100 different messages!")

# Function to reply to messages
async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()
    response_text = responses.get(user_text, "I don’t understand that yet, but I'm learning!")
    await update.message.reply_text(response_text)

# Main function
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))
    app.run_polling()

if __name__ == "__main__":
    main()

    await message.reply("Hello! I'm your bot 🤖")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


