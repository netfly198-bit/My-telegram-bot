import os
import logging
from threading import Thread
from flask import Flask
from telegram import Update, InputMediaVideo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

web_app = Flask('')

@web_app.route('/')
def home():
    return "Bot is Alive and Running 24/7!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

TOKEN = os.environ.get("TOKEN", "8988674887:AAEv3JCa9TyvtdBkedSnOjddJoXCLD3gAeM")
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

VIDEOS = {
    "vid_1": {"title": "🎬 الفيديو الأول", "price": 50, "content": "BAACAgQAAxkBAAMqaoFQoX6qZxyt8KgoJ5ivrFRDAdEAAlcmAAKDWAlQ-1-N239Vw3g9BA"},
    "vid_2": {"title": "🎬 الفيديو الثاني", "price": 80, "content": "BAACAgQAAxkBAAMgaoFOjrMqtewSkn71JxvImxsRTNkAAlYmAAKDWAlQDZSOMq5bp-I9BA"}
}

MENU_KEYBOARD = [[KeyboardButton("شاهد الفيديوهات الحصرية 🎥")]]
REPLY_MARKUP = ReplyKeyboardMarkup(MENU_KEYBOARD, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✨ أهلاً بك! اضغط على الزر أدناه للبدء:", reply_markup=REPLY_MARKUP)

async def show_videos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for vid_id, vid_data in VIDEOS.items():
        await context.bot.send_paid_media(
            chat_id=update.effective_chat.id,
            star_count=vid_data["price"],
            media=[InputMediaVideo(media=vid_data["content"], caption=vid_data["title"])]
        )

async def ignore_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⛔ يرجى استخدام الزر الموجود في الأسفل فقط.", reply_markup=REPLY_MARKUP)

def main():
    keep_alive()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Text("شاهد الفيديوهات الحصرية 🎥"), show_videos))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, ignore_input))
    print("🚀 البوت يعمل الآن!")
    app.run_polling()

if __name__ == "__main__":
    main()
