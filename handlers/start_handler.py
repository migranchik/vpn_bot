from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from adapters import user_db_adapter

from keyboards import start_keyboard, trial_keyboard

router_start = Router()
user_db_adapter = user_db_adapter.UserDB()


@router_start.message(Command('check'))
async def choice_course(message: Message):
    await message.answer("Бот работает")


@router_start.message(Command('start'))
async def start_bot(message: Message):
    await message.delete()
    try:
        user_db_adapter.create_user(message.from_user.id, message.from_user.username)
        await message.answer('Вы успешно зарегистрированы. Вам доступен пробный период на 3 дня\n\n'
                             'Для подключения подпишитесь на наш канал:',
                             reply_markup=trial_keyboard.get_trial_kb)
    except Exception as e:
        print("Такой пользователь существует", e)
    finally:
        await message.answer('<b>Ваша учетная запись активна.</b>'
                             '\n'
                             '\n'
                             '<i>Воспользуйтесь меню ниже:</i>',
                             reply_markup=start_keyboard.menu_kb,
                             parse_mode="HTML")


@router_start.message(F.video)
async def get_video_id(message: Message):
    print(message.chat.id)
    print(message.message_id)


