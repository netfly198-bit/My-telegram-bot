from flask import Flask
import json
import os
from threading import Thread
import telebot
from telebot import types

# --- 1️⃣ إعداد خادم Web بسيط لإبقاء Render مستيقظاً ---
app = Flask(__name__)

@app.route('/')
def home():
  return 'Bot is alive! 🚀', 200

def run_flask():
  port = int(os.environ.get('PORT', 8080))
  app.run(host='0.0.0.0', port=port)

Thread(target=run_flask, daemon=True).start()

# --- 2️⃣ إعداد البوت والبيانات ---
API_TOKEN = '8988674887:AAEv3JCa9TyvtdBkedSnOjddJoXCLD3gAeM'
bot = telebot.TeleBot(API_TOKEN)

DATA_FILE = 'users_data.json'

def load_data():
  if os.path.exists(DATA_FILE):
    try:
      with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)
    except:
      return {}
  return {}

def save_data(data):
  with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# --- 3️⃣ قوائم الفيديوهات ---

FREE_VIDEOS = [
    {
        'title': {'ar': '🎥 فيديو مجاني 1', 'en': '🎥 Free Video 1'},
        'files': [
            'BAACAgEAAxkBAAIDAmqDbsxy1lGu39DuCZJZ6zoYGMpGAALHAwAC8kVgRbeGtCbLRZbsPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 2', 'en': '🎥 Free Video 2'},
        'files': [
            'BAACAgEAAxkBAAIDA2qDbswAAeqMEoVad5sC7V3laQictwACygMAAvJFYEWTk63rrK4V0z0E'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 3', 'en': '🎥 Free Video 3'},
        'files': [
            'BAACAgEAAxkBAAIDBGqDbszoSrGnSypGZKnDwWOft66GAALOAwAC8kVgRZRScyW8cBtRPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 4', 'en': '🎥 Free Video 4'},
        'files': [
            'BAACAgEAAxkBAAIDBWqDbsyDfAd3ts9yZp1hp2_OGkg9AALQAwAC8kVgRTH6xZdsAUfEPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 5', 'en': '🎥 Free Video 5'},
        'files': [
            'BAACAgIAAxkBAAIDC2qDcGvfOWX9O2V5-FZKWGRYQHJIAAJRIAAC5eJZSEXeBDWwTHl8PQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 6', 'en': '🎥 Free Video 6'},
        'files': [
            'BAACAgIAAxkBAAIDCmqDcGvTe12CZyDclsMcPRacZG65AAJJIAAC5eJZSEFx6Kh-yB5xPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 7', 'en': '🎥 Free Video 7'},
        'files': [
            'BAACAgIAAxkBAAIDDGqDcGvBYXJG0r1QHuHjJhncQxo4AAJZIAAC5eJZSPZeGN8p8I8SPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 8', 'en': '🎥 Free Video 8'},
        'files': [
            'BAACAgIAAxkBAAIDFGqDcGt4wqQ6cpLhaEn9lNFE1e0FAAIPgAAC-yx4SnkuqR8cldjJPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 9', 'en': '🎥 Free Video 9'},
        'files': [
            'BAACAgIAAxkBAAIDEmqDcGvgr5ua66X6KmBHsZX13gnPAAKCfQAC-yx4SpBRqAqWiRuXPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 10', 'en': '🎥 Free Video 10'},
        'files': [
            'BAACAgIAAxkBAAIDEWqDcGvEOak0ZykAATg6XhJYL95PnQACgX0AAvsseErRLJUmLioKJz0E'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 11', 'en': '🎥 Free Video 11'},
        'files': [
            'BAACAgEAAxkBAAIDEGqDcGt71bZpo5AryYXfBh_vOk7sAAJPBQAC5OYQRm_fXG5t94QfPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 12', 'en': '🎥 Free Video 12'},
        'files': [
            'BAACAgIAAxkBAAIDD2qDcGtPIwI1HkSN65jyQLn6PJMAA9doAAKjyLBLpyKURcKrWJ09BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 13', 'en': '🎥 Free Video 13'},
        'files': [
            'BAACAgIAAxkBAAIDDmqDcGuKaoydLEmb7qRXII8sV_BgAALWaAACo8iwSwTlzAumf2_cPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 14', 'en': '🎥 Free Video 14'},
        'files': [
            'BAACAgIAAxkBAAIDDWqDcGtBY6uYvZ376H3DG8WQJjiXAALVaAACo8iwS9UOXNAq7hFUPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 15', 'en': '🎥 Free Video 15'},
        'files': [
            'BAACAgIAAxkBAAIDKWqDci8gzQK5muPBbuOs4vTgxoh9AAJ0igACcnSgStJUwf01c0JJPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 16', 'en': '🎥 Free Video 16'},
        'files': [
            'BAACAgIAAxkBAAIDJ2qDci_xX6u5njVTM9JRRksgjJhNAAJtigACcnSgSsnge8DATcOVPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 17', 'en': '🎥 Free Video 17'},
        'files': [
            'BAACAgIAAxkBAAIDKGqDci8Ym31JPpeJ8LD8DY_MO_yMAAJwigACcnSgSr5Q2Qc_my4LPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 18', 'en': '🎥 Free Video 18'},
        'files': [
            'BAACAgIAAxkBAAIDJWqDcfk2yCN-DT00cBgypBzfrkIvAAIeeQAC0HOhSqRMDIwV5-TXPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 19', 'en': '🎥 Free Video 19'},
        'files': [
            'BAACAgIAAxkBAAIDIWqDcecgLis_GkxrORDarLUTS_vmAAIjcwACF9V4SNu2erBtqrmxPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 20', 'en': '🎥 Free Video 20'},
        'files': [
            'BAACAgIAAxkBAAIDIGqDcecPrrGArMGi3A2UzwaeMz1KAALdVQAC372xStAvSrRpIqKwPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 21', 'en': '🎥 Free Video 21'},
        'files': [
            'BAACAgIAAxkBAAIDH2qDcechZ1o3anvkWpipE5ZGchzMAAJEgAACH2KJSpz5-W9GQUEjPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 22', 'en': '🎥 Free Video 22'},
        'files': [
            'BAACAgEAAxkBAAIDMGqDdOgoXW9SHDST5R-8warEZIFIAALUBwACxLWQR2shEo_23qLMPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 23', 'en': '🎥 Free Video 23'},
        'files': [
            'BAACAgQAAxkBAAIDL2qDdOjDyvINkBcOmyYerhGZSbvmAALfHAACOe1JUtyPY5-bHaSsPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 24', 'en': '🎥 Free Video 24'},
        'files': [
            'BAACAgIAAxkBAAIDLWqDdOimfNXglwL91dMQTp3LivJdAAL0hAACe-BZSgHbx6_xZGJiPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو مجاني 25', 'en': '🎥 Free Video 25'},
        'files': [
            'BAACAgUAAxkBAAIDLmqDdOgmQu6ClquOOBfven4n3yuOAAK-LgACDOA5Vm0qMZBy-Ix0PQQ'
        ],
    },
]

KIDS_VIDEOS = [
    {
        'title': {'ar': '🎥 فيديو صغار 1', 'en': '🎥 Kids Video 1'},
        'price': 100,
        'files': [
            'BAACAgQAAxkBAAOTaoF4SmIIw3ue1_JiWTrwjLCKXL8AAnMmAAKDWAlQvtpTmD9RpCo9BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 2', 'en': '🎥 Kids Video 2'},
        'price': 50,
        'files': [
            'BAACAgQAAxkBAAOZaoF4yfdx1YSkg7OQgcnOxmXRRWwAAnQmAAKDWAlQ2h1DDfXHybw9BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 3', 'en': '🎥 Kids Video 3'},
        'price': 80,
        'files': [
            'BAACAgQAAxkBAAPIaoGAO8dW7pBN2wWZZjaVnTo7hzgAApQmAAKDWAlQ6t38o7hZhD89BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 4', 'en': '🎥 Kids Video 4'},
        'price': 30,
        'files': [
            'BAACAgQAAxkBAAPKaoGAmVULFnPyK4KK7iEu-mTMGokAApUmAAKDWAlQYwaLhz0XVPg9BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 5', 'en': '🎥 Kids Video 5'},
        'price': 10,
        'files': [
            'BAACAgQAAxkBAAPMaoGA30T8l98AARfuLcX_4aR1poopAAKWJgACg1gJUGxbIgjCo2mHPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 6', 'en': '🎥 Kids Video 6'},
        'price': 20,
        'files': [
            'BAACAgQAAxkBAAPOaoGBTgONgOPCzUSVSbNmr_9L7fkAApcmAAKDWAlQt2rlRjg2HWw9BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 7', 'en': '🎥 Kids Video 7'},
        'price': 5,
        'files': [
            'BAACAgQAAxkBAAPQaoGBpmpS01FKI76SBW8jWszZ0hUAApomAAKDWAlQBsuvYG2_evg9BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 8', 'en': '🎥 Kids Video 8'},
        'price': 10,
        'files': [
            'BAACAgQAAxkBAAPSaoGCCHt1RWrujcuACizOoMtE0NwAApsmAAKDWAlQ2qYd_qGtm189BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 9', 'en': '🎥 Kids Video 9'},
        'price': 20,
        'files': [
            'BAACAgQAAxkBAAPUaoGCQ4oxJO908uwGpnQC3GDhHbkAAp0mAAKDWAlQnX2lCf-XR_s9BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 10', 'en': '🎥 Kids Video 10'},
        'price': 10,
        'files': [
            'BAACAgQAAxkBAAPWaoGCkKlsl7W2_tuRASdANbBJKb8AAp4mAAKDWAlQ00ZyCh2mx_g9BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 11', 'en': '🎥 Kids Video 11'},
        'price': 15,
        'files': [
            'BAACAgQAAxkBAAPYaoGD_pFdFbIAAfm0D0SHYjLmU08UAAKhJgACg1gJUOF1tacNyCI9PQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 12', 'en': '🎥 Kids Video 12'},
        'price': 5,
        'files': [
            'BAACAgQAAxkBAAPaaoGEBldmtCGO61G3RvrDdvBxLSYAAqImAAKDWAlQGntSynT_5_s9BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 13', 'en': '🎥 Kids Video 13'},
        'price': 20,
        'files': [
            'BAACAgQAAxkBAAPcaoGEDuUocyh0oY8HX7gzuylCQHkAAqMmAAKDWAlQF6a9IWNmnYY9BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 14', 'en': '🎥 Kids Video 14'},
        'price': 10,
        'files': [
            'BAACAgQAAxkBAAPeaoGEFh__YOZMpyQR0zeW9A2CTy0AAqQmAAKDWAlQznUfrhZe6Jk9BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 15', 'en': '🎥 Kids Video 15'},
        'price': 10,
        'files': [
            'BAACAgQAAxkBAAPmojiEHnGVlF6BicCOMS5GqgukazIAAqYmAAKDWAlQ0V8G4lEDz2o9BA'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو صغار 16', 'en': '🎥 Kids Video 16'},
        'price': 15,
        'files': [
            'BAACAgQAAxkBAAPkaoGEJodz2PK7F45B7O73km3tm1sAAqcmAAKDWAlQ1A41dgTSaic9BA'
        ],
    },
]

ADULT_VIDEOS = [
    {
        'title': {'ar': '🎥 فيديو 1', 'en': '🎥 Video 1'},
        'price': 20,
        'files': [
            'BAACAgQAAxkBAAICjGqCGrEiV7Izcz9qN8wqilrpYDaKAAIvJAACg1gRUNUAAd7MCAkY2T0E'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 2', 'en': '🎥 Video 2'},
        'price': 30,
        'files': [
            'BAACAgQAAxkBAAICjmqCGv6w7vwy0slR_wpKetrsIItfAAI2JAACg1gRUDumtqekuc_jPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 3', 'en': '🎥 Video 3'},
        'price': 30,
        'files': [
            'BAACAgQAAxkBAAICkmqCGwcQIbLuXYOhBsG5WGk9-DZHAAI4JAACg1gRUA6hr8VAQhNhPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 4', 'en': '🎥 Video 4'},
        'price': 15,
        'files': [
            'BAACAgQAAxkBAAIClGqCGwjTOVDW6JcINnjprFruZzFKAAI5JAACg1gRUFr7RMh-Pva9PQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 5', 'en': '🎥 Video 5'},
        'price': 10,
        'files': [
            'BAACAgQAAxkBAAIClmqCGwk0XFlNgtEMLqDReTycfO55AAI6JAACg1gRUA6Ml4wRvatDPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 6', 'en': '🎥 Video 6'},
        'price': 10,
        'files': [
            'BAACAgQAAxkBAAICmGqCGw0kF29b-N__YWdBaOEwfkO6AAI7JAACg1gRUGKvHwQwquxSPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 7', 'en': '🎥 Video 7'},
        'price': 10,
        'files': [
            'BAACAgQAAxkBAAICmmqCGw8HhnajzrJ62J9SLWeuikHsAAI8JAACg1gRUEXlMsAAAV6-Hj0E'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 8', 'en': '🎥 Video 8'},
        'price': 20,
        'files': [
            'BAACAgQAAxkBAAICnGqCGxOlWNE36stky3rG9l97rbx-AAI9JAACg1gRUAeQZGssGCfoPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 9', 'en': '🎥 Video 9'},
        'price': 30,
        'files': [
            'BAACAgQAAxkBAAICnmqCGyHRdovyr7nqeVDYfJvlj1WiAAI-JAACg1gRUIqbMOzIwjG5PQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 10', 'en': '🎥 Video 10'},
        'price': 15,
        'files': [
            'BAACAgQAAxkBAAICoGqCG5T0zPDmzzGSogW1S9-J8RKLAAJEJAACg1gRUKs5VbVhQMB7PQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 11', 'en': '🎥 Video 11'},
        'price': 40,
        'files': [
            'BAACAgQAAxkBAAICqmqCHXlPoTXzpBDPjkCGDZYAAbed2QACTCQAAoNYEVAzldH9phiQaT0E'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 12', 'en': '🎥 Video 12'},
        'price': 20,
        'files': [
            'BAACAgQAAxkBAAICsGqCHfrAbyGNztcVOrHhZ642FakbAAJPJAACg1gRUFTogfBxSZLiPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 13', 'en': '🎥 Video 13'},
        'price': 25,
        'files': [
            'BAACAgQAAxkBAAICrmqCHeTeXMQn5Fjc7axu9MmZQ8l-AAJOJAACg1gRUIr1F7r_20dpPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 14', 'en': '🎥 Video 14'},
        'price': 20,
        'files': [
            'BAACAgQAAxkBAAICsmqCHo9E7S1jzZPxIsDNmNMwJ96EAAJSJAACg1gRUHVh4c_uVOYFPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 15', 'en': '🎥 Video 15'},
        'price': 15,
        'files': [
            'BAACAgQAAxkBAAICtmqCHpfJ5wU-lyw8I_bTaDnUJ8yyAAJTJAACg1gRUMFe-4swmKcfPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 16', 'en': '🎥 Video 16'},
        'price': 10,
        'files': [
            'BAACAgQAAxkBAAICuGqCHpqZMBCgnGh_f1gcDhDdwLWMAAJUJAACg1gRUA0pXQ_EkvgXPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 17', 'en': '🎥 Video 17'},
        'price': 10,
        'files': [
            'BAACAgQAAxkBAAICumqCHzYI4xqZ8aDq_F7S3r5Q1PKBAAJVJAACg1gRUHGM782ieIstPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 18', 'en': '🎥 Video 18'},
        'price': 20,
        'files': [
            'BAACAgQAAxkBAAICvGqCIA4thUBn8_TC2v0M6DBK_0vhAAJWJAACg1gRUKZWe0hL9uhWPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 19', 'en': '🎥 Video 19'},
        'price': 15,
        'files': [
            'BAACAgQAAxkBAAICvGqCIA4thUBn8_TC2v0M6DBK_0vhAAJWJAACg1gRUKZWe0hL9uhWPQQ'
        ],
    },
    {
        'title': {'ar': '🎥 فيديو 20', 'en': '🎥 Video 20'},
        'price': 50,
        'files': [
            'BAACAgQAAxkBAAICvmqCIB-ZRTKxp6Br91reeXDjjNUcAAJXJAACg1gRUM3PiU6chC91PQQ'
        ],
    },
]

TEXTS = {
    'ar': {
        'welcome': '✨ أهلاً بك في البوت الخاص بنا! ✨\n\nاختر من القائمة أدناه ما يناسبك:',
        'btn_kids': '🎥 فيديوهات صغار',
        'btn_adults': '🎥 فيديوهات كبار',
        'btn_free': '🎁 فيديوهات مجانية (25)',
        'btn_discount': '🎁 عرض خاص 50%',
        'btn_lang': '🌐 تغيير اللغة / Change Language',
        'kids_header': '🎥 قائمة فيديوهات الصغار:',
        'adults_header': '🎥 قائمة فيديوهات الكبار:',
        'free_header': '🎁 قائمة الفيديوهات المجانية:',
        'btn_back': '🔙 العودة للقائمة الرئيسية',
        'block_photo': '⚠️ عذراً، إرسال الصور أو اللقطات (Screenshots) غير متاح.',
    },
    'en': {
        'welcome': '✨ Welcome to Our Bot! ✨\n\nPlease choose an option from below:',
        'btn_kids': '🎥 Kids Videos',
        'btn_adults': '🎥 Adult Videos',
        'btn_free': '🎁 Free Videos (25)',
        'btn_discount': '🎁 Special Offer 50%',
        'btn_lang': '🌐 Change Language / تغيير اللغة',
        'kids_header': '🎥 Kids Videos List:',
        'adults_header': '🎥 Adult Videos List:',
        'free_header': '🎁 Free Videos List:',
        'btn_back': '🔙 Back to Main Menu',
        'block_photo': '⚠️ Sorry, sending photos or screenshots is not allowed.',
    },
}

@bot.message_handler(content_types=['video'])
def get_file_id(message):
  bot.reply_to(
      message,
      f'⚙️ **File ID الخاص بالفيديو:**\n`{message.video.file_id}`',
      parse_mode='Markdown',
  )

@bot.message_handler(content_types=['photo'])
def block_photos(message):
  user_id = str(message.chat.id)
  data = load_data()
  lang = data.get(user_id, {}).get('lang', 'ar') or 'ar'
  try:
    bot.delete_message(message.chat.id, message.message_id)
  except:
    pass
  bot.send_message(message.chat.id, TEXTS[lang]['block_photo'])

@bot.message_handler(commands=['start'])
def start_cmd(message):
  user_id = str(message.from_user.id)
  args = message.text.split()
  data = load_data()

  if user_id not in data:
    data[user_id] = {
        'lang': None,
        'invited_count': 0,
        'referred_by': None,
        'discount_active': False
    }
    
    # التحقق من رابط الدعوة (أن شخصاً دعاه واستخدم البوت)
    if len(args) > 1:
      referrer_id = args[1]
      if referrer_id != user_id and referrer_id in data:
        data[user_id]['referred_by'] = referrer_id
        data[referrer_id]['invited_count'] = data[referrer_id].get('invited_count', 0) + 1
        
        # تفعيل الخصم تلقائياً إذا وصل إلى 20 دعوة
        if data[referrer_id]['invited_count'] >= 20:
          data[referrer_id]['discount_active'] = True
          
    save_data(data)

  if data[user_id].get('lang'):
    show_main_menu(message.chat.id, data[user_id]['lang'])
  else:
    show_language_selection(message.chat.id)

def show_language_selection(chat_id):
  markup = types.InlineKeyboardMarkup(row_width=2)
  btn_ar = types.InlineKeyboardButton('العربية 🇸🇦', callback_data='set_lang_ar')
  btn_en = types.InlineKeyboardButton('English 🇬🇧', callback_data='set_lang_en')
  markup.add(btn_ar, btn_en)

  msg = 'مرحباً بك! يرجى اختيار لغتك المفضلة.\nWelcome! Please select your preferred language.'
  bot.send_message(chat_id, msg, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('set_lang_'))
def set_language(call):
  try:
    bot.answer_callback_query(call.id)
  except:
    pass
    
  lang = call.data.split('_')[2]
  user_id = str(call.message.chat.id)
  data = load_data()

  if user_id not in data:
    data[user_id] = {'invited_count': 0, 'discount_active': False}

  data[user_id]['lang'] = lang
  save_data(data)

  try:
    bot.delete_message(call.message.chat.id, call.message.message_id)
  except:
    pass
  show_main_menu(call.message.chat.id, lang)

def show_main_menu(chat_id, lang):
  t = TEXTS[lang]
  user_id = str(chat_id)
  data = load_data()
  user_data = data.get(user_id, {})
  
  markup = types.InlineKeyboardMarkup(row_width=1)

  btn_kids = types.InlineKeyboardButton(t['btn_kids'], callback_data='show_kids')
  btn_adults = types.InlineKeyboardButton(t['btn_adults'], callback_data='show_adults')
  btn_free = types.InlineKeyboardButton(t['btn_free'], callback_data='show_free')
  
  markup.add(btn_kids, btn_adults, btn_free)

  # إظهار زر العرض الخاص (الخصم) فقط إذا كان مفعلاً
  if user_data.get('discount_active', False):
    btn_discount = types.InlineKeyboardButton(t['btn_discount'], callback_data='show_discount')
    markup.add(btn_discount)

  btn_lang = types.InlineKeyboardButton(t['btn_lang'], callback_data='change_lang')
  markup.add(btn_lang)

  bot.send_message(chat_id, t['welcome'], reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data == 'change_lang')
def change_lang_callback(call):
  try:
    bot.answer_callback_query(call.id)
  except:
    pass
  try:
    bot.delete_message(call.message.chat.id, call.message.message_id)
  except:
    pass
  show_language_selection(call.message.chat.id)

@bot.callback_query_handler(func=lambda call: call.data == 'show_free')
def show_free_callback(call):
  try:
    bot.answer_callback_query(call.id)
  except:
    pass
    
  user_id = str(call.message.chat.id)
  data = load_data()
  lang = data.get(user_id, {}).get('lang', 'ar') or 'ar'
  t = TEXTS[lang]

  markup = types.InlineKeyboardMarkup(row_width=1)

  for i, item in enumerate(FREE_VIDEOS):
    title = item['title'][lang]
    markup.add(types.InlineKeyboardButton(f'{title} | 🆓 مجاناً', callback_data=f'get_free_{i}'))

  markup.add(types.InlineKeyboardButton(t['btn_back'], callback_data='back_main'))
  
  try:
    bot.edit_message_text(
        t['free_header'],
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup,
        parse_mode='Markdown',
    )
  except Exception as e:
    print(f"Error in show_free: {e}")

@bot.callback_query_handler(func=lambda call: call.data.startswith('get_free_'))
def handle_free_video(call):
  try:
    bot.answer_callback_query(call.id, 'جاري إرسال الفيديو...')
  except:
    pass
    
  index = int(call.data.split('_')[2])
  item = FREE_VIDEOS[index]
  user_id = str(call.message.chat.id)

  data = load_data()
  lang = data.get(user_id, {}).get('lang', 'ar') or 'ar'
  title = item['title'][lang]

  file_id = item['files'][0]
  caption = (
      f'✨ **{title}**\n\nمشاهدة ممتعة! 🎬'
      if lang == 'ar'
      else f'✨ **{title}**\n\nEnjoy watching! 🎬'
  )

  try:
    bot.send_video(
        call.message.chat.id,
        video=file_id,
        caption=caption,
        parse_mode='Markdown',
    )
  except Exception as e:
    print(f"Error sending free video: {e}")
    bot.send_message(
        call.message.chat.id,
        '⚠️ عذراً، تعذر إرسال الفيديو.' if lang == 'ar' else '⚠️ Sorry, failed to send video.',
    )

@bot.callback_query_handler(func=lambda call: call.data == 'show_kids')
def show_kids_callback(call):
  try:
    bot.answer_callback_query(call.id)
  except:
    pass
    
  user_id = str(call.message.chat.id)
  data = load_data()
  lang = data.get(user_id, {}).get('lang', 'ar') or 'ar'
  t = TEXTS[lang]
  discount = data.get(user_id, {}).get('discount_active', False)

  markup = types.InlineKeyboardMarkup(row_width=1)

  for i, item in enumerate(KIDS_VIDEOS):
    original_price = item['price']
    # تطبيق خصم 50% إذا كان العرض مفعل للمستخدم
    price = int(original_price * 0.5) if discount else original_price
    title = item['title'][lang]
    price_text = f'⭐ {price} (خصم 50%)' if discount else f'⭐ {original_price}'
    markup.add(types.InlineKeyboardButton(f'{title} | {price_text}', callback_data=f'buy_kids_{i}'))

  markup.add(types.InlineKeyboardButton(t['btn_back'], callback_data='back_main'))
  
  try:
    bot.edit_message_text(
        t['kids_header'],
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup,
        parse_mode='Markdown',
    )
  except Exception as e:
    print(f"Error in show_kids: {e}")

@bot.callback_query_handler(func=lambda call: call.data == 'show_adults')
def show_adults_callback(call):
  try:
    bot.answer_callback_query(call.id)
  except:
    pass
    
  user_id = str(call.message.chat.id)
  data = load_data()
  lang = data.get(user_id, {}).get('lang', 'ar') or 'ar'
  t = TEXTS[lang]
  discount = data.get(user_id, {}).get('discount_active', False)

  markup = types.InlineKeyboardMarkup(row_width=1)

  for i, item in enumerate(ADULT_VIDEOS):
    original_price = item['price']
    # تطبيق خصم 50% إذا كان العرض مفعل للمستخدم
    price = int(original_price * 0.5) if discount else original_price
    title = item['title'][lang]
    price_text = f'⭐ {price} (خصم 50%)' if discount else f'⭐ {original_price}'
    markup.add(types.InlineKeyboardButton(f'{title} | {price_text}', callback_data=f'buy_adults_{i}'))

  markup.add(types.InlineKeyboardButton(t['btn_back'], callback_data='back_main'))
  
  try:
    bot.edit_message_text(
        t['adults_header'],
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup,
        parse_mode='Markdown',
    )
  except Exception as e:
    print(f"Error in show_adults: {e}")

@bot.callback_query_handler(func=lambda call: call.data == 'show_discount')
def show_discount_callback(call):
  try:
    bot.answer_callback_query(call.id)
  except:
    pass
  user_id = str(call.message.chat.id)
  data = load_data()
  lang = data.get(user_id, {}).get('lang', 'ar') or 'ar'
  t = TEXTS[lang]

  bot_info = bot.get_me()
  referral_link = f"https://t.me/{bot_info.username}?start={user_id}"
  invited_count = data.get(user_id, {}).get('invited_count', 0)

  if lang == 'ar':
    msg = f"🎉 **مبروك! لقد حصلت على خصم 50%**\n\nعدد الأشخاص الذين دعوتهم واستخدموا البوت: `{invited_count}/20`\n\n🔗 رابط الدعوة الخاص بك:\n`{referral_link}`\n\nشارك الرابط مع أصدقائك لاستخدام البوت والاستمتاع بالأسعار المخفضة!"
  else:
    msg = f"🎉 **Congratulations! You unlocked a 50% discount**\n\nInvited users who used the bot: `{invited_count}/20`\n\n🔗 Your Referral Link:\n`{referral_link}`\n\nShare this link with your friends to enjoy discounted prices!"

  markup = types.InlineKeyboardMarkup()
  markup.add(types.InlineKeyboardButton(t['btn_back'], callback_data='back_main'))

  try:
    bot.edit_message_text(
        msg,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup,
        parse_mode='Markdown',
    )
  except Exception as e:
    print(f"Error in show_discount: {e}")

@bot.callback_query_handler(func=lambda call: call.data == 'back_main')
def back_main_callback(call):
  try:
    bot.answer_callback_query(call.id)
  except:
    pass
    
  user_id = str(call.message.chat.id)
  data = load_data()
  lang = data.get(user_id, {}).get('lang', 'ar') or 'ar'
  t = TEXTS[lang]
  user_data = data.get(user_id, {})

  markup = types.InlineKeyboardMarkup(row_width=1)
  btn_kids = types.InlineKeyboardButton(t['btn_kids'], callback_data='show_kids')
  btn_adults = types.InlineKeyboardButton(t['btn_adults'], callback_data='show_adults')
  btn_free = types.InlineKeyboardButton(t['btn_free'], callback_data='show_free')
  
  markup.add(btn_kids, btn_adults, btn_free)

  if user_data.get('discount_active', False):
    btn_discount = types.InlineKeyboardButton(t['btn_discount'], callback_data='show_discount')
    markup.add(btn_discount)

  btn_lang = types.InlineKeyboardButton(t['btn_lang'], callback_data='change_lang')
  markup.add(btn_lang)

  try:
    bot.edit_message_text(
        t['welcome'],
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup,
        parse_mode='Markdown',
    )
  except Exception as e:
    print(f"Error in back_main: {e}")

@bot.callback_query_handler(func=lambda call: call.data.startswith('buy_'))
def handle_payment(call):
  try:
    parts = call.data.split('_')
    category = parts[1]
    index = int(parts[2])

    item = KIDS_VIDEOS[index] if category == 'kids' else ADULT_VIDEOS[index]
    user_id = str(call.message.chat.id)

    data = load_data()
    lang = data.get(user_id, {}).get('lang', 'ar') or 'ar'
    discount = data.get(user_id, {}).get('discount_active', False)

    original_price = item['price']
    price = int(original_price * 0.5) if discount else original_price
    title = item['title'][lang]

    bot.answer_callback_query(call.id, f'السعر المطلوب: {price} نجوم')

    media_list = [types.InputMediaVideo(media=fid) for fid in item['files']]

    caption = (
        f'✨ شكراً لثقتك!\nاستمتع بمشاهدة: {title}\n💰 السعر المدفوع: {price} نجوم.'
        if lang == 'ar'
        else f'✨ Thank you!\nEnjoy watching: {title}\n💰 Paid Price: {price} Stars.'
    )

    bot.send_paid_media(
        chat_id=call.message.chat.id,
        star_count=price,
        media=media_list,
        caption=caption,
    )
  except Exception as e:
    print(f"Error in handle_payment: {e}")
    try:
      bot.answer_callback_query(call.id, "حدث خطأ ما، يرجى المحاولة لاحقاً.")
    except:
      pass

if __name__ == '__main__':
  bot.remove_webhook()
  print('🚀 البوت يعمل الآن بنجاح...')
  bot.infinity_polling()
