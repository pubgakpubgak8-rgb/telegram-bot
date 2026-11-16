# Telegram bot - bot.1.py
# 1) BotFather'dan olgan tokeningizni TOKEN qatoriga yozing.
# 2) Terminalda: pip install python-telegram-bot
# 3) Ishga tushirish: python bot.1.py

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "BOT_TOKENINGIZNI_SHU_YERGA_QOYING"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! Men sizning Telegram botingizman. 😊\n"
        "Menga xabar yuboring — javob beraman."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Buyruqlar:\n"
        "/start - botni boshlash\n"
        "/help - yordam"
    )


async def reply_to_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Xabaringiz qabul qilindi: {update.message.text}"
    )


def main():
    if TOKEN == "BOT_TOKENINGIZNI_SHU_YERGA_QOYING":
        raise SystemExit(
            "Avval bot.1.py ichidagi TOKEN qatoriga BotFather tokenini yozing."
        )

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_to_text))

    print("Bot ishga tushdi. To'xtatish uchun Ctrl+C bosing.")
    app.run_polling()


if __name__ == "__main__":
    main()
