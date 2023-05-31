import asyncio
from decimal import Decimal

from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from config import CONFIG
from loader import dp, bot
from states.users.userState import UserStates


@dp.message_handler(commands=["start"])
async def registration_start(message: types.Message):
    await message.delete()
    for i in range(10):
        await asyncio.sleep(int(CONFIG.PING))  # Задержка в 5 секунд
        await message.answer(f'Сообщение {i + 1}')


@dp.message_handler(commands=["admin"])
async def registration_start(message: types.Message):
    await message.answer(text='Введите секунд задержки:')
    await UserStates.Ping.set()


@dp.message_handler(state=UserStates.Ping)
async def process_number(message: types.Message, state: FSMContext):
    try:
        CONFIG.PING = Decimal(message.text)
        await state.finish()
    except ValueError:
        await message.answer("Ошибка ввода. Пожалуйста, введите корректное число.")
        return
