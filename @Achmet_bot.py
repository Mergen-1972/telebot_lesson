import telebot
TOKEN = "6130684311:AAGMwRmhkeTuTfp46OyPy4Mnc_CmOX6HGDo"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):

    if message.text =="/start":
        bot.send_message(message.from_user.id,"lets go")
    elif message.text =="/help":
        bot.send_message(message.from_user.id, "can i help yuo?")


bot.polling(none_stop=True, interval=0)