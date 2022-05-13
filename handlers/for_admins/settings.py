import asyncio

from aiogram import types

import commands
import config
from loader import dp


@dp.message_handler(commands='test', user_id=config.admins.owner_id)
async def _(msg: types.Message):
    await msg.answer('...')


@dp.message_handler(commands=commands.RESTART, user_id=config.admins.owner_id)
async def restart(msg: types.Message):
    await msg.answer('Остановка бота...')

    async def _exit():
        dp.stop_polling()
        await dp.wait_closed()
        await asyncio.sleep(10)
        asyncio.get_event_loop().stop()

    asyncio.create_task(_exit())
