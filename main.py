from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logger as lg


print("Бот запущен. Нажмите Ctrl+C для завершения")

def on_start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Привет, я Бот Калькулятор!")

def on_message(update, context):
	chat = update.effective_chat
	text = update.message.text
	try:
		context.bot.send_message(chat_id=chat.id, text="Результат:" + str(eval(text)))
	except:
		context.bot.send_message(chat_id=chat.id, text="Напишите числа для выполения операции, и знак. Пример: 2+5")
lg.info("Compute: {on_message.update.message.text} = {on_message.text}")        
        
token = "5773814946:AAFwEieDns-hR_Z2Qz89_pMKU99FcwZ5glE"

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()