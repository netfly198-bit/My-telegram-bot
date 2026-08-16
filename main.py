import telebot
from telebot import types
import json
import os

API_TOKEN = '8988674887:AAEv3JCa9TyvtdBkedSnOjddJoXCLD3gAeM'
bot = telebot.TeleBot(API_TOKEN)

# ملف لحفظ الدعوات ورابط الإحالة
DATA_FILE = "users_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f: return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f: json.dump(data, f)

# قائمة الفيديوهات والحزم
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

# رسالة ترحيب فخمة
WELCOME_MSG = """
✨ **مرحباً بك في متجرنا الرقمي المميز!** ✨

هنا يمكنك الحصول على أجود الفيديوهات الحصرية بأسعار تنافسية.
استخدم النجوم ⭐ للوصول إلى محتواك المفضل فوراً.

💎 **كيفية الاستخدام:**
1. تصفح القائمة بالأسفل.
2. اضغط على الفيديو الذي ترغب في اقتنائه.
3. تابع عملية الدفع بالنجوم واستمتع بالمشاهدة!

🔥 _جودة عالية، سرعة فائقة، تجربة لا مثيل لها._
"""

# 1. أداة استخراج الـ file_id عند إرسال أي فيديو للمطور
@bot.message_handler(content_types=['video'])
def get_file_id(message):
    bot.reply_to(message, f"⚙️ **Developer Tools**\n\nFile ID:\n`{message.video.file_id}`", parse_mode="Markdown")

# 2. القائمة الرئيسية مع نظام الدعوات والترحيب
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = str(message.chat.id)
    data = load_data()
    
    # معالجة نظام الدعوات عبر رابط الإحالة
    args = message.text.split()
    if len(args) > 1:
        referrer_id = args[1]
        if referrer_id != user_id:
            if referrer_id not in data: 
                data[referrer_id] = {"invites": 0, "referred_by": []}
            
            # التأكد من عدم احتساب نفس الشخص مرتين
            if user_id not in data.get(referrer_id, {}).get("referred_by", []):
                if "referred_by" not in data[referrer_id]:
                    data[referrer_id]["referred_by"] = []
                
                data[referrer_id]["invites"] += 1
                data[referrer_id]["referred_by"].append(user_id)
                save_data(data)
                
                try:
                    bot.send_message(referrer_id, "🎉 انضم شخص جديد عبر رابطك! اقتربت من الحصول على خصم 50%.")
                except:
                    pass

    # جلب عدد الدعوات الحالية للمستخدم
    invites = data.get(user_id, {}).get("invites", 0)
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # زر توضيحي لحالة الخصم وعدد الدعوات
    discount_status = f"🎁 رصيدك: {invites}/20 دعوة للحصول على تخفيض 50%!"
    markup.add(types.InlineKeyboardButton(discount_status, callback_data="info_discount"))
    
    # إضافة الفيديوهات مع تطبيق الخصم إذا وصل لـ 20 دعوة
    for i, item in enumerate(VIDEOS):
        current_price = item['price'] // 2 if invites >= 20 else item['price']
        markup.add(types.InlineKeyboardButton(f"{item['title']} | ⭐ {current_price}", callback_data=f"buy_{i}"))
    
    # بناء رسالة الترحيب مع رابط الدعوة الخاص بالمستخدم
    bot_username = bot.get_me().username
    invite_link = f"https://t.me/{bot_username}?start={user_id}"
    
    full_msg = f"{WELCOME_MSG}\n📌 **طريقة للحصول على تخفيض 50%:**\nادعُ 20 شخصاً عبر رابطك الشخصي أدناه:\n`{invite_link}`"
    
    bot.send_message(message.chat.id, full_msg, reply_markup=markup, parse_mode="Markdown")

# تنبيه تفاعلي لزر معلومات الخصم
@bot.callback_query_handler(func=lambda call: call.data == "info_discount")
def info_discount_callback(call):
    user_id = str(call.message.chat.id)
    data = load_data()
    invites = data.get(user_id, {}).get("invites", 0)
    bot.answer_callback_query(call.id, f"لديك حالياً {invites} دعوة من أصل 20 مطلوبة لخصم 50%!", show_alert=True)

# 3. نظام الدفع بالنجوم (فردي أو مجموعة فيديوهات مقفلة مع دعم الخصم)
@bot.callback_query_handler(func=lambda call: call.data.startswith("buy_"))
def handle_payment(call):
    index = int(call.data.split("_")[1])
    item = VIDEOS[index]
    user_id = str(call.message.chat.id)
    
    data = load_data()
    invites = data.get(user_id, {}).get("invites", 0)
    current_price = item['price'] // 2 if invites >= 20 else item['price']
    
    bot.answer_callback_query(call.id, f"جاري تحضير {item['title']}...")
    
    # تجهيز قائمة الفيديوهات
    media_list = [types.InputMediaVideo(media=fid) for fid in item['files']]
    
    bot.send_paid_media(
        chat_id=call.message.chat.id,
        star_count=current_price,
        media=media_list,
        caption=f"✨ شكراً لثقتك!\nاستمتع بمشاهدة: {item['title']}"
    )

if __name__ == "__main__":
    print("🚀 البوت يعمل الآن بكامل طاقته ونظامه المحدث...")
    bot.infinity_polling()
