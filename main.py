import logging

from aiogram import executor

import commands
import config
from loader import dp, arg_parser


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
    args = arg_parser.parse_args()
    filename = None if args.log_to_stdout else config.Log.FILE
    logging.basicConfig(filename=filename, level=config.Log.LEVEL)

    executor.start_polling(dp, on_startup=on_startup, skip_updates=config.Bot.SKIP_UPDATES)
