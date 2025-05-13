# Kiel Telegram Bot - Gaya Chat Non-Baku
import os
import openai
import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# Mengambil API key dari environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Konfigurasi OpenAI
openai.api_key = OPENAI_API_KEY

# Fungsi untuk membalas pesan dengan gaya santai
def generate_response(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=100,
        temperature=0.7
    )
    text = response["choices"][0]["text"].strip()
    # Menyesuaikan gaya bahasa Kiel
    text = text.replace("ya", "iyaw sayang").replace("iya", "oteyy sayang").replace("haha", "xixixixi")
    return text

# Fungsi untuk menangani pesan
def handle_message(update, context):
    user_message = update.message.text
    reply = generate_response(user_message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

# Fungsi untuk memulai bot
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hai bububb, Kiel di sini! Apa kabar sayangg?")

# Mengatur bot Telegram
updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Menjalankan bot
updater.start_polling()
updater.idle()
