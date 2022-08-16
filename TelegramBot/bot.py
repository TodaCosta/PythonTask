import json
import time
from pathlib import Path

import requests
import telebot
import datetime
import re
from telebot import types # импорт клавиатуры
import pytube
from pytube import YouTube



bot = telebot.TeleBot('')
# создали объект класса, инициализировали его





@bot.message_handler(commands = ['start'])
def start(message):
    message = bot.send_message(message.chat.id, "Пришли ссылку на видео",)
    bot.register_next_step_handler(message, vid)

def vid(message):
    youtube_video_url = message.text

    yt_obj = YouTube(youtube_video_url)
    filters =yt_obj.streams.filter(progressive=True, file_extension='mp4')
    filters.get_highest_resolution().download(filename=f'{yt_obj.title}.mp4')
    bot.send_message(message.chat.id, "Видео скачивается")
    video = open(f'{yt_obj.title}.mp4', 'rb')
    bot.send_video(message.chat.id, video)
    time.sleep(200)
    video.close()
    vid_fail = Path(f'{yt_obj.title}.mp4')
    vid_fail.unlink()







@bot.message_handler(commands=['ch'])
def handle_message(message):
    bot.send_message("@chenel_raw", "сообщение от бота", time.sleep(10))

#рассылка
@bot.message_handler(commands=['start'])
def start(message):
    with open('pers_id.txt', 'a+') as pers_id:
        print(message.chat.id, file=pers_id)

@bot.message_handler(commands=['rassilka'])
def rassylka(message):
    if message.chat.id == 308414940:
        for i in open('pers_id.txt', 'r').readlines():
            bot.send_message(i, 'массовая рассылка')

# @bot.message_handler(regexp='[0-9]+')
# def start(message):
#     answer = requests.get(f'http://numbersapi.com/{message.text}?json')
#     bot.send_message(message.chat.id, json.loads(answer.text)['text'])

@bot.message_handler(commands = ['getpost'])
def start(message):
    message = bot.send_message(message.chat.id, "Отправьте любой поисковой запрос!🔎",)
    bot.register_next_step_handler(message, reply)

def reply(message):
    saved_message = message.text
    first, second = '+'.join(message.text.split()), '%20'.join(message.text.split())
    bot.send_message(message.chat.id, f'<a href="https://www.google.com/search?q={first}"> Google</a>\n'
                                      f'<a href="https://yandex.ru/search/?lr=16&text={first}">Yandex</a>\n'
                                      f'<a href="https://www.youtube.com/results?search_query={first}">Yotube</a>\n'
                                      f'<a href="https://stepik.org/catalog/search?q={second}">Stepa</a>', parse_mode='HTML')

# @bot.message_handler(commands=['start', 'end'])
# def start(message): # message-объект
#     bot.send_message(message.chat.id, message.from_user.first_name) # message.chat.id==message.from_user.id
#     bot.send_message(message.chat.id, message.from_user.username)
#     date = message.date + 10800  # Прибавляем 3 часа (в секундах) к времени по UTC и получаем время по МСК!
#     bot.send_message(message.chat.id, datetime.datetime.utcfromtimestamp(date))
#     bot.send_message(message.chat.id, message.chat.id)

@bot.message_handler(commands=['text'])
def handle_message(message):
    bot.send_message(message.chat.id, '<i>Какой-то</i> текст', parse_mode='HTML')
    bot.send_message(message.chat.id, '<tg-spoiler> текст </tg-spoiler>', parse_mode='HTML')

BUY = 'Купить \U0001F381'
STONE = 'Камень с глазами'
BACK = 'Назад'
@bot.message_handler(commands=['магазин'])
@bot.message_handler(func=lambda message: message.text == BACK)
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text=BUY)
    kb.add(btn1)
    bot.send_message(message.chat.id, 'Добро пожаловть в интернет-магазин"Полезные товары"', reply_markup=kb)
@bot.message_handler(func=lambda message: message.text==BUY )
def start(message):
    kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn2 = types.KeyboardButton(text=STONE)
    btn3 = types.KeyboardButton(text=BACK)
    kb2.add(btn2, btn3)
    bot.send_message(message.chat.id, 'Что хотите купить', reply_markup=kb2)
