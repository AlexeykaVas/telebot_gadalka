import telebot
from telebot import types
import random

bot = telebot.TeleBot("5950728038:AAHC-5Nz5HlaIfX53ZFcw0bXgZv6puUgDQc")
sp_n = []
sp = []



def plus(a):
    bot.send_message(a, text="Please write the word you want to add.")
    @bot.message_handler(content_types=['text'])
    def in_plus(message):
        qqqq = message.text
        aaa1 = sp_n.index(message.from_user.id)
        if qqqq.isdigit() == True:
            sp[aaa1].pop(int(message.text)-1)
            if len(sp[aaa1]) == 0:
                markup = types.InlineKeyboardMarkup()
                btn1 = types.InlineKeyboardButton('Add word', callback_data='1')
                markup.add(btn1)
                bot.send_message(message.chat.id, text="There are no words", reply_markup=markup)
            else:
                aqqq = ''
                for i in range(0, len(sp[aaa1]), 1):
                    aqqq = aqqq + str(i+1) + '. ' + str(sp[aaa1][i]) + "\n"
                markup = types.InlineKeyboardMarkup()
                btn2 = types.InlineKeyboardButton('Random word', callback_data='2')
                markup.add(btn1, btn2)
                bot.send_message(message.chat.id, text=aqqq, reply_markup=markup)

        else:
            sp[aaa1].append(message.text)
            markup = types.InlineKeyboardMarkup()
            btn2 = types.InlineKeyboardButton('Random word', callback_data='2')
            markup.add(btn2)
            bot.send_message(message.chat.id, text="Word added ✅", reply_markup=markup)
        return ""
    return ""















@bot.message_handler(commands=['start'])
def start(message):
    telegram_user = message.from_user
    user_id = message.from_user.id
    print(user_id)
    sp.append([])
    sp_n.append(user_id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Add word', callback_data='1')
    btn2 = types.InlineKeyboardButton('Random word', callback_data='2')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text=f"Hello, {message.from_user.first_name}! It's Гадалка! There are commands:\n/add - Add word\n/random_word - show random word\n/all_list - show all words\n/delete - Delete word\n/help - Show all commands", reply_markup=markup)

@bot.message_handler(commands=['add'])
plus(message.chat.id)

