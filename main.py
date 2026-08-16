import os
import telebot
from telebot import types

# ضع توكن البوت الخاص بك هنا من BotFather
API_TOKEN = os.environ.get('BOT_TOKEN', 'ضع_توكن_البوت_هنا')

bot = telebot.TeleBot(API_TOKEN)

# ==========================================
# 📊 قاعدة بيانات المنتجات (فردية وحزم)
# ==========================================
PRODUCTS = {
    # --------------------------------------
    # 👶 قسم: فيديوهات صغار (فردية)
    # --------------------------------------
    "kids_1": {
        "title": "فيديو صغار 1",
        "price": 100,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAOTaoF4SmIIw3ue1_JiWTrwjLCKXL8AAnMmAAKDWAlQvtpTmD9RpCo9BA"
    },
    "kids_2": {
        "title": "فيديو صغار 2",
        "price": 50,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAOZaoF4yfdx1YSkg7OQgcnOxmXRRWwAAnQmAAKDWAlQ2h1DDfXHybw9BA"
    },
    "kids_3": {
        "title": "فيديو صغار 3",
        "price": 80,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPIaoGAO8dW7pBN2wWZZjaVnTo7hzgAApQmAAKDWAlQ6t38o7hZhD89BA"
    },
    "kids_4": {
        "title": "فيديو صغار 4",
        "price": 30,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPKaoGAmVULFnPyK4KK7iEu-mTMGokAApUmAAKDWAlQYwaLhz0XVPg9BA"
    },
    "kids_5": {
        "title": "فيديو صغار 5",
        "price": 10,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPMaoGA30T8l98AARfuLcX_4aR1poopAAKWJgACg1gJUGxbIgjCo2mHPQQ"
    },
    "kids_6": {
        "title": "فيديو صغار 6",
        "price": 20,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPOaoGBTgONgOPCzUSVSbNmr_9L7fkAApcmAAKDWAlQt2rlRjg2HWw9BA"
    },
    "kids_7": {
        "title": "فيديو صغار 7",
        "price": 5,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPQaoGBpmpS01FKI76SBW8jWszZ0hUAApomAAKDWAlQBsuvYG2_evg9BA"
    },
    "kids_8": {
        "title": "فيديو صغار 8",
        "price": 10,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPSaoGCCHt1RWrujcuACizOoMtE0NwAApsmAAKDWAlQ2qYd_qGtm189BA"
    },
    "kids_9": {
        "title": "فيديو صغار 9",
        "price": 20,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPUaoGCQ4oxJO908uwGpnQC3GDhHbkAAp0mAAKDWAlQnX2lCf-XR_s9BA"
    },
    "kids_10": {
        "title": "فيديو صغار 10",
        "price": 10,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPWaoGCkKlsl7W2_tuRASdANbBJKb8AAp4mAAKDWAlQ00ZyCh2mx_g9BA"
    },
    "kids_11": {
        "title": "فيديو صغار 11",
        "price": 15,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPYaoGD_pFdFbIAAfm0D0SHYjLmU08UAAKhJgACg1gJUOF1tacNyCI9PQQ"
    },
    "kids_12": {
        "title": "فيديو صغار 12",
        "price": 5,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPaaoGEBldmtCGO61G3RvrDdvBxLSYAAqImAAKDWAlQGntSynT_5_s9BA"
    },
    "kids_13": {
        "title": "فيديو صغار 13",
        "price": 20,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPcaoGEDuUocyh0oY8HX7gzuylCQHkAAqMmAAKDWAlQF6a9IWNmnYY9BA"
    },
    "kids_14": {
        "title": "فيديو صغار 14",
        "price": 10,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPeaoGEFh__YOZMpyQR0zeW9A2CTy0AAqQmAAKDWAlQznUfrhZe6Jk9BA"
    },
    "kids_15": {
        "title": "فيديو صغار 15",
        "price": 10,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPiaoGEHnGVlF6BicCOMS5GqgukazIAAqYmAAKDWAlQ0V8G4lEDz2o9BA"
    },
    "kids_16": {
        "title": "فيديو صغار 16",
        "price": 15,
        "type": "single",
        "file_id": "BAACAgQAAxkBAAPkaoGEJodz2PK7F45B7O73km3tm1sAAqcmAAKDWAlQ1A41dgTSaic9BA"
    },

    # --------------------------------------
    # 📦 قسم: حزم ومجموعات الفيديوهات (مثال)
    # --------------------------------------
    "bundle_kids_all": {
        "title": "📦 حزمة فيديوهات صغار (5 فيديوهات)",
        "price": 30,  # سعر الحزمة بالنجوم
        "type": "bundle",
        "file_ids": [
            "BAACAgQAAxkBAAPMaoGA30T8l98AARfuLcX_4aR1poopAAKWJgACg1gJUGxbIgjCo2mHPQQ",
            "BAACAgQAAxkBAAPQaoGBpmpS01FKI76SBW8jWszZ0hUAApomAAKDWAlQBsuvYG2_evg9BA",
            "BAACAgQAAxkBAAPSaoGCCHt1RWrujcuACizOoMtE0NwAApsmAAKDWAlQ2qYd_qGtm189BA",
            "BAACAgQAAxkBAAPWaoGCkKlsl7W2_tuRASdANbBJKb8AAp4mAAKDWAlQ00ZyCh2mx_g9BA",
            "BAACAgQAAxkBAAPeaoGEFh__YOZMpyQR0zeW9A2CTy0AAqQmAAKDWAlQznUfrhZe6Jk9BA"
        ]
    }
}


