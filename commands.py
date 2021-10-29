from contextlib import suppress

from aiogram import types
from aiogram.utils.exceptions import TelegramAPIError

import config
from loader import dp

START = 'start'
CANCEL = 'cancel'
BROADCAST = 'broadcast'

USER_COMMANDS = [
    types.BotCommand(START, 'Запустить бота'),
]

ADMIN_COMMANDS = USER_COMMANDS + [
    types.BotCommand(CANCEL, 'Отменить'),
    types.BotCommand(BROADCAST, 'Рассылка'),
]


async def setup():
    await dp.bot.set_my_commands(USER_COMMANDS)

    for user_id in config.Users.admins_ids:
        with suppress(TelegramAPIError):
            await dp.bot.set_my_commands(ADMIN_COMMANDS, scope=types.BotCommandScopeChat(user_id))