@bot.message_handler(func=lambda message: message.text==STONE )
def start(message):
    file = open('stoun.jpg', 'rb')
    bot.send_photo(message.chat.id, file, caption="""Товар: Камень с глазами
Цена: 1000$
В наличии: 2""")

#разные кнопки для админа и пользователей
one = 'Добро пожаловать в магазин цифровых товаров'
two = 'Каталог 🎁'
three = 'Мой профиль 👤'
fo = 'FAQ'
five = 'Информация о боте 🗿'
six = 'Сделать рассылку 📢'

@bot.message_handler(commands=['вход'])
def start(message):
    kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) # one_time_keyboard=True убрать клаву при нажатии кнопки
    kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text=two)
    btn2 = types.KeyboardButton(text=three)
    btn3 = types.KeyboardButton(text=fo)
    btn4 = types.KeyboardButton(text=five)
    btn5 = types.KeyboardButton(text=six)
    kb1.add(btn1, btn2, btn3, btn4, btn5)
    kb2.add(btn1, btn2, btn3)
    if message.chat.id == 308414940:
        bot.send_message(308414940, 'Добро пожаловать в интернет-магазин "Полезные товары"', reply_markup=kb1)
    else:
        bot.send_message(message.chat.id, 'Добро пожаловать в интернет-магазин "Полезные товары"', reply_markup=kb2)
    time.sleep(5)
    #bot.send_message(message.chat.id, "Убираем клавиатуру", reply_markup=types.ReplyKeyboardRemove()) # убрать клаву

#url-кнопки
@bot.message_handler(commands=['ссылка'])
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='ссылка1', url='https://www.youtube.com/c/selfedu_rus')
    btn2 = types.InlineKeyboardButton(text='ссылка2', url='https://www.youtube.com/c/DjangoSchool')
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, 'выбери ссылку', reply_markup=kb)

#calback кнопки
@bot.message_handler(commands=['call'])
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    btn = types.InlineKeyboardButton(text='да', callback_data='btn1')
    btn1 = types.InlineKeyboardButton(text='нет', callback_data='btn2')
    kb.add(btn, btn1)
    bot.send_message(message.chat.id, 'выбери вариант ответа', reply_markup=kb)
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_calback(callback):
    if callback.data == 'btn1':
        bot.send_message(callback.message.chat.id, 'Вы согласны на обработку данных')
    elif callback.data == 'btn2':
        bot.send_message(callback.message.chat.id, 'Вы НЕ согласны')

#кнопки+
@bot.message_handler(commands=['крест'])
def start(message):
    kb = types.InlineKeyboardMarkup()
    b = types.InlineKeyboardButton(text='➕️', callback_data='+')
    kb.row(b).row(*[b] * 3).row(b)
    bot.send_message(message.chat.id, '+️', reply_markup=kb)




#удаление
# @bot.message_handler(content_types=['text','audio','video','photo','voice','sticker'])
# def delete_user_message(message):
#     bot.delete_message(message.chat.id, message.id)
#бот отвечает сообщением и удаляет его и польз-ля
# @bot.message_handler()
# def greating(message):
#     bot_message = bot.send_message(message.chat.id, "Здесь нет свободы слова")
#     time.sleep(2)
#     bot.delete_message(message.chat.id, message.id)
#     bot.delete_message(message.chat.id, bot_message.id)


#документ
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     my_file = open("file.txt", "w+", encoding='utf-8')
#     my_file.write(message.text)
#     my_file.close()
#     my_file = open("file.txt", 'r', encoding='utf-8')
#     bot.send_document(message.chat.id, my_file)

#отправить админу фото видео отправителя
# @bot.message_handler(content_types=['photo', 'video'])
# def handle_message(message):
#     if message.content_type == 'photo':
#         bot.send_photo(308414940, message.photo[0].file_id)
#     elif message.content_type == 'video':
#         bot.send_video(308414940, message.video.file_id)

# @bot.message_handler(content_types=['audio'])
# def handle_message(message):
#     bot.send_message(message.chat.id, f'Имя аудиофайла: {message.audio.file_name}')

