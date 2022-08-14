import telebot
from telebot import types

bot = telebot.TeleBot('1318704228:AAFt5rrfP_dMc_yi6-dCNAOdyEUI1mRbmio')

# создаем клавиатуру
keyboard = types.InlineKeyboardMarkup()

# добавляем на нее две кнопки
button1 = types.InlineKeyboardButton(text="ДА", callback_data="button1")
button2 = types.InlineKeyboardButton(text="НЕТ", callback_data="button2")
keyboard.add(button1)
keyboard.add(button2)

# создаем клавиатуру
keyboard1 = types.InlineKeyboardMarkup()

# добавляем на нее две кнопки
b1 = types.InlineKeyboardButton(text="ДА", callback_data="b1")
b2 = types.InlineKeyboardButton(text="НЕТ", callback_data="b2")
keyboard1.add(b1)
keyboard1.add(b2)


@bot.message_handler(commands=["start"])
def repeat_all_messages(message):

    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, "Привет 😊, ты зашёл сюда, потому что знаешь, что книги 📚 "
                                      "сейчас стали дорогим удовольствием 😔💰, цены варьируются от "
                                      "150 до 1000 рублей 😱. Но, благодаря мне 😃, ты сможешь читать "
                                      "абсолютно любые книги БЕСПЛАТНО 🤗!!! Хочешь узнать "
                                      "как 😏? (Нажми кнопку 'ДА')", reply_markup=keyboard)

# функция запустится, когда пользователь нажмет на кнопку
@bot.callback_query_handler(func=lambda call:call.data in ['button1','button2'])
def callback_inline_keyboard(call):
    if call.message:
        if call.data == "button1":
            bot.send_message(call.message.chat.id, "Отлично 😉! Администратор @irinab2021 добавит тебя в чат-бот 🤖 с "
                                                   "книгами 📚, где ты будешь вводить название книги или автора, а "
                                                   "бот будет присылать тебе книги для скачивания 📲. "
                                                   "Так же Администратор отправит 🤳 тебе подробную "
                                                   "инструкцию как скачаивать - куда жать, как сохранить."
                                                   " Добавить тебя в "
                                                   "чат-бот с книгами ☺?", reply_markup=keyboard1)
        if call.data == "button2":
            bot.send_message(call.message.chat.id, "Неправильный ответ. Нажми ДА")

@bot.callback_query_handler(func=lambda call:call.data in ['b1','b2'])
def callback_inline_keyboard1(call):
    if call.message:
        if call.data == "b1":
            bot.send_message(call.message.chat.id, "Добавление в чат-бот с книгами стоит "
                                                   "899руб. Ты 1 раз платишь за сам доступ, а "
                                                   "потом скачиваешь любые книги абсолютно бесплатно 😋! "
                                                   "Администратор предоставит инструкцию по скачиванию, а так же гарантии 📃 , "
                                                   "что бот работает. Напиши @irinab2021 (нажми на имя 👉 @irinab2021 - и сразу "
                                                   "перейдёшь в чат с администратором) - ответит как оплатить и "
                                                   "добавит в чат-бот с книгами.")
        if call.data == "b2":
            bot.send_message(call.message.chat.id, "Неправильный ответ. Нажми ДА")


bot.polling(none_stop=True)