# ==========================================
# 🏁 الأمر /start والقائمة الرئيسية
# ==========================================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    btn_kids = types.InlineKeyboardButton("🎬 فيديوهات صغار (فردي)", callback_data="cat_kids")
    btn_bundles = types.InlineKeyboardButton("📦 حزم الفيديوهات (مجموعات)", callback_data="cat_bundles")
    btn_arabic = types.InlineKeyboardButton("🎬 فيديوهات عربية", callback_data="cat_arabic")
    btn_foreign = types.InlineKeyboardButton("🎬 فيديوهات أجنبية", callback_data="cat_foreign")
    
    markup.add(btn_kids, btn_bundles, btn_arabic, btn_foreign)
    
    bot.send_message(
        message.chat.id,
        "مرحباً بك في بوت الفيديوهات! 🍿\nاختر القسم الذي تريد تصفحه للشراء بالنجوم (Telegram Stars):",
        reply_markup=markup
    )


# ==========================================
# 🔘 معالجة ضغطات الأزرار (Callback Queries)
# ==========================================
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    chat_id = call.message.chat.id
    
    # 1. عرض قائمة فيديوهات صغار الفردية
    if call.data == "cat_kids":
        markup = types.InlineKeyboardMarkup(row_width=1)
        for prod_id, prod in PRODUCTS.items():
            if prod.get("type") == "single" and prod_id.startswith("kids_"):
                btn_text = f"{prod['title']} - ⭐ {prod['price']} نجمة"
                markup.add(types.InlineKeyboardButton(btn_text, callback_data=f"buy_{prod_id}"))
        
        markup.add(types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu"))
        bot.edit_message_text("🎬 **قسم فيديوهات صغار (فردي):**\nاختر الفيديو للوصول لصفحة الشراء:", chat_id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    # 2. عرض قسم الحزم والمجموعات
    elif call.data == "cat_bundles":
        markup = types.InlineKeyboardMarkup(row_width=1)
        for prod_id, prod in PRODUCTS.items():
            if prod.get("type") == "bundle":
                btn_text = f"{prod['title']} - ⭐ {prod['price']} نجمة"
                markup.add(types.InlineKeyboardButton(btn_text, callback_data=f"buy_{prod_id}"))
        
        markup.add(types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu"))
        bot.edit_message_text("📦 **قسم حزم الفيديوهات:**\nشراء مجموعة فيديوهات دفعة واحدة بسعر مخفض:", chat_id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    # 3. الأقسام المتبقية (عربية وأجنبية)
    elif call.data in ["cat_arabic", "cat_foreign"]:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu"))
        bot.edit_message_text("قريباً! جاري إضافة الفيديوهات لهذا القسم... ⏳", chat_id, call.message.message_id, reply_markup=markup)

    # 4. العودة للقائمة الرئيسية
    elif call.data == "main_menu":
        send_welcome(call.message)

    # 5. إرسال فاتورة الشراء بالنجوم (Invoice)
    elif call.data.startswith("buy_"):
        prod_id = call.data.replace("buy_", "")
        prod = PRODUCTS.get(prod_id)
        
        if prod:
            prices = [types.LabeledPrice(label=prod['title'], amount=prod['price'])] # amount بالنجوم
            
            bot.send_invoice(
                chat_id=chat_id,
                title=prod['title'],
                description=f"شراء المحتوى مقابل {prod['price']} من نجوم تلغرام.",
                invoice_payload=prod_id,
                provider_token="", # يترك فارغاً للعمل بنجوم تلغرام (Telegram Stars)
                currency="XTR",   # كود عملة نجوم تلغرام
                prices=prices,
                start_parameter=f"buy-{prod_id}"
            )


# ==========================================
# 💳 التحقق والإجابة على استعلام الشراء
# ==========================================
@bot.pre_checkout_query_handler(func=lambda query: True)
def process_pre_checkout_query(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


# ==========================================
# 🎉 معالجة الشراء الناجح وإرسال المحتوى
# ==========================================
@bot.message_handler(content_types=['successful_payment'])
def process_successful_payment(message):
    prod_id = message.successful_payment.invoice_payload
    prod = PRODUCTS.get(prod_id)
    chat_id = message.chat.id
    
    if prod:
        bot.send_message(chat_id, f"✅ **تم الشراء بنجاح!**\nشُكراً لك، جاري إرسال محتوى '{prod['title']}'...", parse_mode="Markdown")
        
        # إذا كانت حزمة فيديوهات (أكثر من فيديو)
        if prod.get("type") == "bundle" and "file_ids" in prod:
            for f_id in prod["file_ids"]:
                bot.send_video(chat_id, f_id)
        
        # إذا كان فيديو فردي
        elif prod.get("type") == "single" and "file_id" in prod:
            bot.send_video(chat_id, prod["file_id"])


# ==========================================
# 🚀 تشغيل البوت
# ==========================================
if __name__ == "__main__":
    print("🤖 البوت يعمل الآن بنجاح...")
    bot.infinity_polling()
