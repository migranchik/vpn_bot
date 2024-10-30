from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_tariffs_kb(tariffs: list) -> InlineKeyboardMarkup:
    back_button = [InlineKeyboardButton(text='⬅️ Назад', callback_data='back_to_menu_from_buy_vpn')]
    vpn_buttons = [[InlineKeyboardButton(text=tariff[1], callback_data=f'choosed_{tariff[0]}_{tariff[2]}')] for tariff in tariffs]
    vpn_buttons.append(back_button)

    return InlineKeyboardMarkup(inline_keyboard=vpn_buttons)
