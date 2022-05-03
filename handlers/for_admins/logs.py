from aiogram import types

import commands
import config
import texts
from loader import dp


@dp.message_handler(commands=commands.LOGS, user_id=config.Users.admins_ids)
async def logs(msg: types.Message):
    document = types.InputFile(config.Log.file, filename='logs.txt')
    await msg.answer_document(document)
