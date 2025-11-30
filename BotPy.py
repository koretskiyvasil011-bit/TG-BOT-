import telebot
from telebot import types

TOKEN = "8308238539:AAHTSpFzqp-AzHHic4_9YqRHISEw-G1U-IQ"

bot = telebot.TeleBot(TOKEN)

# 12 тем
topics = [
    "Многогранники",
    "Призма. Паралелепіпед",
    "Піраміда",
    "Перерізи многогранників",
    "Циліндр",
    "Конус",
    "Куля і сфера",
    "Площі поверхонь геометричних тіл",
    "Об’єм призми",
    "Об’єм піраміди",
    "Об’єм конуса та циліндра",
    "Об’єм кулі"
]

# Унікальні тексти для кожної теми
data = {
    "Многогранники": {
        "Теорія": "📘 https://wayground.com/join/presentation/678398f0e64648de05a4a130/start?from=admin&preview=true",
        "Відео": "🎥 https://www.youtube.com/watch?v=c06rZ_pTcQU ",
        "Тест": "📝 https://learningapps.org/watch?v=pd3ji3dda23."
    },
    "Призма. Паралелепіпед": {
        "Теорія": "📘 Теорія: https://wayground.com/join/presentation/6783ce8695908de5d02d5a7f/start?from=admin&preview=true",
        "Відео": "🎥 Відео: https://www.youtube.com/watch?v=FP93ajYmm9o",
        "Тест": "📝 https://learningapps.org/watch?v=puiy51hp523"
    },
    "Піраміда": {
        "Теорія": "📘 Теорія пірамід:https://wayground.com/join/presentation/6783db3e931f5248c1579765/start?preview=true ",
        "Відео": "🎥 ВШО: https://www.youtube.com/watch?v=pZ4fpG1Pw7E ",
        "Тест": "📝https://learningapps.org/watch?v=pknzrw36c23 "
    },
    "Перерізи многогранників": {
        "Теорія": "📘 Теорія:https://wayground.com/join/presentation/6783e37d895d0c3b2202cd8a/start?from=admin&preview=true ",
        "Відео": "🎥 Відео: https://www.youtube.com/watch?v=qPRX7OZyFJM",
        "Тест": "📝 https://learningapps.org/watch?v=pknzrw36c23 ."
    },
    "Циліндр": {
        "Теорія": "📘 Теорія:https://wayground.com/join/presentation/6783ea588de0a69b9e2a2751/start?from=admin&preview=true ",
        "Відео": "🎥 Циліндр: https://www.youtube.com/watch?v=xe3IUL4JuBs ",
        "Тест": "📝https://learningapps.org/watch?v=pysyci8av23 ."
    },
    "Конус": {
        "Теорія": "📘 Теорія:https://wayground.com/join/presentation/67852d87746cf174c370f29c/start?from=admin&preview=true ",
        "Відео": "🎥 Відео:https://www.youtube.com/watch?v=aGBefvv4ULg ",
        "Тест": "📝https://learningapps.org/watch?v=pvzbxovst23 "
    },
    "Куля і сфера": {
        "Теорія": "📘 Теорія:https://wayground.com/join/presentation/67853c0a09379b36f7718027/start?from=admin&preview=true ",
        "Відео": "🎥 ВШО: https://www.youtube.com/watch?v=iSJ9wldasac .",
        "Тест": "📝https://learningapps.org/watch?v=p57tura8c23 "
    },
    "Площі поверхонь геометричних тіл": {
        "Теорія": "📘 Теорія:https://wayground.com/join/presentation/6785487fc14fd846b45216f8/start?from=admin&preview=true ",
        "Відео": "🎥 Відео: https://www.youtube.com/watch?v=cLFpK-IubN8 ",
        "Тест": "📝 https://learningapps.org/watch?v=pfjic7m9k23"
    },
    "Об’єм призми": {
        "Теорія": "📘 Теорія:https://wayground.com/join/presentation/678cbe61b5ec1be0cf4a57aa/start?from=admin&preview=true ",
        "Відео": "🎥 https://www.youtube.com/watch?v=NEyn-ukABqQ ",
        "Тест": "📝 https://learningapps.org/watch?v=py5wa5o8323"
    },
    "Об’єм піраміди": {
        "Теорія": "📘 Теорія:https://wayground.com/join/presentation/678cc47ee847d3547ed67063/start?from=admin&preview=true",
        "Відео": "🎥 Відео https://www.youtube.com/watch?v=rclprPTHZo0 ",
        "Тест": "📝 https://learningapps.org/watch?v=pxyvry2kc23"
    },
    "Об’єм конуса та циліндра": {
        "Теорія": "📘 Теорія:https://wayground.com/join/presentation/678cca25ee176d02d99f02e0/start?from=admin&preview=true ",
        "Відео": "🎥 Об'єм конуса: https://www.youtube.com/watch?v=PBYkdiyH5e4 Об'єм циліндраhttps://www.youtube.com/watch?v=j7xq52Vjv14:",
        "Тест": "📝https://learningapps.org/watch?v=pvzbxovst23  https://learningapps.org/watch?v=pg5gx1o5a23 "
    },
    "Об’єм кулі": {
        "Теорія": "📘 Теорія:https://wayground.com/join/presentation/678ccde272497f6629451b4b/start?from=admin&preview=true ",
        "Відео": "🎥 Відео:https://www.youtube.com/watch?v=PSVBiJ4thxs .",
        "Тест": "📝 https://learningapps.org/watch?v=p57tura8c23"
    }
}

# Збереження вибору
last_topic = ""

# --- Головне меню (12 кнопок по 3 в ряд) ---
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    row = []
    for i, t in enumerate(topics, start=1):
        row.append(types.KeyboardButton(f"{i}. {t}"))
        if len(row) == 3:
            markup.row(*row)
            row = []
    if row:
        markup.row(*row)
    return markup

# --- Підменю ---
def submenu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Теорія", "Відео ВШО", "Тест")
    markup.row("⬅️ Назад")
    return markup

# --- START ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Обери тему:", reply_markup=main_menu())

# --- Натискання 12 основних кнопок ---
@bot.message_handler(func=lambda m: any(m.text.startswith(str(i)) for i in range(1, 13)))
def choose_topic(message):
    global last_topic
    last_topic = message.text.split(". ", 1)[1]   # отримуємо саму назву теми
    bot.send_message(message.chat.id, f"Обрана тема: {last_topic}", reply_markup=submenu())

# --- Натискання підкнопок ---
@bot.message_handler(func=lambda m: m.text in ["Теорія", "Відео ВШО", "Тест"])
def send_material(message):
    t = last_topic

    if message.text == "Теорія":
        text = data[t]["Теорія"]
    elif message.text == "Відео ВШО":
        text = data[t]["Відео"]
    else:
        text = data[t]["Тест"]

    bot.send_message(message.chat.id, text)

# --- Назад ---
@bot.message_handler(func=lambda m: m.text == "⬅️ Назад")
def back(message):
    bot.send_message(message.chat.id, "Повертаюсь до меню:", reply_markup=main_menu())


print("BOT RUNNING...")
bot.infinity_polling()
