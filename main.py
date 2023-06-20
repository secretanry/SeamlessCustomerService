import telebot

token = "AAFTgH9GYnOoUogisKj2d81xCi5o9xI2US4"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    pass


@bot.message_handler(commands=["button"])
def enter_onClick_listener(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    enter_button = telebot.types.KeyboardButton("I'm ready to answer questions!")
    markup.add(enter_button)
    bot.send_message(message.chat.id, "I'm ready to answer questions!")


@bot.message_handler(content_types=['text'])
def main_script(message):
    pass
