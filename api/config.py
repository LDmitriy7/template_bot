import os

from models import documents


def get_env(key: str, default=None, required=False):
    value = os.getenv(key, default)
    if required and value is None:
        print(f'You must set env ${key}')
        exit(1)
    return value


def get_doc():
    config = documents.Config.object() or documents.Config().save()
    return config
