from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from integer import integer
from calc_fraction import calc_fraction
from complex_num import complex_num

Token = ''

with open('token.ini', 'r') as file:
    Token = file.read()
bot = Bot(token=Token)
dp = Dispatcher(bot)


class OrderFood(StatesGroup):
    waiting_for_food_name = State()
    waiting_for_food_size = State()


@dp.message_handler(commands=['start'])
async def Calc_start(message: types.Message):
    await  message.answer(
        'Введите выражение вида: наименование_калькулятора первый_операнд оператор второй_операнд. Разделитель пробел. Для получения справки введите /help')


@dp.message_handler(commands=['help'])
async def Calc_help(message: types.Message):
    await  message.answer('Целое число "I", рациональное "R" или комплексное "C" /n'
                          'Рациональное число вводить в виде n/m, где n,m - целые числа /n'
                          'Комплексное число вводить в виде a+bi, где a,b - целые числа, i-мнимая единица')


@dp.message_handler()
async def calc_handler(message: types.Message):
    lst = message.text.split(' ')
    await message.answer(calculation(lst))



def calculation(lst: list):
    if is_valid_data(lst)==False:
        return 'error'
    calc = str.upper(lst[0])
    number1 = lst[1]
    operator = lst[2]
    number2 = lst[3]
    if calc=='I':
        try:
            return integer(act=operator,num1=int(number1),num2=int(number2))
        except ValueError:
            return 'ValureError'
    if calc=='R':
        r1=number1.split('/')
        r2=number2.split('/')
        a=int(r1[0])
        b=int(r1[1])
        c=int(r2[0])
        d=int(r2[1])
        return calc_fraction(operator,a,b,c,d)
    if calc=='C':
        return  str(complex_num(number1,number2,operator))
    else:
        return 'error'



def is_valid_data(lst: list):
    if len(lst) != 4:
        return False


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
