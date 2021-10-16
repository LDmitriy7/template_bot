import mongoengine as me
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.mongo import MongoStorage

import config

me.connect(
    db=config.Database.NAME,
    username=config.Database.USERNAME,
    password=config.Database.PASSWORD,
    host=config.Database.HOST,
    port=config.Database.PORT,
    authentication_source=config.Database.AUTH_SOURCE,
)

storage = MongoStorage(
    db_name=config.Database.NAME,
    username=config.Database.USERNAME,
    password=config.Database.PASSWORD,
    host=config.Database.HOST,
    port=config.Database.PORT,
)

bot = Bot(config.Bot.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
