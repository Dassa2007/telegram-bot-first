import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from aiohttp import web

# /start විධානයට උත්තර දෙන විදිහ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("හායි! මම ඔබේ අලුත් ටෙලිග්‍රෑම් බොට් එක.")

# Render එකෙන් සර්වර් එක ඔන් කරලා තබා ගැනීමට සරල වෙබ් පිටුවක්
async def handle(request):
    return web.Response(text="Bot is running!")

async def web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render එක දෙන Port එක පාවිච්චි කරයි
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

if __name__ == '__main__':
    TOKEN = "8650700541:AAGZX9o1XVg8libgKEinJvGoRz3qEitdH5Y"
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(web_server())
    
    print("Bot එක වැඩ කරන්න පටන් ගත්තා...")
    app.run_polling()
