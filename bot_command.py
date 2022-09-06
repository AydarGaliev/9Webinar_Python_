from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from log import *

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}!')

async def eval_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    msg = update.message.text
    items = msg.split()
    msg = str(items[1])
    exp=eval(msg)
    log(update, context, exp)
    await update.message.reply_text(f'{msg}={exp}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Доступные команды и их написание:\n/hello\n/eval 10+20\n/help')