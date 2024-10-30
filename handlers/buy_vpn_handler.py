from aiogram import Router, F
from aiogram.types import CallbackQuery

from adapters import tariff_db_adapter

from keyboards import start_keyboard, buy_vpn_keyboard

router_buy_vpn = Router()
tariff_db = tariff_db_adapter.TariffDB()


@router_buy_vpn.callback_query(F.data.startswith('buy_vpn'))
async def get_tariffs(callback: CallbackQuery):
    tariffs = tariff_db.get_tariffs()
    await callback.message.edit_reply_markup(reply_markup=buy_vpn_keyboard.get_tariffs_kb(tariffs))

    await callback.answer()


@router_buy_vpn.callback_query(F.data.startswith('back_to_menu_from_buy_vpn'))
async def back_to_menu_from_buy_vpn(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=start_keyboard.menu_kb)

    await callback.answer()