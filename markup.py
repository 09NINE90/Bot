from telebot import types

# =========== Города

btnInfo = types.KeyboardButton(text='/info')
btnReg = types.KeyboardButton(text='/reg')
mainMenu = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True, resize_keyboard=True).add(btnInfo, btnReg)

# =========== Номер телефона

btnTel = types.KeyboardButton(text='Отправить свой номер телефона', request_contact=True)
telMenu = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True, resize_keyboard=True).add(btnTel)
# =========== Города

btnEkb = types.KeyboardButton(text='Екатеринбург')
btnMsk = types.KeyboardButton(text='Москва')
cityMenu = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True, resize_keyboard=True).add(btnEkb, btnMsk)


# =========== Ночи

btn7 = types.KeyboardButton(text='7')
btn10 = types.KeyboardButton(text='10')
btn14 = types.KeyboardButton(text='14')
nightMenu = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True, resize_keyboard=True).add(btn7, btn10, btn14)


# =========== Питание

btnNut1 = types.KeyboardButton(text='Завтраки')
btnNut2 = types.KeyboardButton(text='Завтрак-ужин')
btnNut3 = types.KeyboardButton(text='Всё включено')
btnNut4 = types.KeyboardButton(text='Всё включено LUX')
nutritionMenu = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True).add(btnNut1, btnNut2, btnNut3, btnNut4)

# =========== Питание

btn1 = types.KeyboardButton(text='1')
btn2 = types.KeyboardButton(text='2')
btn3 = types.KeyboardButton(text='3')
btn4 = types.KeyboardButton(text='4')
btn5 = types.KeyboardButton(text='5')
btn6 = types.KeyboardButton(text='6')
btn8 = types.KeyboardButton(text='8')
btn9 = types.KeyboardButton(text='9')
btn0 = types.KeyboardButton(text='0')
numMenu = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True).add(btn1, btn2, btn3, btn4,
                                                                                             btn5, btn0)