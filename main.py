from bot_command import *
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = ApplicationBuilder().token("5753137996:AAGldncFpLpHhmqYBK7vA1CGH5giTjgxhcs").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("eval", eval_command))

print('server start')
app.run_polling()