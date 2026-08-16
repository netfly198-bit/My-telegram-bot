import telebot
from telebot import types

# توكن البوت
API_TOKEN = '8988674887:AAEv3JCa9TyvtdBkedSnOjddJoXCLD3gAeM'
bot = telebot.TeleBot(API_TOKEN)

# قائمة الفيديوهات الجاهزة
VIDEOS = [
    {"title": "🎬 فيديو صغار 1", "price": 100, "files": ["BAACAgQAAxkBAAOTaoF4SmIIw3ue1_JiWTrwjLCKXL8AAnMmAAKDWAlQvtpTmD9RpCo9BA"]},
    {"title": "🎬 فيديو صغار 2", "price": 50, "files": ["BAACAgQAAxkBAAOZaoF4yfdx1YSkg7OQgcnOxmXRRWwAAnQmAAKDWAlQ2h1DDfXHybw9BA"]},
    {"title": "🎬 فيديو صغار 3", "price": 80, "files": ["BAACAgQAAxkBAAPIaoGAO8dW7pBN2wWZZjaVnTo7hzgAApQmAAKDWAlQ6t38o7hZhD89BA"]},
    {"title": "🎬 فيديو صغار 4", "price": 30, "files": ["BAACAgQAAxkBAAPKaoGAmVULFnPyK4KK7iEu-mTMGokAApUmAAKDWAlQYwaLhz0XVPg9BA"]},
    {"title": "🎬 فيديو صغار 5", "price": 10, "files": ["BAACAgQAAxkBAAPMaoGA30T8l98AARfuLcX_4aR1poopAAKWJgACg1gJUGxbIgjCo2mHPQQ"]},
    {"title": "🎬 فيديو صغار 6", "price": 20, "files": ["BAACAgQAAxkBAAPOaoGBTgONgOPCzUSVSbNmr_9L7fkAApcmAAKDWAlQt2rlRjg2HWw9BA"]},
    {"title": "🎬 فيديو صغار 7", "price": 5, "files": ["BAACAgQAAxkBAAPQaoGBpmpS01FKI76SBW8jWszZ0hUAApomAAKDWAlQBsuvYG2_evg9BA"]},
    {"title": "🎬 فيديو صغار 8", "price": 10, "files": ["BAACAgQAAxkBAAPSaoGCCHt1RWrujcuACizOoMtE0NwAApsmAAKDWAlQ2qYd_qGtm189BA"]},
    {"title": "🎬 فيديو صغار 9", "price": 20, "files": ["BAACAgQAAxkBAAPUaoGCQ4oxJO908uwGpnQC3GDhHbkAAp0mAAKDWAlQnX2lCf-XR_s9BA"]},
    {"title": "🎬 فيديو صغار 10", "price": 10, "files": ["BAACAgQAAxkBAAPWaoGCkKlsl7W2_tuRASdANbBJKb8AAp4mAAKDWAlQ00ZyCh2mx_g9BA"]},
    {"title": "🎬 فيديو صغار 11", "price": 15, "files": ["BAACAgQAAxkBAAPYaoGD_pFdFbIAAfm0D0SHYjLmU08UAAKhJgACg1gJUOF1tacNyCI9PQQ"]},
    {"title": "🎬 فيديو صغار 12", "price": 5, "files": ["BAACAgQAAxkBAAPaaoGEBldmtCGO61G3RvrDdvBxLSYAAqImAAKDWAlQGntSynT_5_s9BA"]},
    {"title": "🎬 فيديو صغار 13", "price": 20, "files": ["BAACAgQAAxkBAAPcaoGEDuUocyh0oY8HX7gzuylCQHkAAqMmAAKDWAlQF6a9IWNmnYY9BA"]},
    {"title": "🎬 فيديو صغار 14", "price": 10, "files": ["BAACAgQAAxkBAAPeaoGEFh__YOZMpyQR0zeW9A2CTy0AAqQmAAKDWAlQznUfrhZe6Jk9BA"]},
    {"title": "🎬 فيديو صغار 15", "price": 10, "files": ["BAACAgQAAxkBAAPmojiEHnGVlF6BicCOMS5GqgukazIAAqYmAAKDWAlQ0V8G4lEDz2o9BA"]},
    {"title": "🎬 فيديو صغار 16", "price": 15, "files": ["BAACAgQAAxkBAAPkaoGEJodz2PK7F45B7O73km3tm1sAAqcmAAKDWAlQ1A41dgTSaic9BA"]}
]

# رسالة الترحيب
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

# استخراج الـ file_id
@bot.message_handler(content_types=['video'])
def get_file_id(message):
    bot.reply_to(message, f"⚙️ **Developer Tools**\n\nFile ID:\n`{message.video.file_id}`", parse_mode="Markdown")

# القائمة الرئيسية
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for i, item in enumerate(VIDEOS):
        markup.add(types.InlineKeyboardButton(f"{item['title']} | ⭐ {item['price']}", callback_data=f"buy_{i}"))
    bot.send_message(message.chat.id, WELCOME_MSG, reply_markup=markup, parse_mode="Markdown")

# نظام الدفع
@bot.callback_query_handler(func=lambda call: call.data.startswith("buy_"))
def handle_payment(call):
    index = int(call.data.split("_")[1])
    item = VIDEOS[index]
    bot.answer_callback_query(call.id, f"جاري تحضير {item['title']}...")
    media_list = [types.InputMediaVideo(media=fid) for fid in item['files']]
    bot.send_paid_media(
        chat_id=call.message.chat.id,
        star_count=item['price'],
        media=media_list,
        caption=f"✨ شكراً لثقتك!\nاستمتع بمشاهدة: {item['title']}"
    )

if __name__ == "__main__":
    bot.infinity_polling()
