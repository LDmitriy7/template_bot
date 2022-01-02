from aiogram import types

import commands
import texts
from loader import dp


@dp.message_handler(commands=commands.START, state='*')
async def welcome(msg: types.Message):
    await msg.answer(texts.welcome)
