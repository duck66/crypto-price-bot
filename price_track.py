import requests
import telegram
import json

from telegram.ext import Updater
from telegram.ext import CommandHandler

telegram_bot_token = "THIS_IS_SECRET"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

def rego(update, context):
    chat_id = update.effective_chat.id

    base_url = "https://indodax.com/api/ticker"

    coin = f"{base_url}/{context.args[0]}idr"

    response = requests.get(coin)

    print(response.json())

    if response.json().get("ticker"):
        text = response.json().get("ticker").get("last")
        text = "{:0,}".format(float(text))
        text = f"Regone Rp {text} cok!"
    else:
        text = f"{context.args[0]} iku token apaan cok ?!"
    context.bot.send_message(chat_id=chat_id, text=f"{text}")

dispatcher.add_handler(CommandHandler("rego", rego))
updater.start_polling()
