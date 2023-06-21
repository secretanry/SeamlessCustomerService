import telebot

token = "6095790820:AAFTgH9GYnOoUogisKj2d81xCi5o9xI2US4"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    enter_button = telebot.types.KeyboardButton("I'm ready to answer questions!")
    markup.add(enter_button)
    bot.send_message(message.chat.id, "Hello, what you want to do?", reply_markup=markup)


@bot.message_handler(commands=["button"])
def enter_onClick_listener(message):
    bot.send_message(message.chat.id, "I'm ready to answer questions!",
                     reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(func=lambda message: message == "I'm ready to answer questions!", content_types=["text"])
def main_script(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    exit_button = telebot.types.KeyboardButton("I want to make a pause")
    markup.add(exit_button)
    bot.send_message(message.chat.id, "Ok, thanks for your work, you can start!", reply_markup=markup)


bot.polling()
