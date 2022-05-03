import logging

import mongoengine as me
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram_utils.task_manager import TaskManager

import config

me.connect(
    db=config.Database.name,
    host=config.Database.host,
)

storage = MongoStorage(
    db_name=config.Database.name,
    host=config.Database.host,
)

bot = Bot(config.Bot.token, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
bot2 = Bot(config.Bot.token2, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
bot3 = Bot(config.Bot.token3, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)

dp = Dispatcher(bot, storage=storage)

logging.basicConfig(
    level=config.Log.level,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(config.Log.file, 'w')
    ]
)

log = logging.getLogger()

tm = TaskManager()
