import telegram
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# 1. Define the bot's token. 
#    !!! Replace 'YOUR_BOT_TOKEN_HERE' with your actual token !!!
BOT_TOKEN = '8223632445:AAEdSjRjU0v8TfxfmxacXSCalYRKqwWG_L0' # <--- REPLACE THIS LINE WITH YOUR TOKEN

# 2. Define the handler function for the /start command
async def start_command(update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message when the /start command is issued."""
    await update.message.reply_text('مرحباً! أنا بوتك الجديد.') # Hello! I am your new bot.

# 3. Define the main function to run the bot
def main(/):
    """Start the bot."""
    
    # Create the Application and pass it your bot's token.
    # The 'ApplicationBuilder()' approach is deprecated, use Application.builder()
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start_command))
    
    # Run the bot until the user presses Ctrl-C
    print("Bot is running...")
    application.run_polling(allowed_updates=telegram.constants.Update.ALL_TYPES)

# 4. Run the main function
if __name__ == '__main__':
    main()

