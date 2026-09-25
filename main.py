import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# /start විධානයට උත්තර දෙන විදිහ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("හායි! මම ඔබේ අලුත් ටෙලිග්‍රෑම් බොට් එක.")

def main():
    # BotFatherගෙන් ගත් Token එක මෙතැනට දාන්න
    TOKEN = "8650700541:AAGZX9o1XVg8libgKEinJvGoRz3qEitdH5Y"
    
    # Render එක දෙන Port එක ලබා ගැනීම (Web Service එකක් ලෙස ක්‍රියාත්මක වීමට)
    PORT = int(os.environ.get("PORT", "8443"))
    
    # Render එකේ දෙන ඔබේ App එකේ වෙබ් ලිපිනය (Render එකෙන් ලැබෙන URL එක මෙතැනට දමන්න, නැත්නම් පස්සේ දාන්න පුළුවන්)
    # උදාහරණයක් ලෙස: https://your-app-name.onrender.com
    RENDER_EXTERNAL_URL = os.environ.get("RENDER_EXTERNAL_URL")

    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
    if RENDER_EXTERNAL_URL:
        # Webhook හරහා ක්‍රියාත්මක වීම (Render එකට අවශ්‍ය වේ)
        WEBHOOK_URL = f"{RENDER_EXTERNAL_URL}/{TOKEN}"
        print(f"Starting webhook on port {PORT} with URL {WEBHOOK_URL}")
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
            webhook_url=WEBHOOK_URL
        )
    else:
        # ලෝකල් ෆෝන් එකේ හෝ වෙනත් තැනක ටෙස්ට් කිරීමට
        print("Starting polling...")
        app.run_polling()

if __name__ == '__main__':
    main()
