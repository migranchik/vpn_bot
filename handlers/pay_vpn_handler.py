from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import configparser

from yookassa import Configuration, Payment
from utils.outline_manager import client

from adapters import tariff_db_adapter, subscription_db_adapter
from utils import create_yookassa_payload, add_to_date
from keyboards import pay_vpn_keyboard

router_pay_vpn = Router()
tariff_db = tariff_db_adapter.TariffDB()
subscription_db = subscription_db_adapter.SubscriptionDB()

config = configparser.ConfigParser()
config.read('config.ini')

card_shop_id = config["Yookassa"]["cardshopid"]
token = config["Yookassa"]["token"]

VPN_NAME = 'ClevVPN'

# TODO Configuration.account_id = card_shop_id
# TODO Configuration.secret_key = token


@router_pay_vpn.callback_query(F.data.startswith('choosed_'))
async def create_payment(callback: CallbackQuery, state: FSMContext):
    # data = callback.data.split('_')
    #
    # tariff_id = data[1]
    # tariff_cost = int(data[2])
    # tariff_name = tariff_db.get_one_tariff(tariff_id)[1]
    #
    # # TODO payment = create_yookassa_payload.create_yookassa_payload(tariff_cost, tariff_name)
    #
    # await state.update_data(tariff_id=tariff_id)
    #
    # await callback.message.answer(f'{tariff_name}\n\n'
    #                               f'Никто кроме банка и интернет-эквайринга не имеет доступа к вашим банковским данным',
    #                               reply_markup=pay_vpn_keyboard.get_pay_kb('https://google.com',
    #                                                                        'payment')
    #                               )

    await callback.answer('Платная подписка пока недоступна!')


@router_pay_vpn.callback_query(F.data.startswith('check_payment'))
async def check_pay(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    payment_id = callback.data.split('_')[2]
    tariff_id = data['tariff_id']

    print(payment_id)
    # TODO payment = Payment.find_one(payment_id)
    paid = True # TODO payment.paid

    if paid:
        tariff = tariff_db.get_one_tariff(tariff_id)
        print(tariff)

        await callback.message.answer(
            f'Оплата успешно прошла!\n'
            f'Узнайте как начать им пользоваться в разделе "Мои VPN"\n\n',
            parse_mode="HTML")

        exist_subscription = subscription_db.get_user_subscription(callback.from_user.id)
        print(exist_subscription)
        if exist_subscription is not None:

            end_time = add_to_date.add_month_to_date(tariff[3], exist_subscription)
            subscription_db.extend_subscription(callback.from_user.id, end_time)
        else:
            vpn_key = client.create_key(
                key_id=f'{callback.from_user.id}',
                name=f'{callback.from_user.username}',
            )

            end_time = add_to_date.add_month_to_date(tariff[3])
            subscription_db.add_subscription(callback.from_user.id, end_time, f'{vpn_key.access_url}#{VPN_NAME}')

        await callback.message.delete()
        await callback.answer()
    else:
        await callback.answer('Вы не оплатили!', show_alert=True)
