from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot import bot
from adapters import user_db_adapter, subscription_db_adapter

from utils.outline_manager import client
from utils import add_to_date

router_trial = Router()
user_db_adapter = user_db_adapter.UserDB()
subscription_db = subscription_db_adapter.SubscriptionDB()
TIME_FOR_TRIAL = 3 # days
VPN_NAME = 'ClevVPN'


async def check_subscription(user_id):
    member = await bot.get_chat_member('@ClevVPN', user_id)
    return member.status in ['member', 'administrator', 'creator']


@router_trial.callback_query(F.data.startswith('get_trial'))
async def get_trial(callback: CallbackQuery):
    member_check = await check_subscription(callback.from_user.id)
    if member_check:
        trial_end_date = add_to_date.add_day_to_date(TIME_FOR_TRIAL)
        formatted_date = trial_end_date.strftime('%d.%m.%Y')

        vpn_key = client.create_key(
            key_id=f'{callback.from_user.id}',
            name=f'{callback.from_user.username}',
        )

        subscription_db.add_subscription(callback.from_user.id, trial_end_date, f'{vpn_key.access_url}#{VPN_NAME}')

        await callback.message.edit_text(f'✅ <b>Вы подключили пробный период до {formatted_date}</b>.\n\n'
                                         f'Узнайте как подключить к устройству в разделе "📋 Мои VPN"', parse_mode="HTML")

        await callback.answer()
    else:
        await callback.answer('Вы не подписались!')
