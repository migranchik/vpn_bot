from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

get_trial_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Подписаться 📰', url='https://t.me/ClevVPN')],
        [InlineKeyboardButton(text='🔐 Подключить VPN', callback_data='get_trial')]
    ]
)
