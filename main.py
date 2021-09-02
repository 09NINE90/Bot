import config
import markup as nav
import telebot
from telebot import types  # кнопки
from string import Template

bot = telebot.TeleBot(config.token)

user_dict = {}


class User:
    def __init__(self, fullname):
        self.fullname = fullname

        keys = ['phone', 'city', 'date',
                'night', 'nutrition', 'adults',
                'child']

        for key in keys:
            self.key = None


# если  /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте, " + message.from_user.first_name + "! \n"
                           "Я помогу подобрать Вам тур, чтобы сэкономить "
                           "Ваше время и время агента!", reply_markup=nav.mainMenu)



@bot.message_handler(commands=['info'])
def send_info(message):
    bot.send_message(message.chat.id, "ИНФОРМАЦИЯ О РАБОТЕ БОТА:\n"
"Команды бота:\n"
"#########################\n"                                     
"\n/info - вызов этого сообщения\n"
"/reg - начать заполнение заявки\n"
"\n#########################\n"                                      
"/city - выбор города вылета\n"
"/date - предполагаемая дата вылета\n"
"/numofnight - количество ночей\n"
"/sysnutrition - система питания\n"
"/numofadults - количество взрослых\n"
"/numofchild - количество детей\n"
"\nЭтот бот поможет сэкономить Ваше время и время агента!\n"
"Гранд Тур бот соберет основную информацию о Вашем планируемом путешевствии и отправит данные агенту!")


# /reg
@bot.message_handler(commands=["reg"])
def user_fam(message):

        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        # удалить старую клавиатуру
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'Фамилия Имя Отчество')
        bot.register_next_step_handler(msg, process_fam_step)


def process_fam_step(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg = bot.send_message(chat_id, 'Ваш номер телефона')
        bot.register_next_step_handler(msg, process_phone_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_phone_step(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, 'Ваш город вылета?', reply_markup=nav.cityMenu)
        bot.register_next_step_handler(msg, process_date_step)

    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
        bot.register_next_step_handler(msg, process_phone_step)


def process_date_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.city = message.text

        msg = bot.send_message(chat_id, 'Введите дату вылета:')
        bot.register_next_step_handler(msg, process_night_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_night_step(message):
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.date = message.text

        msg = bot.send_message(chat_id, 'Введите количество ночей', reply_markup=nav.nightMenu)
        bot.register_next_step_handler(msg, process_nutrition_step)


def process_nutrition_step(message):
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.night = message.text

        msg = bot.send_message(chat_id, 'Выберите систему питания:', reply_markup=nav.nutritionMenu)
        bot.register_next_step_handler(msg, process_adults_step)


def process_adults_step(message):
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.nutrition = message.text

        msg = bot.send_message(chat_id, 'Введите количество взрослых:', reply_markup=nav.numMenu)
        bot.register_next_step_handler(msg, process_child_step)


def process_child_step(message):
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.adults = message.text

        msg = bot.send_message(chat_id, 'Введите количество детей:', reply_markup=nav.numMenu)
        bot.register_next_step_handler(msg, process_chil_step)


def process_chil_step(message):
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.child = message.text
        # ваша заявка "Имя пользователя"
        bot.send_message(chat_id, getRegData(user, 'Ваша заявка', message.from_user.first_name), parse_mode="Markdown", reply_markup=nav.mainMenu)
        # отправить в группу
        bot.send_message(config.chat_id, getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")


# формирует вид заявки регистрации
# нельзя делать перенос строки Template
# в send_message должно стоять parse_mode="Markdown"
def getRegData(user, title, name):
    t = Template(
        '$title *$name*\nФИО: *$fullname* \nТелефон: *$phone*\nГород вылета: *$userCity* \nДата вылета: *$date* \nКоличество ночей: *$night* \nСистема питания: *$nutrition* \nКоличество взрослых: *$adults* \nКоличество детей: *$child*')

    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'fullname': user.fullname,
        'phone': user.phone,
        'date': user.date,
        'night': user.night,
        'nutrition': user.nutrition,
        'adults': user.adults,
        'child': user.child,
    })


if __name__ == '__main__':
    bot.polling(none_stop=True)
