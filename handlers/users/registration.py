import asyncio
from decimal import Decimal

from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from config import CONFIG
from loader import dp, bot
from states.users.userState import UserStates


@dp.message_handler(commands=["start"], state=UserStates.all_states)
async def registration_start_two(message: types.Message):
    await message.delete()
    await message.answer(f'Отмена')


@dp.message_handler(commands=["start"])
async def registration_start(message: types.Message):
    await message.delete()
    await asyncio.sleep(int(CONFIG.PING))
    await message.answer(f'Сообщение 1')
    for i in range(1, 10):
        await asyncio.sleep(int(CONFIG.PINGTWO))  # Задержка в 5 секунд
        await message.answer(f'Сообщение {i + 1}')


@dp.message_handler(commands=["1"])
async def registration_start(message: types.Message):
    await message.answer(text='Введите секунд задержки Для первого сообщения:')
    await UserStates.Ping.set()


@dp.message_handler(state=UserStates.Ping)
async def process_number(message: types.Message, state: FSMContext):
    try:
        CONFIG.PING = Decimal(message.text)
        await state.finish()
    except ValueError:
        await message.answer("Ошибка ввода. Пожалуйста, введите корректное число.")
        return


@dp.message_handler(commands=["2"])
async def registration_start(message: types.Message):
    await message.answer(text='Введите секунд задержки с 2-10 сообщения:')
    await UserStates.PingTwo.set()


@dp.message_handler(state=UserStates.PingTwo)
async def process_number(message: types.Message, state: FSMContext):
    try:
        CONFIG.PINGTWO = Decimal(message.text)
        await state.finish()
    except ValueError:
        await message.answer("Ошибка ввода. Пожалуйста, введите корректное число.")
        return
