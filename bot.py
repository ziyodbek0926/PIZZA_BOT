from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from handlers import start, button_handler, handle_contact, request_phone, load_user_data, save_user_data
from admin import admin_commands


import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


USER_DATA = load_user_data()

def save_user_data_periodically():
    save_user_data(USER_DATA)
    logger.info("User data saved successfully.")

def main():
    
    token = '6377726298:AAEIgQi6_TYu9pnXEvvxuf9c4rEZkZlEbkQ'

    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, handle_contact))

    admin_commands(dispatcher)


    updater.start_polling()

    updater.job_queue.run_repeating(save_user_data_periodically, interval=900)  

    updater.idle()

if __name__ == '__main__':
    main()
