import asyncio
import logging
from datetime import date

from bot import bot
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from utils.outline_manager import client

from adapters import subscription_db_adapter

from handlers import (start_handler,
                      trial_handler,
                      buy_vpn_handler,
                      pay_vpn_handler,
                      my_subscriptions_handler)
logging.basicConfig(level=logging.INFO)


subscription_db = subscription_db_adapter.SubscriptionDB()

TIME_IN_DAY = 86400


# Запуск бота
async def main():

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start_handler.router_start)
    dp.include_router(trial_handler.router_trial)
    dp.include_router(buy_vpn_handler.router_buy_vpn)
    dp.include_router(pay_vpn_handler.router_pay_vpn)
    dp.include_router(my_subscriptions_handler.router_my_subscriptions)


    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)

    loop = asyncio.get_event_loop()
    loop.create_task(check_subscriptions())

    await dp.start_polling(bot)


async def delete_user(user_id):
    subscription_db.delete_user(user_id)
    client.delete_key(key_id=f'{user_id}')
    print('deleted')


async def check_subscriptions():
    while True:
        subscriptions = subscription_db.get_all()
        today_date = date.today()
        for subscription in subscriptions:
            print(subscription)
            if subscription[2] == today_date:
                try:
                    await delete_user(subscription[1])
                except Exception as e:
                    print('Ошибка во время удаления')
        await asyncio.sleep(TIME_IN_DAY) # 86400


if __name__ == "__main__":
    asyncio.run(main())
