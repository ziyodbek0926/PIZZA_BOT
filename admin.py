import json
from telegram import Update
from telegram.ext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from handlers import USER_DATA


ADMIN_CHAT_ID = "5338316566"

def order_history(update: Update, context: CallbackContext) -> None:
    orders_text = "Buyurtmalar tarixi:\n"
    for user_id, user_data in USER_DATA.items():
        orders_text += f"\nFoydalanuvchi: {user_data['name']}, Telefon raqami: {user_data['phone_number']}\nBuyurtmalar:\n"
        for order in user_data['orders']:
            orders_text += f"- {order['name']} - {order['quantity']} dona\n"
    update.message.reply_text(orders_text)

def modify_menu(update: Update, context: CallbackContext) -> None:
    buttons = [
        [InlineKeyboardButton("Yangi pitsa qo'shish", callback_data='add_pizza')],
        [InlineKeyboardButton("Pitsa o'chirish", callback_data='delete_pizza')],
        [InlineKeyboardButton("Pitsa nomini o'zgartirish", callback_data='rename_pizza')],
        [InlineKeyboardButton("Asosiy menyuga qaytish", callback_data='start')]
    ]
    update.message.reply_text('Menuni o\'zgartirish:', reply_markup=InlineKeyboardMarkup(buttons))

def promotions(update: Update, context: CallbackContext) -> None:
    buttons = [
        [InlineKeyboardButton("Aktsiyani o'zgartirish", callback_data='change_promotion')],
        [InlineKeyboardButton("Asosiy menyuga qaytish", callback_data='start')]
    ]
    update.message.reply_text('Aktsiyalarni boshqarish:', reply_markup=InlineKeyboardMarkup(buttons))

def add_pizza(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Yangi pitsa qo'shish funksiyasi hozircha qo'llab-quvvatlanmaydi.")

def delete_pizza(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Pitsa o'chirish funksiyasi hozircha qo'llab-quvvatlanmaydi.")


def rename_pizza(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Pitsa nomini o'zgartirish funksiyasi hozircha qo'llab-quvvatlanmaydi.")

def change_promotion(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Aktsiyani o'zgartirish funksiyasi hozircha qo'llab-quvvatlanmaydi.")
