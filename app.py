import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Flask app (Railway keeps this alive)
app = Flask(__name__)

@app.route("/")
def home():
    return "Mapla AI Bot is Running 🔥"

# Telegram commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Vanakkam Mapla!\n\n"
        "Polymarket AI Bot is Online.\n"
        "Use /help to see available commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available Commands:\n"
        "/start - Start the bot\n"
        "/help - Show help"
    )

def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling()

# Start Telegram bot in background
threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
