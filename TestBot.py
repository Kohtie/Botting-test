import telebot
telebot.apihelper.proxy = {'https':'https://138.197.5.192:8888'}

bot = telebot.TeleBot('1036419164:AAHV0bQkmvJct5YLXHB7LM7sTA6VVK6GmIE')

@bot.message_handler(content_types=['start'])

def start_message(message):
    bot.send_message(message.from_user.id, "HELLO BEAUTIFUL")

bot.polling(none_stop=True)