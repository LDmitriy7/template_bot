from contextlib import suppress

from aiogram import types
from aiogram.utils.exceptions import TelegramAPIError

import config
from loader import dp

START = 'start'
CANCEL = 'cancel'
BROADCAST = 'broadcast'
SET_COMMANDS = 'set_commands'

USER_COMMANDS = [
    # types.BotCommand(START, 'Запустить бота'),
    # types.BotCommand(CANCEL, 'Отменить'),
]

ADMIN_COMMANDS = USER_COMMANDS + [
    types.BotCommand(BROADCAST, 'Рассылка'),
    types.BotCommand(SET_COMMANDS, 'Обновить команды'),
]


async def setup():
    await dp.bot.set_my_commands(USER_COMMANDS)

    for user_id in config.Users.admins_ids:
        with suppress(TelegramAPIError):
            await dp.bot.set_my_commands(ADMIN_COMMANDS, scope=types.BotCommandScopeChat(user_id))
