import logging, os
from telegram import *
from telegram.ext import *
from readwise import ReadWise
from datetime import datetime
import markdown
import markdownify
from functools import wraps
from dotenv import load_dotenv

load_dotenv()

#get bot token from env
BOT_TOKEN = os.getenv('BOT_TOKEN')
# initialize class for Readwise api
WISE = ReadWise(os.getenv('READWISE_TOKEN'))
# restrict access to our bot to avoid spam
ADMIN = os.getenv('ADMIN_USER')

logging.FileHandler("info_telewise_bot.txt", mode='a', encoding=None, delay=False)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

SEND_TO_READWISE = range(1)

def get_html(text_html: str) -> str:
    markdown_from_html = markdownify.markdownify(text_html)
    return markdown.markdown(markdown_from_html)

def restricted(func):
    @wraps(func)
    async def wrapped(update: Update, context, *args, **kwargs):
        username = update.effective_user.username
        if username != ADMIN:
            error_message = f"Unauthorized access denied for {username}."
            await context.bot.send_message(chat_id=update.effective_chat.id, text=error_message)
            logging.warning(error_message)
            return
        return await func(update, context, *args, **kwargs)
    return wrapped
    

@restricted
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Bot for integration with ReadWise api and Telegram. Forward me posts and I will send them to your ReadWise. For more go to https://github.com/uchr/readwise_telegram_bot")

@restricted
async def send_to_reader(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Prepare text for Readwise")

    # link for the telegram post
    telegram_link = "https://t.me/" + str(update.message.forward_from_chat.username) + "/" + str(update.message.forward_from_message_id)

    # if the message contains only text, it will have text_html property, but if the message contains media the text of the message would be in the caption_html property    
    text = get_html(update.message.text_html_urled) if update.message.caption_html_urled is None else get_html(update.message.caption_html_urled)

    title = str(update.message.forward_from_chat.username) + " " + str(datetime.now().isoformat())

    WISE.check_token()
    #send post as Readwise highlight
    WISE.save(url=telegram_link,
        html=text,
        title = title,
        summary = text[:128])
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{title} was sent to Readwise")
    return ConversationHandler.END

@restricted
async def cancel(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Oops...")
    return ConversationHandler.END

if __name__ == '__main__':
    #start app
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    #register commands
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler((filters.TEXT | filters.ATTACHMENT | filters.PHOTO) & ~filters.COMMAND & filters.FORWARDED, send_to_reader))
    
    #run bot
    application.run_polling()
