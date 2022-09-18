import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import BotCommand
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Handler import Handler
from States_Data import CalcsStates
import registrator




async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot.set_my_commands(commands)


async def Main():
    with open('token.ini', 'r') as file:
        Token = file.read()
    bot = Bot(token=Token)
    dp = Dispatcher(bot,storage=MemoryStorage())

    current_state=FSMContext.set_state(CalcsStates.waiting_for_choiсen_calculator)
    # registrator.register_message_common(dp)
    registrator.register_message_calc(dp)

    await set_commands(bot)
    await dp.skip_updates()
    await dp.start_polling()



if __name__ == '__main__':
    asyncio.run(Main())
