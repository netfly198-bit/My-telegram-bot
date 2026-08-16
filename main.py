import telebot
from telebot import types
import json
import os

API_TOKEN = '8988674887:AAEv3JCa9TyvtdBkedSnOjddJoXCLD3gAeM'
bot = telebot.TeleBot(API_TOKEN)

DATA_FILE = "users_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f: 
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f: 
        json.dump(data, f)

# قائمة الفيديوهات
VIDEOS = [
    {"title": {"ar": "🎬 فيديو حماسي 1", "en": "🎬 Action Video 1"}, "price": 100, "files": ["BAACAgQAAxkBAAOTaoF4SmIIw3ue1_JiWTrwjLCKXL8AAnMmAAKDWAlQvtpTmD9RpCo9BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 2", "en": "🎬 Action Video 2"}, "price": 50, "files": ["BAACAgQAAxkBAAOZaoF4yfdx1YSkg7OQgcnOxmXRRWwAAnQmAAKDWAlQ2h1DDfXHybw9BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 3", "en": "🎬 Action Video 3"}, "price": 80, "files": ["BAACAgQAAxkBAAPIaoGAO8dW7pBN2wWZZjaVnTo7hzgAApQmAAKDWAlQ6t38o7hZhD89BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 4", "en": "🎬 Action Video 4"}, "price": 30, "files": ["BAACAgQAAxkBAAPKaoGAmVULFnPyK4KK7iEu-mTMGokAApUmAAKDWAlQYwaLhz0XVPg9BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 5", "en": "🎬 Action Video 5"}, "price": 10, "files": ["BAACAgQAAxkBAAPMaoGA30T8l98AARfuLcX_4aR1poopAAKWJgACg1gJUGxbIgjCo2mHPQQ"]},
    {"title": {"ar": "🎬 فيديو حماسي 6", "en": "🎬 Action Video 6"}, "price": 20, "files": ["BAACAgQAAxkBAAPOaoGBTgONgOPCzUSVSbNmr_9L7fkAApcmAAKDWAlQt2rlRjg2HWw9BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 7", "en": "🎬 Action Video 7"}, "price": 5, "files": ["BAACAgQAAxkBAAPQaoGBpmpS01FKI76SBW8jWszZ0hUAApomAAKDWAlQBsuvYG2_evg9BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 8", "en": "🎬 Action Video 8"}, "price": 10, "files": ["BAACAgQAAxkBAAPSaoGCCHt1RWrujcuACizOoMtE0NwAApsmAAKDWAlQ2qYd_qGtm189BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 9", "en": "🎬 Action Video 9"}, "price": 20, "files": ["BAACAgQAAxkBAAPUaoGCQ4oxJO908uwGpnQC3GDhHbkAAp0mAAKDWAlQnX2lCf-XR_s9BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 10", "en": "🎬 Action Video 10"}, "price": 10, "files": ["BAACAgQAAxkBAAPWaoGCkKlsl7W2_tuRASdANbBJKb8AAp4mAAKDWAlQ00ZyCh2mx_g9BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 11", "en": "🎬 Action Video 11"}, "price": 15, "files": ["BAACAgQAAxkBAAPYaoGD_pFdFbIAAfm0D0SHYjLmU08UAAKhJgACg1gJUOF1tacNyCI9PQQ"]},
    {"title": {"ar": "🎬 فيديو حماسي 12", "en": "🎬 Action Video 12"}, "price": 5, "files": ["BAACAgQAAxkBAAPaaoGEBldmtCGO61G3RvrDdvBxLSYAAqImAAKDWAlQGntSynT_5_s9BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 13", "en": "🎬 Action Video 13"}, "price": 20, "files": ["BAACAgQAAxkBAAPcaoGEDuUocyh0oY8HX7gzuylCQHkAAqMmAAKDWAlQF6a9IWNmnYY9BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 14", "en": "🎬 Action Video 14"}, "price": 10, "files": ["BAACAgQAAxkBAAPeaoGEFh__YOZMpyQR0zeW9A2CTy0AAqQmAAKDWAlQznUfrhZe6Jk9BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 15", "en": "🎬 Action Video 15"}, "price": 10, "files": ["BAACAgQAAxkBAAPmojiEHnGVlF6BicCOMS5GqgukazIAAqYmAAKDWAlQ0V8G4lEDz2o9BA"]},
    {"title": {"ar": "🎬 فيديو حماسي 16", "en": "🎬 Action Video 16"}, "price": 15, "files": ["BAACAgQAAxkBAAPkaoGEJodz2PK7F45B7O73km3tm1sAAqcmAAKDWAlQ1A41dgTSaic9BA"]}
]

