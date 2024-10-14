from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

get_events_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Посмотреть события', callback_data='choose_type')]])