import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# /start විධානයට උත්තර දෙන විදිහ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("හායි! මම ඔබේ අලුත් ටෙලිග්‍රෑම් බොට් එක.")

if __name__ == '__main__':
    # BotFatherගෙන් ගත් Token එක මෙතැනට දාන්න
    TOKEN = "8650700541:AAGZX9o1XVg8libgKEinJvGoRz3qEitdH5Y"
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("Bot එක වැඩ කරන්න පටන් ගත්තා...")
    app.run_polling()
