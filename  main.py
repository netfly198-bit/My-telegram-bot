import os
import logging
from threading import Thread
from flask import Flask
from telegram import Update, InputMediaVideo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ==========================================
# 1. خادم Flask (إبقاء البوت أونلاين)
# ==========================================
web_app = Flask('')
@web_app.route('/')
def home(): return "Bot is Alive!"
def run_flask():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host='0.0.0.0', port=port)
Thread(target=run_flask).start()

# ==========================================
# 2. الإعدادات
# ==========================================
TOKEN = os.environ.get("TOKEN", "8988674887:AAEv3JCa9TyvtdBkedSnOjddJoXCLD3gAeM")
logging.basicConfig(level=logging.INFO)

# الأزرار (القائمة)
MENU_KEYBOARD = [
    [KeyboardButton("🎬 أفلام صغار")],
    [KeyboardButton("🎬 أفلام عربية"), KeyboardButton("🎬 أفلام أجنبية")]
]
REPLY_MARKUP = ReplyKeyboardMarkup(MENU_KEYBOARD, resize_keyboard=True)

# ==========================================
# 3. الوظائف
# ==========================================

# عند إرسال فيديو، يقوم البوت بإعطائك الـ file_id
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        file_id = update.message.video.file_id
        await update.message.reply_text(f"✅ تم الحصول على الكود:\n`{file_id}`", parse_mode='Markdown')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! البوت في وضع التطوير حالياً.", reply_markup=REPLY_MARKUP)

# ==========================================
# 4. التشغيل
# ==========================================
def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    # هذا السطر يستقبل أي فيديو ترسله ويستخرج الكود منه
    app.add_handler(MessageHandler(filters.VIDEO, get_file_id))
    
    print("🚀 البوت يعمل الآن بدون قيود، أرسل أي فيديو للحصول على الـ ID الخاص به.")
    app.run_polling()

if __name__ == "__main__":
    main()
