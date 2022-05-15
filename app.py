from aiogram import executor

import commands
import config
from loader import dp


async def on_startup(_):
    import filters
    import handlers
    import middlewares
    import tasks

    filters.setup(dp)
    handlers.setup()
    middlewares.setup(dp)
    tasks.setup()
    await commands.setup()
    await dp.bot.send_message(config.admins.owner_id, 'Бот запущен...')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
