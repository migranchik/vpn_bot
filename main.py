import configparser
import asyncio
import logging
from datetime import date

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import start_handler
logging.basicConfig(level=logging.INFO)

config = configparser.ConfigParser()
config.read('config.ini')

token = config["Bot"]["token"]

bot = Bot(token=token)


# Запуск бота
async def main():

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start_handler.router_start)



    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
