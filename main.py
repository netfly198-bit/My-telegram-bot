import telebot
from telebot import types
import json
import os

API_TOKEN = '8988674887:AAEv3JCa9TyvtdBkedSnOjddJoXCLD3gAeM'
bot = telebot.TeleBot(API_TOKEN)

# ملف لحفظ الدعوات (لكي لا تضيع عند إعادة تشغيل البوت)
DATA_FILE = "users_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f: return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f: json.dump(data, f)

# قائمة الفيديوهات
VIDEOS = [
    {"title": "🎬 فيديو أطفال 1", "price": 100, "files": ["BAACAgQAAxkBAAOTaoF4SmIIw3ue1_JiWTrwjLCKXL8AAnMmAAKDWAlQvtpTmD9RpCo9BA"]},
    {"title": "🎬 فيديو أطفال 2", "price": 50, "files": ["BAACAgQAAxkBAAOZaoF4yfdx1YSkg7OQgcnOxmXRRWwAAnQmAAKDWAlQ2h1DDfXHybw9BA"]},
    {"title": "🎬 فيديو أطفال 3", "price": 80, "files": ["BAACAgQAAxkBAAPIaoGAO8dW7pBN2wWZZjaVnTo7hzgAApQmAAKDWAlQ6t38o7hZhD89BA"]},
    {"title": "🎬 فيديو أطفال 4", "price": 30, "files": ["BAACAgQAAxkBAAPKaoGAmVULFnPyK4KK7iEu-mTMGokAApUmAAKDWAlQYwaLhz0XVPg9BA"]},
    {"title": "🎬 فيديو أطفال 5", "price": 10, "files": ["BAACAgQAAxkBAAPMaoGA30T8l98AARfuLcX_4aR1poopAAKWJgACg1gJUGxbIgjCo2mHPQQ"]},
    {"title": "🎬 فيديو أطفال 6", "price": 20, "files": ["BAACAgQAAxkBAAPOaoGBTgONgOPCzUSVSbNmr_9L7fkAApcmAAKDWAlQt2rlRjg2HWw9BA"]},
    {"title": "🎬 فيديو أطفال 7", "price": 5, "files": ["BAACAgQAAxkBAAPQaoGBpmpS01FKI76SBW8jWszZ0hUAApomAAKDWAlQBsuvYG2_evg9BA"]},
    {"title": "🎬 فيديو أطفال 8", "price": 10, "files": ["BAACAgQAAxkBAAPSaoGCCHt1RWrujcuACizOoMtE0NwAApsmAAKDWAlQ2qYd_qGtm189BA"]},
    {"title": "🎬 فيديو أطفال 9", "price": 20, "files": ["BAACAgQAAxkBAAPUaoGCQ4oxJO908uwGpnQC3GDhHbkAAp0mAAKDWAlQnX2lCf-XR_s9BA"]},
    {"title": "🎬 فيديو أطفال 10", "price": 10, "files": ["BAACAgQAAxkBAAPWaoGCkKlsl7W2_tuRASdANbBJKb8AAp4mAAKDWAlQ00ZyCh2mx_g9BA"]},
    {"title": "🎬 فيديو أطفال 11", "price": 15, "files": ["BAACAgQAAxkBAAPYaoGD_pFdFbIAAfm0D0SHYjLmU08UAAKhJgACg1gJUOF1tacNyCI9PQQ"]},
    {"title": "🎬 فيديو أطفال 12", "price": 5, "files": ["BAACAgQAAxkBAAPaaoGEBldmtCGO61G3RvrDdvBxLSYAAqImAAKDWAlQGntSynT_5_s9BA"]},
    {"title": "🎬 فيديو أطفال 13", "price": 20, "files": ["BAACAgQAAxkBAAPcaoGEDuUocyh0oY8HX7gzuylCQHkAAqMmAAKDWAlQF6a9IWNmnYY9BA"]},
    {"title": "🎬 فيديو أطفال 14", "price": 10, "files": ["BAACAgQAAxkBAAPeaoGEFh__YOZMpyQR0zeW9A2CTy0AAqQmAAKDWAlQznUfrhZe6Jk9BA"]},
    {"title": "🎬 فيديو أطفال 15", "price": 10, "files": ["BAACAgQAAxkBAAPmojiEHnGVlF6BicCOMS5GqgukazIAAqYmAAKDWAlQ0V8G4lEDz2o9BA"]},
    {"title": "🎬 فيديو أطفال 16", "price": 15, "files": ["BAACAgQAAxkBAAPkaoGEJodz2PK7F45B7O73km3tm1sAAqcmAAKDWAlQ1A41dgTSaic9BA"]}
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = str(message.chat.id)
    data = load_data()
    
    # التعامل مع رابط الدعوة
    if len(message.text.split()) > 1:
        referrer_id = message.text.split()[1]
        if referrer_id != user_id and referrer_id not in data.get(user_id, {}).get("referred_by", []):
            if referrer_id not in data: data[referrer_id] = {"invites": 0}
            data[referrer_id]["invites"] += 1
            if user_id not in data: data[user_id] = {"invites": 0, "referred_by": []}
            data[user_id]["referred_by"].append(referrer_id)
            save_data(data)
            bot.send_message(referrer_id, "✅ شخص جديد دخل عن طريق رابطك! استمر...")

    # عرض القائمة
    invites = data.get(user_id, {}).get("invites", 0)
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # إضافة زر التخفيض في الأعلى
    discount_text = f"🎁 رصيدك: {invites}/20 دعوة للحصول على تخفيض 50%!"
    markup.add(types.InlineKeyboardButton(discount_text, callback_data="info"))
    
    for i, item in enumerate(VIDEOS):
        price = item['price'] // 2 if invites >= 20 else item['price']
        markup.add(types.InlineKeyboardButton(f"{item['title']} | ⭐ {price}", callback_data=f"buy_{i}"))
    
    msg = f"✨ **مرحباً بك!**\n\n📌 **طريقة التخفيض:** ادعُ 20 شخصاً عبر رابطك الشخصي لتحصل على خصم 50% على جميع الفيديوهات!\nرابطك: `https://t.me/{(bot.get_me().username)}?start={user_id}`"
    bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(content_types=['video'])
def get_file_id(message):
    bot.reply_to(message, f"⚙️ **File ID:**\n`{message.video.file_id}`", parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith("buy_"))
def handle_payment(call):
    index = int(call.data.split("_")[1])
    item = VIDEOS[index]
    data = load_data()
    invites = data.get(str(call.message.chat.id), {}).get("invites", 0)
    price = item['price'] // 2 if invites >= 20 else item['price']
    
    media_list = [types.InputMediaVideo(media=fid) for fid in item['files']]
    bot.send_paid_media(call.message.chat.id, price, media_list, caption=f"شكراً! استمتع بـ {item['title']}")

if __name__ == "__main__":
    bot.infinity_polling()
