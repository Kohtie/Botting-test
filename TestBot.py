import telebot
from telebot import types
import main_config
telebot.apihelper.proxy = main_config.API

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def first_message(message):
    #inline markup
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Books", callback_data="book")
    item2 = types.InlineKeyboardButton("Courses", callback_data="course")
    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "You're welcome, <b>{0.first_name}</b>! Push button to navigate in our menu".format(message.from_user),
                     parse_mode='html',
                     reply_markup= markup
                     )
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'book':
            bot.send_message(call.message.chat.id, 'BOOKS:')
        elif call.data == 'course':
            bot.send_message(call.message.chat.id, 'COURSES:')

bot.polling(none_stop=True)
