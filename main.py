import telebot as tb
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def link():
    global new_message
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
            InlineKeyboardButton("Github", url="https://github.com/AndreBezer"),
            InlineKeyboardButton("Instagram", url="https://www.instagram.com/andrelbrj_?igsh=MTZndDBpd296NTJueQ=="),
            InlineKeyboardButton("LinkedIn", url="https://www.linkedin.com/in/andr%C3%A9-luis-219009353?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
    )
    return markup

chave = "_Your_Key_here_"
bot = tb.TeleBot(chave)

@bot.message_handler(commands=["start"])
def responder_start(mensagem):
    bot.send_message(mensagem.chat.id, "link das redes sociais:", reply_markup=link())

bot.infinity_polling()
