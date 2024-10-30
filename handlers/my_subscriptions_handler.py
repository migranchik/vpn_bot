from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from bot import bot
from adapters import tariff_db_adapter, subscription_db_adapter

from keyboards import start_keyboard, my_subscriptions_keyboard

router_my_subscriptions = Router()
tariff_db = tariff_db_adapter.TariffDB()
subscription_db = subscription_db_adapter.SubscriptionDB()


@router_my_subscriptions.callback_query(F.data.startswith('my_subscriptions'))
async def get_my_subscriptions(callback: CallbackQuery):
    end_times = [subscription_db.get_user_subscription(callback.from_user.id)]
    if end_times[0] is not None:
        await callback.message.edit_text(f'✅ Подписка активна до {end_times[0].strftime("%d.%m.%Y")}',
                                         reply_markup=my_subscriptions_keyboard.get_subscriptions_menu(end_times))
        await callback.answer()
    else:
        await callback.answer('У вас пока нет подключенного VPN')


@router_my_subscriptions.callback_query(F.data.startswith('get_my_vpn_'))
async def get_my_vpn(callback: CallbackQuery):
    end_times = [subscription_db.get_user_subscription(callback.from_user.id)]
    vpn_key = subscription_db.get_user_vpn_key(callback.from_user.id)
    await callback.message.edit_text(f'✅ Подписка активна до {end_times[0].strftime("%d.%m.%Y")}\n\n'
                                     f'Ваш ключ: `{vpn_key}`',
                                     reply_markup=my_subscriptions_keyboard.get_connect_vpn_menu(vpn_key),
                                     parse_mode='Markdown')

    await callback.answer()


@router_my_subscriptions.callback_query(F.data.startswith('manual'))
async def get_manual(callback: CallbackQuery):
    await bot.copy_message(callback.message.chat.id, 7047174818, 51)

    await callback.answer()


# Back buttons handler
@router_my_subscriptions.callback_query(F.data.startswith('back_to_menu_from_my_subscriptions'))
async def back_to_menu_from_my_subscriptions(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=start_keyboard.menu_kb)

    await callback.answer()


@router_my_subscriptions.callback_query(F.data.startswith('back_to_menu_from_get_vpn'))
async def back_to_menu_from_my_subscriptions(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=start_keyboard.menu_kb)

    await callback.answer()
