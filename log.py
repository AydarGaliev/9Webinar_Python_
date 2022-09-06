from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def log(update: Update, context: ContextTypes.DEFAULT_TYPE, exp):
    file = open('log.csv','a', encoding='utf-8')
    file.write(f'{update.effective_user.first_name },{update.effective_user.id},{update.message.text},={exp}\n')
    file.close()