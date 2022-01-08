from aiogram_utils import middlewares

from loader import dp


def setup():
    dp.setup_middleware(middlewares.AnswerAnyQuery())
