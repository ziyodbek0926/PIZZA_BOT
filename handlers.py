import json
from telegram import Update , InlineKeyboardMarkup
from telegram.ext import CallbackContext
from bot import USER_DATA  
from admin import ADMIN_CHAT_ID

def load_pizza_data():
    with open('pizza_data.json', 'r') as f:
        return json.load(f)

PIZZA_DATA = load_pizza_data()


def load_user_data():
    try:
        with open('user_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_user_data(data):
    with open('user_data.json', 'w') as f:
        json.dump(data, f, indent=4)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Pizza botimizga xush kelibsiz, bu botda siz mazzali pizzalarga buyurtma bera olasiz.')

def menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.edit_message_text('Menyu:', reply_markup=InlineKeyboardMarkup([]))

def pizza_info(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    pizza = PIZZA_DATA[query.data]
    query.message.reply_photo(photo=open(pizza['image'], 'rb'), caption=f"{pizza['name']}\n{pizza['description']}")

def about(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.edit_message_text('Biz haqimizda:\n\nManzilimiz:\nBiz bilan bog\'lanish uchun:\nLocation:')


def order(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    pizza_key, quantity = query.data.split('_')
    pizza = PIZZA_DATA[pizza_key]
    order_info = f"Buyurtma: {pizza['name']} - {quantity} dona"

    context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"Yangi buyurtma:\n{order_info}")

    query.edit_message_text(f"Siz {pizza['name']} - {quantity} dona buyurtma qildingiz.")

def request_phone(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Iltimos, buyurtma berish uchun telefon raqamingizni ulashing:")

def handle_contact(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    phone_number = update.message.contact.phone_number
    USER_DATA[user.id] = {
        'name': user.full_name,
        'phone_number': phone_number,
        'orders': []
    }
    save_user_data(USER_DATA)
    update.message.reply_text("Rahmat, endi buyurtma berishingiz mumkin.")

def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == 'menu':
        menu(update, context)
    elif query.data == 'feedback':
        query.edit_message_text('Izoh qoldirish uchun hozircha imkoniyat yo\'q.')
    elif query.data == 'about':
        about(update, context)
    elif query.data in PIZZA_DATA:
        pizza_info(update, context)
    elif query.data == 'start':
        start(update, context)
    elif '_' in query.data:
        order(update, context)
