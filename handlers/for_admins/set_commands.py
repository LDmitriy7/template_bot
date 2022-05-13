from aiogram import types

import commands
import config
import texts
from loader import dp


@dp.message_handler(commands=commands.SET_COMMANDS, user_id=config.admins.ids)
async def set_commands(msg: types.Message):
    await commands.setup()
    await msg.answer(texts.commands_updated)
