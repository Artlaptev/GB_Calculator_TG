from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from Handler import Handler, Common
from States_Data import CalcsStates


def register_message_calc(dp: Dispatcher):
    dp.register_message_handler(Handler.calculation_start,
                                commands='/start')
    dp.register_message_handler(Handler.first_number_entered)
    dp.register_message_handler(Handler.operator_entered)
    dp.register_message_handler(Handler.second_number_entered)

# def register_message_common(dp:Dispatcher):
#     dp.register_message_handler(Common.cmd_start, commands="/start", state="*")
#     dp.register_message_handler(Common.cmd_cancel, commands="/cancel", state="*")
