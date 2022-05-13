from __future__ import annotations

import mongoengine as me
from aiogram_utils.mongoengine import Document


class Config(Document):
    admins_ids: list[int] = me.ListField(me.IntField())
    log_file: str = me.StringField()
    log_level: int = me.IntField()
