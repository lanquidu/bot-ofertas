import logging
from telegram.ext import Updater, CommandHandler
import requests

TOKEN = "8579750338:AAG6bf60oVWvu0dBskEJYsjog4WKT6C3DUo"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text("¡Bienvenido! A partir de ahora recibirás ofertas diarias automáticamente.")

def oferta(update, context):
    update.message.reply_text("Procesando mejores ofertas de Amazon...")

    # EJEMPLO – aquí luego pondremos productos reales
    update.message.reply_text(
        "🔥 Oferta Amazon:\n"
        "Echo Dot 5ta Gen\n"
        "Antes: $49.99\n"
        "Ahora: $22.99\n"
        "👉 https://www.amazon.com/dp/B09B8V9W1V?tag=TU_TAG"
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("oferta", oferta))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
