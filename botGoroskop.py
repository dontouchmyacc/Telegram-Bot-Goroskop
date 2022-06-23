import random
import telebot
from telebot import types
bot = telebot.TeleBot("5374695514:AAHZKfMj2B9rhA_-Zu57ASMdgRUtt1k2gI4")

name = ''

@bot.message_handler(commands=['help','start'])
def start1(message):
    sti = open('2124661471689312712.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.from_user.id,'Добро пожаловать в гороскоп Дня\nВведите ваше имя')
    bot.register_next_step_handler(message,get_name)

@bot.message_handler(content_types = ['text'])
def goroskop(message):
    if message.text =='Рыбы':
        sti3 = open('2124661471689312796.webp','rb')
        bot.send_sticker(message.chat.id, sti3)
        bot.send_message(message.chat.id,'Рыбки.Вас ждет увлекательный день')
    elif message.text =='Козерог':
        sti4 = open('6021468720776349700.webp','rb')
        bot.send_sticker(message.chat.id, sti4)
        bot.send_message(message.chat.id,'Козерошки.Вас ждет продуктивный  день')
    elif message.text =='Близнецы':
        sti5 = open('6023589773195610508.webp','rb')
        bot.send_sticker(message.chat.id, sti5)
        bot.send_message(message.chat.id,'Близняшки-смешнявки.Вас ждет неожиданный день')
    elif message.text =='Рак':
        sti6 = open('6023928302517880685.webp','rb')
        bot.send_sticker(message.chat.id, sti6)
        bot.send_message(message.chat.id,'Раки.Вас кто-то ждет')
    elif message.text =='Водолей':
        sti7 = open('6021453057030622015.webp','rb')
        bot.send_sticker(message.chat.id, sti7)
        bot.send_message(message.chat.id,'Водолеи.Совет: будьте внимательными')
    elif message.text =='Лев':
        sti8 = open('6023963564199380586.webp','rb')
        bot.send_sticker(message.chat.id, sti8)
        bot.send_message(message.chat.id,'Симбочки.Кто-то в тайне в вас влюблен')
    elif message.text =='Весы':
        sti9 = open('6023928302517880685.webp','rb')
        bot.send_sticker(message.chat.id, sti9)
        bot.send_message(message.chat.id,'Весочки.У вас сегодня улётный день')
    elif message.text =='Скорпион':
        bot.send_message(message.chat.id,'Скорпиончики.На работе лучше сегодня не врать,а то не повысят')
    elif message.text =='Телец':
        bot.send_message(message.chat.id,'Тельцы.Если вы домосед, ВЫХОДИТЕ ГУЛЯТЬ')
    elif message.text =='Дева':
        bot.send_message(message.chat.id,'Девочки, ой то есть девы. Посветите день музыке, вам очень понравится')
    elif message.text =='Овен':
        sti10 = open('6023928302517880685.webp','rb')
        bot.send_sticker(message.chat.id, sti10)
        bot.send_message(message.chat.id,'Овны.Сегодня классная погода, чтобы провести время с друзьями или близкими')
    elif message.text =='Стрелец':
        bot.send_message(message.chat.id,'Стрельцы.Не теряйте голову')  
        
def get_name(message):
    name =message.text
    bot.send_message(message.from_user.id,'Какое интересное имя '+name)
    sti2 = open('2124661471689312785.webp','rb')
    bot.send_sticker(message.chat.id, sti2)
    bot.send_message(message.from_user.id,'И так '+ name + '.')    

    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton("Погадаем", callback_data="yes")
    keyboard.add(yes)
    no = types.InlineKeyboardButton("Прогноз", callback_data="no")
    keyboard.add(no)

    question = 'Погадаем? Или хотите узнать прогноз?'

    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)




@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    world = ['Все будет хорошо','Вас ждёт хорошее событие','Смотрите под ноги,может вы найдёте клад','Вы обязаны загадать желание, сегодня волшебный день','Как говорил Ницше:"Вы самые лучшие"','Сегодня продуктивный день','В вас кто-то влюблен','Коротко о вас: "Вы супер!"','Кайфуйте, жизнь одна','Обнимайтесь чаще',]
    if call.data == "yes":

        bot.send_message(call.message.chat.id,"Так...\nСекунду...")
        zz = types.ReplyKeyboardMarkup()
        z1 = types.KeyboardButton('Рыбы')
        z2 = types.KeyboardButton('Козерог')
        z3 = types.KeyboardButton('Близнецы')
        z4 = types.KeyboardButton('Рак')
        z5 = types.KeyboardButton('Водолей')
        z6 = types.KeyboardButton('Лев')
        z7 = types.KeyboardButton('Весы')
        z8 = types.KeyboardButton('Скорпион')
        z9 = types.KeyboardButton('Телец')
        z10 = types.KeyboardButton('Дева')
        z11 = types.KeyboardButton('Овен')
        z12 = types.KeyboardButton('Стрелец')

        zz.add(z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12)
        bot.send_message(call.message.chat.id,'Выбери свой Знак Зодиака', reply_markup=zz)       
    elif call.data == "no":
        bot.send_message(call.message.chat.id,"Ваш рандомный прогноз\nТак...так...так")
        bot.send_message(call.message.chat.id,random.choice(world))



bot.infinity_polling(interval = 0)