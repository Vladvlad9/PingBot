from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStates(StatesGroup):
    Ping = State()
    PingTwo = State()

