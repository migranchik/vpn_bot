from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu_buttons = [[InlineKeyboardButton(text='🛒 Купить VPN', callback_data='buy_vpn')],
                [InlineKeyboardButton(text='📋 Мои VPN', callback_data='my_subscriptions')],
                [InlineKeyboardButton(text='🆘 Поддержка', url='https://t.me/lootally')]]

menu_kb = InlineKeyboardMarkup(inline_keyboard=menu_buttons)