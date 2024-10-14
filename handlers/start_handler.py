from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards import start_keyboard

router_start = Router()


@router_start.message(Command('check'))
async def choice_course(message: Message):
    await message.answer("Бот работает")


@router_start.message(Command('start'))
async def start_bot(message: Message, state: FSMContext):
    await message.delete()
    await message.answer("Привет!", reply_markup=start_keyboard.get_events_kb)
