from aiogram import executor

import commands
import config
from loader import dp


async def on_startup(_):
    import filters
    import handlers
    import middlewares
    import tasks

    filters.setup()
    handlers.setup()
    middlewares.setup()
    tasks.setup()
    await commands.setup()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=config.Bot.skip_updates)