TEXTS = {
    "ar": {
        "welcome": "✨ **أهلاً بك في بوت الفيديوهات الساخنة 💋 !** ✨\n\nاختر من القائمة أدناه ما يناسبك:",
        "btn_videos": "🎬 الفيديوهات الحماسية الحصرية",
        "btn_discount": "🎁 عرض خاص 50%",
        "btn_lang": "🌐 تغيير اللغة / Change Language",
        "videos_header": "🎬 **قائمة الفيديوهات الحماسية المتاحة:**",
        "discount_info": "🎁 **عرض خاص 50%**\n\nاحصل على تخفيض **50%** على جميع الفيديوهات الحماسية!\nكل ما عليك هو دعوة **20 شخصاً** عبر رابطك الخاص لتفعيل العرض تلقائياً.\n\n📊 **رصيدك الحالي:** {invites} / 20 دعوة.\n📌 **حالة العرض:** {status}\n\n🔗 **رابط الدعوة الخاص بك:**\n`{link}`",
        "status_active": "✅ تم تفعيل الخصم 50% بنجاح!",
        "status_pending": "⏳ متبقي لديك: {rem} دعوة لتفعيل الخصم.",
        "btn_back": "🔙 العودة للقائمة الرئيسية",
        "new_invite": "🎉 انضم شخص جديد عبر رابطك!"
    },
    "en": {
        "welcome": "✨ **Welcome to Exclusive Hot Videos Bot!** ✨\n\nPlease choose an option from below:",
        "btn_videos": "🎬 Exclusive Action Videos",
        "btn_discount": "🎁 Special Offer 50%",
        "btn_lang": "🌐 Change Language / تغيير اللغة",
        "videos_header": "🎬 **Available Action Videos:**",
        "discount_info": "🎁 **Special Offer 50%**\n\nGet a **50% discount** on all action videos!\nInvite **20 people** using your link to unlock the offer automatically.\n\n📊 **Current balance:** {invites} / 20 invites.\n📌 **Status:** {status}\n\n🔗 **Your referral link:**\n`{link}`",
        "status_active": "✅ 50% discount activated successfully!",
        "status_pending": "⏳ Remaining: {rem} invites to activate discount.",
        "btn_back": "🔙 Back to Main Menu",
        "new_invite": "🎉 A new user joined using your link!"
    }
}

# أداة المطور لاستخراج file_id
@bot.message_handler(content_types=['video'])
def get_file_id(message):
    bot.reply_to(message, f"⚙️ **Developer Tools**\n\nFile ID:\n`{message.video.file_id}`", parse_mode="Markdown")

# أمر start لتحديد اللغة أو فتح القائمة
@bot.message_handler(commands=['start'])
def start_cmd(message):
    user_id = str(message.chat.id)
    data = load_data()
    
    if user_id not in data:
        data[user_id] = {"invites": 0, "referred_by": [], "lang": None}
    
    # معالجة رابط الدعوة
    args = message.text.split()
    if len(args) > 1:
        referrer_id = args[1]
        if referrer_id != user_id:
            if referrer_id not in data:
                data[referrer_id] = {"invites": 0, "referred_by": [], "lang": "ar"}
            if user_id not in data[referrer_id].get("referred_by", []):
                data[referrer_id]["invites"] += 1
                data[referrer_id]["referred_by"].append(user_id)
                ref_lang = data[referrer_id].get("lang", "ar") or "ar"
                try:
                    bot.send_message(referrer_id, TEXTS[ref_lang]["new_invite"])
                except:
                    pass
    
    save_data(data)
    
    # إذا لم يختر اللغة بعد، تظهر واجهة اختيار اللغة
    if not data[user_id].get("lang"):
        show_language_selection(message.chat.id)
    else:
        show_main_menu(message.chat.id, data[user_id]["lang"])

