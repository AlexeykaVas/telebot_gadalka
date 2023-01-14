import telebot
import time
bot = telebot.TeleBot("5950728038:AAHC-5Nz5HlaIfX53ZFcw0bXgZv6puUgDQc")

@bot.message_handler(commands=['start'])
def start(message):
    i = 0
    a = '996511543'
    bot.send_message(a, text=f'Приветик, {message.from_user.first_name}!\nЭто спам бот!')
    while i != 23:
        i+=1  
        if i % 11 == 0:
            time.sleep(0.3)
        bot.send_message(a, text=f'Это {i} сообщение')
        

bot.infinity_polling()