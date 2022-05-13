from aiogram import types
from aiogram.utils.exceptions import TelegramAPIError
from aiogram_utils.errors import suppress

import config
from loader import dp, log

START = 'start'
CANCEL = 'cancel'
BROADCAST = 'broadcast'
SET_COMMANDS = 'set_commands'
LOGS = 'logs'

USER_COMMANDS = [
    # types.BotCommand(START, 'Запустить бота'),
    # types.BotCommand(CANCEL, 'Отменить'),
]

ADMIN_COMMANDS = USER_COMMANDS + [
    types.BotCommand(BROADCAST, 'Рассылка'),
    types.BotCommand(SET_COMMANDS, 'Обновить команды'),
    types.BotCommand(LOGS, 'Логи'),
]


async def setup():
    await dp.bot.set_my_commands(USER_COMMANDS)

    for user_id in config.admins.ids:
        with suppress(TelegramAPIError, logger=log, user_id=user_id):
            await dp.bot.set_my_commands(ADMIN_COMMANDS, scope=types.BotCommandScopeChat(user_id))
