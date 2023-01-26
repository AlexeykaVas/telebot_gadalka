import requests
import telebot
import secrets
bot = telebot.TeleBot(secrets.TOKEN)


    
@bot.message_handler(content_types=['text'])
def start(message):
    url = 'http://'+message.text
    r = requests.get(url, params={"key_1": "value_1", "key_N": "value_N"}, verify=False).text
    f = open('index.html', 'w').write(r)
    markdown = '```'+r+'```'
    bot.send_message(message.chat.id, markdown, parse_mode="Markdown")
    bot.send_document(message.chat.id, open(r'index.html', 'rb'))

bot.infinity_polling()