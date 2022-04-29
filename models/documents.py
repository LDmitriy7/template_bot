from __future__ import annotations

import mongoengine as me
from aiogram_utils.mongoengine import Document


class Test(Document):
    a: str = me.StringField()
    b: int = me.IntField()
