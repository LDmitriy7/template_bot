import asyncio

from aiogram import types

import config
from loader import dp


@dp.message_handler(commands='test', user_id=config.admins.owner_id)
async def _(msg: types.Message):
    await msg.answer('...')


@dp.message_handler(commands='restart', user_id=config.admins.owner_id)
async def restart(msg: types.Message):
    await msg.answer('Перезагрузка...')

    async def _exit():
        dp.stop_polling()
        await asyncio.sleep(5)
        asyncio.get_event_loop().stop()

    asyncio.create_task(_exit())
