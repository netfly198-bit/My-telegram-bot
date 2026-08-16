import telebot
from telebot import types

# توكن البوت
API_TOKEN = '8988674887:AAEv3JCa9TyvtdBkedSnOjddJoXCLD3gAeM'
bot = telebot.TeleBot(API_TOKEN)

# قائمة الفيديوهات (يمكنك تحديثها متى أردت)
VIDEOS = [
    {"title": "فيديو صغار 1", "price": 100, "file_id": "BAACAgQAAxkBAAOTaoF4SmIIw3ue1_JiWTrwjLCKXL8AAnMmAAKDWAlQvtpTmD9RpCo9BA"},
    {"title": "فيديو صغار 2", "price": 50, "file_id": "BAACAgQAAxkBAAOZaoF4yfdx1YSkg7OQgcnOxmXRRWwAAnQmAAKDWAlQ2h1DDfXHybw9BA"},
    {"title": "فيديو صغار 3", "price": 80, "file_id": "BAACAgQAAxkBAAPIaoGAO8dW7pBN2wWZZjaVnTo7hzgAApQmAAKDWAlQ6t38o7hZhD89BA"},
    {"title": "فيديو صغار 4", "price": 30, "file_id": "BAACAgQAAxkBAAPKaoGAmVULFnPyK4KK7iEu-mTMGokAApUmAAKDWAlQYwaLhz0XVPg9BA"},
    {"title": "فيديو صغار 5", "price": 10, "file_id": "BAACAgQAAxkBAAPMaoGA30T8l98AARfuLcX_4aR1poopAAKWJgACg1gJUGxbIgjCo2mHPQQ"},
    {"title": "فيديو صغار 6", "price": 20, "file_id": "BAACAgQAAxkBAAPOaoGBTgONgOPCzUSVSbNmr_9L7fkAApcmAAKDWAlQt2rlRjg2HWw9BA"},
    {"title": "فيديو صغار 7", "price": 5, "file_id": "BAACAgQAAxkBAAPQaoGBpmpS01FKI76SBW8jWszZ0hUAApomAAKDWAlQBsuvYG2_evg9BA"},
    {"title": "فيديو صغار 8", "price": 10, "file_id": "BAACAgQAAxkBAAPSaoGCCHt1RWrujcuACizOoMtE0NwAApsmAAKDWAlQ2qYd_qGtm189BA"},
    {"title": "فيديو صغار 9", "price": 20, "file_id": "BAACAgQAAxkBAAPUaoGCQ4oxJO908uwGpnQC3GDhHbkAAp0mAAKDWAlQnX2lCf-XR_s9BA"},
    {"title": "فيديو صغار 10", "price": 10, "file_id": "BAACAgQAAxkBAAPWaoGCkKlsl7W2_tuRASdANbBJKb8AAp4mAAKDWAlQ00ZyCh2mx_g9BA"},
    {"title": "فيديو صغار 11", "price": 15, "file_id": "BAACAgQAAxkBAAPYaoGD_pFdFbIAAfm0D0SHYjLmU08UAAKhJgACg1gJUOF1tacNyCI9PQQ"},
    {"title": "فيديو صغار 12", "price": 5, "file_id": "BAACAgQAAxkBAAPaaoGEBldmtCGO61G3RvrDdvBxLSYAAqImAAKDWAlQGntSynT_5_s9BA"},
    {"title": "فيديو صغar 13", "price": 20, "file_id": "BAACAgQAAxkBAAPcaoGEDuUocyh0oY8HX7gzuylCQHkAAqMmAAKDWAlQF6a9IWNmnYY9BA"},
    {"title": "فيديو صغار 14", "price": 10, "file_id": "BAACAgQAAxkBAAPeaoGEFh__YOZMpyQR0zeW9A2CTy0AAqQmAAKDWAlQznUfrhZe6Jk9BA"},
    {"title": "فيديو صغار 15", "price": 10, "file_id": "BAACAgQAAxkBAAPmojiEHnGVlF6BicCOMS5GqgukazIAAqYmAAKDWAlQ0V8G4lEDz2o9BA"},
    {"title": "فيديو صغار 16", "price": 15, "file_id": "BAACAgQAAxkBAAPkaoGEJodz2PK7F45B7O73km3tm1sAAqcmAAKDWAlQ1A41dgTSaic9BA"}
]

# 1. خاصية استخراج الـ file_id عند إرسال أي فيديو للبوت
@bot.message_handler(content_types=['video'])
def handle_docs_video(message):
    bot.reply_to(message, f"✅ الـ file_id هو:\n`{message.video.file_id}`", parse_mode="Markdown")

# 2. القائمة الرئيسية (للمستخدمين)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for i, video in enumerate(VIDEOS):
        markup.add(types.InlineKeyboardButton(f"{video['title']} | ⭐ {video['price']}", callback_data=f"buy_{i}"))
    bot.send_message(message.chat.id, "مرحباً! اختر الفيديو الذي تريد شراءه:", reply_markup=markup)

# 3. إرسال الفيديو كـ Paid Media (للبيع)
@bot.callback_query_handler(func=lambda call: call.data.startswith("buy_"))
def buy(call):
    index = int(call.data.split("_")[1])
    video = VIDEOS[index]
    bot.send_paid_media(
        chat_id=call.message.chat.id,
        star_count=video['price'],
        media=[types.InputMediaVideo(media=video['file_id'], caption=video['title'])]
    )

if __name__ == "__main__":
    bot.infinity_polling()
