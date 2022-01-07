from loader import dp
from .answer_any_query import AnswerAnyQuery


def setup():
    dp.setup_middleware(AnswerAnyQuery())
