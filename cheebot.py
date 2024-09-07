# Version: 1.1 - Create by: StaryDarkz

from telegram.ext import Updater, CommandHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ChatAction
import functions
import time, threading

print ("Iniciando a CheeZBot....")
token = functions.config()
print ("\nCheeZBot ha sido iniciado...")
updater = Updater(token=token, use_context=True)
admins = ["@starydarkz"]

#Commandos generales
def start(update, context):
    ''' Saluda al bot'''
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Estoy despierto")

def quees(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    user_say = " ".join(context.args)
    answer = functions.definiciones(user_say)
    update.message.reply_text(answer)    

#Comandos de administracion
def addquestions(update, context):
    user_say = " ".join(context.args)
    functions.add_questions(user_say)
    update.message.reply_text("Question Saved")

def readquestions(update, context):
    questions = functions.read_questions()
    update.message.reply_text(questions)

isalive = [False, False] #primer= Parar proceso segundo = Evitar mas de un subproceso
def whiledayq(context, update, isalive):
    '''Complemento de preguntas random'''
    isalive[1] = True
    while isalive[0]:
        questions = functions.random_questions()
        context.bot.send_message(chat_id=update.effective_chat.id, text=questions)
        time.sleep(43200)

def randomquestions(update, context, isalive=isalive):
    '''Activa las preguntas random'''
    
    whiledayquestions = threading.Thread(target=whiledayq, args=(context, update, isalive))
    if isalive[1]:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Pregunta del dia esta: ON")
    else:
        isalive[0] = True
        whiledayquestions.start()

def offdayquestion(update, context, isalive=isalive):
    '''Desactiva la funcion de preguntas random'''
    
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    isalive[0] = False
    isalive[1] = False
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pregunta del dia desactivado")

#Comandos publicos
start_handler = CommandHandler('start', start,)
quees_handler = CommandHandler('quees', quees, pass_args=True)

#Comandos de administracion
addq_handler = CommandHandler('addq', addquestions, Filters.user(username=admins), pass_args=True)
readq_handler = CommandHandler('readq', readquestions, Filters.user(username=admins))
random_handler = CommandHandler('randomq', randomquestions, Filters.user(username=admins))
offdayq_handler = CommandHandler('offrandomq', offdayquestion, Filters.user(username=admins))


updater.dispatcher.add_handler(addq_handler)
updater.dispatcher.add_handler(readq_handler)
updater.dispatcher.add_handler(quees_handler)
updater.dispatcher.add_handler(random_handler)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(offdayq_handler)

updater.start_polling()
