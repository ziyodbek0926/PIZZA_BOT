from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_buttons():
    buttons = [
        [InlineKeyboardButton("Menyu", callback_data='menu')],
        [InlineKeyboardButton("Izoh qoldirish", callback_data='feedback')],
        [InlineKeyboardButton("Biz haqimizda", callback_data='about')]
    ]
    return InlineKeyboardMarkup(buttons)

def menu_buttons():
    buttons = [
        [InlineKeyboardButton("Pepperoni", callback_data='pepperoni')],
        [InlineKeyboardButton("Margarita", callback_data='margarita')],
        [InlineKeyboardButton("Bavarian", callback_data='bavarian')],
        [InlineKeyboardButton("Orqaga", callback_data='start')]
    ]
    return InlineKeyboardMarkup(buttons)

def pizza_order_buttons(pizza_key):
    buttons = [[InlineKeyboardButton(f"{i} dona", callback_data=f"{pizza_key}_{i}") for i in range(1, 8)]]
    buttons.append([InlineKeyboardButton("Asosiy menyuga qaytish", callback_data='start')])
    return InlineKeyboardMarkup(buttons)

def back_to_main_menu_button():
    buttons = [[InlineKeyboardButton("Asosiy menyuga qaytish", callback_data='start')]]
    return InlineKeyboardMarkup(buttons)
