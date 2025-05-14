from flask import Flask, request
import telegram

TOKEN = "8031738383:AAE3zxHvhSFhbTESh0dxEPaoODCrPnuOIxw"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message = update.message.text

    # Пример ответа от бота
    bot.send_message(chat_id=chat_id, text="Сигнальный бот активен!")

    return "ok"

@app.route("/")
def index():
    return "Bot is alive!"

if __name__ == "__main__":
    app.run(port=5000)
