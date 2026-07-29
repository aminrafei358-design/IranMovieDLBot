from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8931750974:AAElU1mx9BNRoqBYFcuQzKNVqDrek5e9Xu0"

ADMIN_ID = 8182051742


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if user.id == ADMIN_ID:
        await update.message.reply_text(
            "👑 پنل ادمین فعال شد\nربات آماده است."
        )
    else:
        await update.message.reply_text(
            "سلام 👋\nبه ربات Iran Movie خوش آمدید."
        )


async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    await update.message.reply_text(
        "👑 پنل مدیریت\n\n"
        "📁 مدیریت فایل‌ها\n"
        "📢 مدیریت کانال‌ها\n"
        "👥 آمار کاربران\n"
        "⭐ مدیریت VIP"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("panel", panel))

    print("Bot Started")

    app.run_polling()


if __name__ == "__main__":
    main()
