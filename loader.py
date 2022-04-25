import logging

import mongoengine as me
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram_utils.task_manager import TaskManager

import config

me.connect(
    db=config.Database.name,
    username=config.Database.username,
    password=config.Database.password,
    host=config.Database.host,
    port=config.Database.port,
    authentication_source=config.Database.auth_source,
)

storage = MongoStorage(
    db_name=config.Database.name,
    username=config.Database.username,
    password=config.Database.password,
    host=config.Database.host,
    port=config.Database.port,
)

bot = Bot(config.Bot.token, parse_mode=types.ParseMode.HTML)
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