def show_language_selection(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_ar = types.InlineKeyboardButton("العربية 🇸🇦", callback_data="set_lang_ar")
    btn_en = types.InlineKeyboardButton("English 🇬🇧", callback_data="set_lang_en")
    markup.add(btn_ar, btn_en)
    
    msg = "مرحباً بك! يرجى اختيار لغتك المفضلة.\nWelcome! Please select your preferred language."
    bot.send_message(chat_id, msg, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("set_lang_"))
def set_language(call):
    lang = call.data.split("_")[2]
    user_id = str(call.message.chat.id)
    data = load_data()
    
    if user_id not in data:
        data[user_id] = {"invites": 0, "referred_by": []}
        
    data[user_id]["lang"] = lang
    save_data(data)
    
    bot.delete_message(call.message.chat.id, call.message.message_id)
    show_main_menu(call.message.chat.id, lang)

def show_main_menu(chat_id, lang):
    t = TEXTS[lang]
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    btn_videos = types.InlineKeyboardButton(t["btn_videos"], callback_data="show_videos")
    btn_discount = types.InlineKeyboardButton(t["btn_discount"], callback_data="show_discount")
    btn_lang = types.InlineKeyboardButton(t["btn_lang"], callback_data="change_lang")
    
    markup.add(btn_videos, btn_discount, btn_lang)
    bot.send_message(chat_id, t["welcome"], reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "change_lang")
def change_lang_callback(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    show_language_selection(call.message.chat.id)

@bot.callback_query_handler(func=lambda call: call.data == "show_videos")
def show_videos_callback(call):
    user_id = str(call.message.chat.id)
    data = load_data()
    lang = data.get(user_id, {}).get("lang", "ar")
    invites = data.get(user_id, {}).get("invites", 0)
    t = TEXTS[lang]
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    for i, item in enumerate(VIDEOS):
        price = item['price'] // 2 if invites >= 20 else item['price']
        title = item['title'][lang]
        markup.add(types.InlineKeyboardButton(f"{title} | ⭐ {price}", callback_data=f"buy_{i}"))
        
    markup.add(types.InlineKeyboardButton(t["btn_back"], callback_data="back_main"))
    
    bot.edit_message_text(t["videos_header"], call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "show_discount")
def show_discount_callback(call):
    user_id = str(call.message.chat.id)
    data = load_data()
    lang = data.get(user_id, {}).get("lang", "ar")
    invites = data.get(user_id, {}).get("invites", 0)
    t = TEXTS[lang]
    
    bot_username = bot.get_me().username
    link = f"https://t.me/{bot_username}?start={user_id}"
    
    if invites >= 20:
        status = t["status_active"]
    else:
        status = t["status_pending"].format(rem=20 - invites)
        
    info_text = t["discount_info"].format(invites=invites, status=status, link=link)
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(t["btn_back"], callback_data="back_main"))
    
    bot.edit_message_text(info_text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "back_main")
def back_main_callback(call):
    user_id = str(call.message.chat.id)
    data = load_data()
    lang = data.get(user_id, {}).get("lang", "ar")
    t = TEXTS[lang]
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_videos = types.InlineKeyboardButton(t["btn_videos"], callback_data="show_videos")
    btn_discount = types.InlineKeyboardButton(t["btn_discount"], callback_data="show_discount")
    btn_lang = types.InlineKeyboardButton(t["btn_lang"], callback_data="change_lang")
    markup.add(btn_videos, btn_discount, btn_lang)
    
    bot.edit_message_text(t["welcome"], call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith("buy_"))
def handle_payment(call):
    index = int(call.data.split("_")[1])
    item = VIDEOS[index]
    user_id = str(call.message.chat.id)
    
    data = load_data()
    lang = data.get(user_id, {}).get("lang", "ar")
    invites = data.get(user_id, {}).get("invites", 0)
    
    price = item['price'] // 2 if invites >= 20 else item['price']
    title = item['title'][lang]
    
    bot.answer_callback_query(call.id, "جاري تحضير الطلب...")
    
    media_list = [types.InputMediaVideo(media=fid) for fid in item['files']]
    
    caption = f"✨ شكراً لثقتك!\nاستمتع بمشاهدة: {title}" if lang == "ar" else f"✨ Thank you!\nEnjoy watching: {title}"
    
    bot.send_paid_media(
        chat_id=call.message.chat.id,
        star_count=price,
        media=media_list,
        caption=caption
    )

if __name__ == "__main__":
    print("🚀 البوت يعمل الآن بالنظام المزدوج واللغات...")
    bot.infinity_polling()
