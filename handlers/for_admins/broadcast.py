from aiogram import types

import commands
import config
import texts
from loader import dp


@dp.message_handler(commands=commands.BROADCAST, user_id=config.admins.ids)
async def broadcast(msg: types.Message):
    await msg.answer(texts.not_implemented)
