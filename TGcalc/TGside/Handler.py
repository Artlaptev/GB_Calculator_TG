from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import available_calcs, available_operators
from States_Data import CalcsStates


class messages():
    integer_invitation = 'Введите целое число'
    rational_invitation = 'Введите число вида n/m'
    complex_invitation = 'Введите число вида a+bi, где a,b - целые числа'
    assepted = 'Принято. '


def get_calc_message(calc):
    if calc == available_calcs[0]:
        return messages.integer_invitation
    if calc == available_calcs[1]:
        return messages.rational_invitation
    if calc == available_calcs[2]:
        return messages.complex_invitation

class Handler():

    async def calculation_start(message: types.Message, state: FSMContext):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for name in available_calcs:
            keyboard.add(name)
        await message.answer('Выберите калькулятор из предложенных: I - целые, R - рациональные, C - комплексные:',
                             reply_markup=keyboard)
        await state.set_state(CalcsStates.waiting_for_choiсen_calculator.state)

    async def calc_chocen(message: types.Message, state: FSMContext):
        current_messege = message.text
        if current_messege not in available_calcs:
            await message.answer('Ошибка, выберите калькулятор, используя клавиатуру')
            return
        await state.update_data(chosen_calc=message.text)  # обновление данных
        await state.set_state(CalcsStates.waiting_for_enter_first_number)  # Фиксация состояния

        answer = get_calc_message(current_messege)
        await message.answer(answer, reply_markup=types.ReplyKeyboardRemove())  # Запрос первого чиста

    async def first_number_entered(message: types.Message, state: FSMContext):
        current_messege = message.text
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for name in available_operators:
            keyboard.add(name)

        await state.update_data(first_number=message.text)  # обновление данных
        await state.set_state(CalcsStates.waiting_for_choiсen_oprator)  # Фиксация состояния
        await message.answer('Введите оператор из предложенных', reply_markup=keyboard)  # Запрос оператора

    async def operator_entered(message: types.Message, state: FSMContext):
        current_messege = message.text
        if current_messege not in available_operators:
            await message.answer('Ошибка, выберите оператор, используя клавиатуру')
            return
        await state.update_data(chosen_operator=message.text)  # обновление данных
        await state.set_state(CalcsStates.waiting_for_enter_second_number)  # Фиксация состояния

        data_base = await state.get_data()
        answer = get_calc_message(data_base['chosen_calc'])

        await message.answer(answer, reply_markup=types.ReplyKeyboardRemove())  # Запрос второго чиста

    async def second_number_entered(message: types.Message, state: FSMContext):
        concurrent_messege = message.text

        await  state.update_data(second_number=message.text)
        await state.set_state(CalcsStates.waiting_for_backend_answer)

class Common():
    async def cmd_start(message: types.Message, state: FSMContext):
        await state.finish()

    async def cmd_cancel(message: types.Message, state: FSMContext):
        await state.finish()
        await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())
