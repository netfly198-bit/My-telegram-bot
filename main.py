import os
import logging
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ==========================================
# 1. خادم Flask (إبقاء البوت أونلاين 24/7)
# ==========================================
web_app = Flask('')

@web_app.route('/')
def home():
    return "Bot is Alive!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

# ==========================================
# 2. الإعدادات والتوكن
# ==========================================
TOKEN = os.environ.get("TOKEN", "8988674887:AAEv3JCa9TyvtdBkedSnOjddJoXCLD3gAeM")
logging.basicConfig(level=logging.INFO)

# ==========================================
# 3. وظائف البوت (استخراج الـ file_id)
# ==========================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! أرسل لي أي فيديو وسيصلك الكود الخاص به فوراً 🚀")

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        file_id = update.message.video.file_id
        await update.message.reply_text(f"✅ تم الحصول على الكود:\n\n`{file_id}`", parse_mode='Markdown')

# ==========================================
# 4. تشغيل البوت
# ==========================================
def main():
    keep_alive()
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VIDEO, get_file_id))
    
    print("🚀 البوت يعمل بدون مشاكل!")
    app.run_polling()

if __name__ == "__main__":
    main()
