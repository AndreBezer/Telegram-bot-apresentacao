import telebot as tb
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Cria os botões para minhas redes sociais
def redes_sociais():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1 # Quantidade de botões por linha 
    markup.add(
            InlineKeyboardButton("Github", url="https://github.com/AndreBezer"),
            InlineKeyboardButton("Instagram", url="https://www.instagram.com/andrelbrj_?igsh=MTZndDBpd296NTJueQ=="),
            InlineKeyboardButton("LinkedIn", url="https://www.linkedin.com/in/andr%C3%A9-luis-219009353?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
    )
    return markup

# Comandos disponiveis em resposta ao /start
def comandos_disponiveis():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
            InlineKeyboardButton("Redes sociais", callback_data="redes_sociais"),
			InlineKeyboardButton("Sobre mim", callback_data="sobre_mim")
    )
    return markup

# Configuração do bot
chave = "_Your_Key_Here_"
bot = tb.TeleBot(chave)

# Comando basico
@bot.message_handler(commands=["start"])
def responder_start(mensagem):
	with open("fotos/foto_andre.jpg", "rb") as foto:
		bot.send_photo(mensagem.chat.id, foto, caption=None)

	bot.send_message(mensagem.chat.id, "Seja bem vindo(a) ao Bot de AndreBezer!")
	bot.send_message(mensagem.chat.id, "Sinta-se a vontade para testar o ChatBot")
	bot.send_message(mensagem.chat.id, "Commandos disponiveis:", reply_markup=comandos_disponiveis())

# Handler para callbacks
@bot.callback_query_handler(func=lambda call:True)
def callback_handler(call):
	if call.data == "redes_sociais":
		bot.send_message(call.message.chat.id, "Minhas redes sociais:", reply_markup=redes_sociais())
	
	if call.data == "sobre_mim":
		bot.send_message(call.message.chat.id, "Sobre mim:")
		bot.send_message(call.message.chat.id, "Estou estudando Analise e Desenvolvimento de Software na faculdade")
		bot.send_message(call.message.chat.id, "Trabalhei como Ajudante de Operador de maquinas em uma fabrica por 8 meses")
		bot.send_message(call.message.chat.id, "busco oportunidade de trabalho como Desenvolvedor.")
		bot.send_message(call.message.chat.id, "Conhecimentos na linguagem de prgogramação Python")

bot.infinity_polling()
