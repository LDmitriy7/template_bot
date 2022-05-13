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
        await asyncio.sleep(5)
        asyncio.get_event_loop().stop()

    asyncio.create_task(_exit())

# @dp.message_handler(commands=commands.RESTART, user_id=config.admins.owner_id)
# async def restart(msg: types.Message):
#     _config = documents.Config.object() or documents.Config().save()
#
#     if _config.restart_date and (datetime.now() - _config.restart_date) < timedelta(seconds=10):
#         await msg.answer('...')
#         return
#
#     await msg.answer('Остановка бота...')
#
#     dp.stop_polling()
#     await dp.wait_closed()
#
#     _config.restart_date = datetime.now()
#     _config.save()
#
#     asyncio.get_event_loop().stop()
