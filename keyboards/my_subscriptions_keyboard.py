from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.vpn_link_creator import create_vpn_link


def get_subscriptions_menu(end_times: list) -> InlineKeyboardMarkup:
    back_button = [InlineKeyboardButton(text='⬅️ Назад', callback_data='back_to_menu_from_my_subscriptions')]

    subscriptions_buttons = [[InlineKeyboardButton(text=f'Оплачен до {end_time.strftime("%d.%m.%Y")} ✅', callback_data=f'get_my_vpn_{end_time.strftime("%d.%m.%Y")}')]for end_time in end_times]
    subscriptions_buttons.append(back_button)

    return InlineKeyboardMarkup(inline_keyboard=subscriptions_buttons)


def get_connect_vpn_menu(vpn_key: str) -> InlineKeyboardMarkup:
    get_vpn_buttons = [
        [InlineKeyboardButton(text='ℹ️ Как подключить VPN?', callback_data='manual')],
        [InlineKeyboardButton(text='Активировать VPN ✅', url=create_vpn_link(vpn_key))],
        [InlineKeyboardButton(text='💳 Продлить VPN', callback_data='buy_vpn')],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='back_to_menu_from_get_vpn')]
    ]

    return InlineKeyboardMarkup(inline_keyboard=get_vpn_buttons)


