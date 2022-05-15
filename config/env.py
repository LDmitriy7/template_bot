import os

from dotenv import load_dotenv

from models import documents

load_dotenv()


def _get_env(key: str, default=None, required=False):
    value = os.getenv(key, default)
    if required and value is None:
        print(f'You must set env ${key}')
        exit(1)
    return value


def _get_config():
    config = documents.Config.object() or documents.Config().save()
    return config


class _Bot:

    @property
    def token(self):
        return _get_env('BOT_TOKEN', required=True)


bot = _Bot()


class _Database:

    @property
    def name(self):
        return _get_env('DATABASE_NAME', required=True)

    @property
    def host(self):
        return _get_env('DATABASE_HOST', required=True)


db = _Database()


class _Admins:

    @property
    def owner_id(self):
        value = _get_env('OWNER_ID', required=True)
        return int(value)

    @property
    def ids(self):
        config = _get_config()
        return config.admins_ids


admins = _Admins()


class _Log:

    @property
    def file(self):
        config = _get_config()
        return config.log_file or '.log'

    @property
    def level(self):
        config = _get_config()
        return config.log_level


log = _Log()
