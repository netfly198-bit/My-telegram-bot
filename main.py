import telebot
from telebot import types

# توكن البوت الخاص بك
API_TOKEN = '8988674887:AAEv3JCa9TyvtdBkedSnOjddJoXCLD3gAeM'
bot = telebot.TeleBot(API_TOKEN)

# قاعدة بيانات الفيديوهات الـ 16 كاملة مع أسعارها الحقيقية
PRODUCTS = {
    "kids_1": {"title": "فيديو صغار 1", "price": 100, "file_id": "BAACAgQAAxkBAAOTaoF4SmIIw3ue1_JiWTrwjLCKXL8AAnMmAAKDWAlQvtpTmD9RpCo9BA"},
    "kids_2": {"title": "فيديو صغار 2", "price": 50, "file_id": "BAACAgQAAxkBAAOZaoF4yfdx1YSkg7OQgcnOxmXRRWwAAnQmAAKDWAlQ2h1DDfXHybw9BA"},
    "kids_3": {"title": "فيديو صغار 3", "price": 80, "file_id": "BAACAgQAAxkBAAPIaoGAO8dW7pBN2wWZZjaVnTo7hzgAApQmAAKDWAlQ6t38o7hZhD89BA"},
    "kids_4": {"title": "فيديو صغار 4", "price": 30, "file_id": "BAACAgQAAxkBAAPKaoGAmVULFnPyK4KK7iEu-mTMGokAApUmAAKDWAlQYwaLhz0XVPg9BA"},
    "kids_5": {"title": "فيديو صغار 5", "price": 10, "file_id": "BAACAgQAAxkBAAPMaoGA30T8l98AARfuLcX_4aR1poopAAKWJgACg1gJUGxbIgjCo2mHPQQ"},
    "kids_6": {"title": "فيديو صغار 6", "price": 20, "file_id": "BAACAgQAAxkBAAPOaoGBTgONgOPCzUSVSbNmr_9L7fkAApcmAAKDWAlQt2rlRjg2HWw9BA"},
    "kids_7": {"title": "فيديو صغار 7", "price": 5, "file_id": "BAACAgQAAxkBAAPQaoGBpmpS01FKI76SBW8jWszZ0hUAApomAAKDWAlQBsuvYG2_evg9BA"},
    "kids_8": {"title": "فيديو صغار 8", "price": 10, "file_id": "BAACAgQAAxkBAAPSaoGCCHt1RWrujcuACizOoMtE0NwAApsmAAKDWAlQ2qYd_qGtm189BA"},
    "kids_9": {"title": "فيديو صغار 9", "price": 20, "file_id": "BAACAgQAAxkBAAPUaoGCQ4oxJO908uwGpnQC3GDhHbkAAp0mAAKDWAlQnX2lCf-XR_s9BA"},
    "kids_10": {"title": "فيديو صغار 10", "price": 10, "file_id": "BAACAgQAAxkBAAPWaoGCkKlsl7W2_tuRASdANbBJKb8AAp4mAAKDWAlQ00ZyCh2mx_g9BA"},
    "kids_11": {"title": "فيديو صغار 11", "price": 15, "file_id": "BAACAgQAAxkBAAPYaoGD_pFdFbIAAfm0D0SHYjLmU08UAAKhJgACg1gJUOF1tacNyCI9PQQ"},
    "kids_12": {"title": "فيديو صغار 12", "price": 5, "file_id": "BAACAgQAAxkBAAPaaoGEBldmtCGO61G3RvrDdvBxLSYAAqImAAKDWAlQGntSynT_5_s9BA"},
    "kids_13": {"title": "فيديو صغار 13", "price": 20, "file_id": "BAACAgQAAxkBAAPcaoGEDuUocyh0oY8HX7gzuylCQHkAAqMmAAKDWAlQF6a9IWNmnYY9BA"},
    "kids_14": {"title": "فيديو صغار 14", "price": 10, "file_id": "BAACAgQAAxkBAAPeaoGEFh__YOZMpyQR0zeW9A2CTy0AAqQmAAKDWAlQznUfrhZe6Jk9BA"},
    "kids_15": {"title": "فيديو صغار 15", "price": 10, "file_id": "BAACAgQAAxkBAAPmojiEHnGVlF6BicCOMS5GqgukazIAAqYmAAKDWAlQ0V8G4lEDz2o9BA"},
    "kids_16": {"title": "فيديو صغار 16", "price": 15, "file_id": "BAACAgQAAxkBAAPkaoGEJodz2PK7F45B7O73km3tm1sAAqcmAAKDWAlQ1A41dgTSaic9BA"}
}

# 🏁 القائمة الرئيسية عند إرسال /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # إضافة زر قسم الفيديوهات تماماً كما يظهر في صورتك
    btn_kids = types.InlineKeyboardButton("🎬 فيديوهات صغار", callback_data="cat_kids")
    markup.add(btn_kids)
    
    bot.send_message(
        message.chat.id,
        "مرحباً بك في متجر الفيديوهات! 🍿\nاختر القسم لعرض الفيديوهات وأسعارها بالنجوم:",
        reply_markup=markup
    )

# 🔘 تصفح الأقسام والفيديوهات
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    chat_id = call.message.chat.id
    
    if call.data == "cat_kids":
        markup = types.InlineKeyboardMarkup(row_width=1)
        for prod_id, prod in PRODUCTS.items():
            if prod_id.startswith("kids_"):
                # شكل الزر: اسم الفيديو بجانبه السعر بالنجوم (مطابق لصورنك)
                btn_text = f"{prod['title']} - ⭐ {prod['price']} نجمة"
                markup.add(types.InlineKeyboardButton(btn_text, callback_data=f"buy_{prod_id}"))
        
        markup.add(types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu"))
        bot.edit_message_text("🎬 **قسم فيديوهات صغار:**\nاختر الفيديو للشراء والشاهدة:", chat_id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    elif call.data == "main_menu":
        send_welcome(call.message)

    elif call.data.startswith("buy_"):
        prod_id = call.data.replace("buy_", "")
        prod = PRODUCTS.get(prod_id)
        
        if prod:
            prices = [types.LabeledPrice(label=prod['title'], amount=prod['price'])]
            
            # إرسال فاتورة الدفع بالنجوم
            bot.send_invoice(
                chat_id=chat_id,
                title=prod['title'],
                description=f"شراء وإرسال {prod['title']} مقابل {prod['price']} نجمة.",
                invoice_payload=prod_id,
                provider_token="",
                currency="XTR",
                prices=prices,
                start_parameter=f"buy-{prod_id}"
            )

# 💳 الموافقة على الدفع
@bot.pre_checkout_query_handler(func=lambda query: True)
def process_pre_checkout_query(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# 🎉 إرسال الفيديو بعد نجاح الدفع تلقائياً
@bot.message_handler(content_types=['successful_payment'])
def process_successful_payment(message):
    prod_id = message.successful_payment.invoice_payload
    prod = PRODUCTS.get(prod_id)
    chat_id = message.chat.id
    
    if prod:
        bot.send_message(chat_id, f"✅ **تم الشراء بنجاح!**\nإليك فيديو '{prod['title']}' الخاص بك:", parse_mode="Markdown")
        bot.send_video(chat_id, prod["file_id"])

if __name__ == "__main__":
    print("🤖 البوت يعمل بكامل الفيديوهات الآن...")
    bot.infinity_polling()
