from aiogram import Dispatcher
from aiogram_utils import middlewares


def setup(dp: Dispatcher):
    dp.setup_middleware(middlewares.AnswerAnyQuery())
