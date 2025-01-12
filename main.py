import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

schedule = {
    "Понедельник": ["Алгебра 9:00 - 9:40", "Геометрия 9:50 - 10:30", "Русский язык 10:40 - 11:20", "Литература 11:40 - 12:20", "История 12:40 - 13:20", "Химия 13:30 - 14:10", "Биология 14:20 - 15:00"],
    "Вторник": ["Русский 9:00 - 9:40", "Алгебра 9:50 - 10:30", "Литература 10:40 - 11:20", "География 11:40 - 12:20", "Обществознание 12:40 - 13:20", "Геометрия 13:30 - 14:10", "Физкультура 14:20 - 15:00"],
    "Среда": ["Информатика 9:00 - 9:40", "Обществознание 9:50 - 10:30", "Физкультура 10:40 - 11:20", "Английский язык 11:40 - 12:20", "Химия 12:40 - 13:20", "Музыка 13:30 - 14:10"],
    "Четверг": ["Русский язык 9:00 - 9:40", "Алгебра 9:50 - 10:30", "География 10:40 - 11:20", "Английский Язык 11:40 - 12:20", "Геометрия 12:40 - 13:20", "История 13:30 - 14:10", "Биология 14:20 - 15:00", "Физика 15:10 - 15:50"],
    "Пятница": ["Физика 9:00 - 9:40", "Обж 9:50 - 10:30", "Химия 10:40 - 11:20", "Вероятность и статистика 11:40 - 12:20", "Алгебра 12:40 - 13:20", "История 13:30 - 14:10", "Труды 14:20 - 15:00"]
}

def create_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    schedule_button = types.KeyboardButton("Получить расписание")
    markup.add(schedule_button)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    markup = create_buttons()
    bot.send_message(message.chat.id, "Мы - онлайн-школа, стремящаяся обеспечить наших учеников удобными и эффективными инструментами для обучения. Для того, чтобы получить расписание, нажмите на кнопку ниже.", reply_markup=markup)


@bot.message_handler(commands=['help'])
def start(message):
    markup = create_buttons()
    bot.send_message(message.chat.id, "Нажимите на кнопку <<Получить расписание>> чтобы получить расписание всех уроков на неделю!!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Получить расписание")
def get_schedule(message):
    schedule_text = "Расписание уроков: \n\n"
    if not schedule:
        schedule_text += "Расписание еще не задано. \n"
    else:
        for day, lessons in schedule.items():
            schedule_text += f"{day}:\n"
            for lesson in lessons:
                schedule_text += f"- {lesson}\n"

    bot.send_message(message.chat.id, schedule_text)

bot.polling(none_stop=True)

