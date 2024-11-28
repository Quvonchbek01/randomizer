import telebot
from random import randint
bot = telebot.TeleBot("7706266393:AAFVvOZ1hSvpFKYdZT2_OW5IPwSOHTD7hhk")
@bot.message_handler(commands=['start', 'help'])
def command(message):
    username = message.from_user.first_name
    bot.reply_to(
        message,
        f"Assalomu alaykum {username}, tasodifiy son tanlash uchun ma'lum bir oraliqni tanlang!\n"
        "Misol uchun: 1-100"
    )
@bot.message_handler(func=lambda m: True)
def random_number(message):
    try:
        z = message.text.split("-")
        if len(z) != 2:
            bot.send_message(message.chat.id, "Iltimos, oraliqni to'g'ri formatda kiriting. Masalan: 1-100.")
            return
        start = int(z[0].strip())
        end = int(z[1].strip())
        random_num = randint(start, end)
        bot.send_message(message.chat.id, f"Tasodifiy son: {random_num}")
        
    except ValueError:
        bot.send_message(message.chat.id, "1-son 2-sondan katta, iltimos to'g'ri formatda kiriting. Masalan: 1-100.")
    except IndexError:
        bot.send_message(message.chat.id, "Iltimos, oraliqni to'g'ri formatda kiriting. Masalan: 1-100.")

bot.polling()
