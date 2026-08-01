from telegram.ext import Application, CommandHandler
from config import BOT_TOKEN


async def start(update, context):
    await update.message.reply_text(
        "🎟️ سلام رفیق 😎\n\nربات KingK Ticket روشنه 🚀"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    print("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
