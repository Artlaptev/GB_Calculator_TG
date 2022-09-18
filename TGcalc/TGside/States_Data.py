from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class CalcsStates(StatesGroup):
    waiting_for_choiсen_calculator = State()
    waiting_for_choiсen_oprator = State()
    waiting_for_enter_first_number = State()
    waiting_for_enter_second_number = State()
    waiting_for_backend_answer = State()