@bot.message_handler(content_types=['sticker'])
def handle_message(message):
    bot.send_message(message.chat.id, message.sticker.file_id)
    bot.send_sticker(message.chat.id, message.sticker.file_id)

@bot.message_handler(commands=['бокс', 'перчатки'])
@bot.message_handler(func=lambda message: message.text == 'сумка')
def handle_message(message):
    file = open('bag.jpg', 'rb')
    bot.send_photo(message.chat.id, file, "фото")

@bot.message_handler(func=lambda message: message.text == 'бот')
def handle_message(message):
    bot.send_photo(message.chat.id, r'https://ibb.co/G557cNb')

#-----------------------------------------------------------------------------------
# @bot.message_handler(regexp="^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
# def handle_message(message):
#     bot.send_message(message.chat.id, 'Это номер телефона')
#
# @bot.message_handler(func=lambda m: True)
# def findkeywords(message):
#     bot.send_message(message.chat.id, 'Отправьте номер телефона')
#------------------------------------------------------------------------------------

def poli(message):
    message = message.text
    message = message.lower().replace(' ', '')
    return message == message[-1::-1]
    # message = message.text
    # message = re.sub(r'[ьъ]', '', message)
    # message = message.lower().split()
    # for i in range(len(message)):
    #     return message[i] == message[i - 1][::-1]
@bot.message_handler(func=poli)
def start(message):
    bot.send_message(message.chat.id, 'Палиндром')




#---------------------------
# ct = {'text': 'Это текст',
#     'audio': 'Это аудио',
#     'document': 'Это документ',
#     'photo': 'Это фото',
#     'sticker': 'Это стикер',
#     'video': 'Это видео',
#     'voice': 'Это голосовое сообщение',
#     'location': 'Это местоположение',
#     'contact': 'Это контакт',
#     'new_chat_members': 'Это новый участник чата',
#     'left_chat_member': 'Это участник вышел из чата',
#     'new_chat_title': 'Название чата изменено',
#     'new_chat_photo': 'Картинка чата изменена',
#     'delete_chat_photo': 'Картинка чата удалена',
#     'pinned_message': 'Сообщение закреплено'
#   }
# @bot.message_handler(content_types=ct.keys())
# def echo_all(message):
#     bot.send_message(message.chat.id, ct[message.content_type])
# ------------------------------------------------------------------

# def f(message):
#     return message.text == '1'
#
# @bot.message_handler(func=f)
# def start(message):
#     bot.reply_to(message, 'Hi')


def findkeyword(message):
    keywords = ['карт', 'card', 'cvv', 'код', 'code', 'bank']
    return any(word in message.text.lower() for word in keywords)
    # message = message.text
    # message = message.lower()
    # message = re.sub(r'[^\w\s]', '', message)
    # message = message.split()
    # flug = False
    # for i in keywords:
    #     for j in message:
    #         if i == j[:len(i)]:
    #             flug = True
    #             break
    # return flug
@bot.message_handler(func=findkeyword)
def start(message):
    bot.reply_to(message, 'Есть слово, связанное с картами')

def findThiev(message):
    w1, w2 = 'Edinaya Rossiya', '$¥€'
    return w1 in message.text and any(w in message.text for w in w2)
    # keywords = ['Edinaya Rossiya']
    # keywords2 = ['$', '¥', '€']
    # one = any(word in message.text for word in keywords)
    # two = any(word in message.text for word in keywords2)
    # return one and two
@bot.message_handler(func=findThiev)
def start(message):
    bot.reply_to(message, 'Есть слово, связанное с шифрованием')


@bot.message_handler(func=lambda message: True)
def start(message):
    bot.send_message(message.chat.id, f'"{message.text}"  И что? Всем наплевать... Зачем ты это написал, \U0001F921 ?')

bot.polling()
# метод polling ждёт сообщения от пользователей, выполняется всегда, никогда не закрывает скрипт,
# когда приходит сообщение, оно проходит проверку обработчиков handler
# если хоть 1 обработчик выдаст True, другие обр-ки не запустятся
