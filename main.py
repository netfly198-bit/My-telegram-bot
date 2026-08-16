from telegram import LabeledPrice, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    PreCheckoutQueryHandler,
    filters,
)

# 1. ضع الـ Token الذي أخذته من BotFather هنا
BOT_TOKEN = "8988674887:AAEv3JCa9TyvtdBkedSnOjddJoXCLD3gAeM"

# أمر /start للترحيب بالمستخدم
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك! لشراء الفيديو الحصري، أرسل الأمر: /buy"
    )

# 2. أمر إرسال فاتورة الدفع بالنجوم
async def buy_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    title = "فيديو حصري"
    description = "شراء فيديو تعليمي حصري"
    payload = "video-payload-123"
    currency = "XTR"  # XTR هو رمز نجوم تلجرام

    # السعر بالنجوم (مثلاً: 50 نجمة)
    prices = [LabeledPrice("فيديو حصري", 50)]

    await context.bot.send_invoice(
        chat_id=chat_id,
        title=title,
        description=description,
        payload=payload,
        provider_token="",  # اتركها فارغة عند استخدام النجوم
        currency=currency,
        prices=prices,
    )

# 3. التأكيد والموافقة على عملية الدفع
async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    await query.answer(ok=True)

# 4. إرسال الفيديو بعد نجاح الدفع
async def successful_payment_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    # يمكنك وضع رابط مباشر للفيديو أو استخدام file_id
    video_url = "https://www.w3schools.com/html/mov_bbb.mp4"  # رابط تجريبي

    await update.message.reply_video(
        video=video_url,
        caption="شكراً لشراء الفيديو! نتمنى لك مشاهدة ممتعة.",
        protect_content=True,  # لمنع إعادة التوجيه أو حفظ الفيديو
    )

if __name__ == "__main__":
    # تشغيل البوت
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy_video))
    app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    app.add_handler(
        MessageHandler(
            filters.SUCCESSFUL_PAYMENT, successful_payment_callback
        )
    )

    print("البوت يعمل الآن...")
    app.run_polling()
