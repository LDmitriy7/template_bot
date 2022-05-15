from dotenv import load_dotenv

import api

load_dotenv()


class _Bot:

    @property
    def token(self) -> str:
        return api.config.get_env('BOT_TOKEN', required=True)


bot = _Bot()


class _Database:

    @property
    def name(self) -> str:
        return api.config.get_env('DATABASE_NAME', required=True)

    @property
    def host(self) -> str:
        return api.config.get_env('DATABASE_HOST', required=True)


db = _Database()


class _Admins:

    @property
    def owner_id(self) -> int:
        value = api.config.get_env('OWNER_ID', required=True)
        return int(value)

    @property
    def ids(self) -> list[int]:
        config = api.config.get_doc()
        return config.admins_ids


admins = _Admins()


class _Log:

    @property
    def file(self) -> str:
        config = api.config.get_doc()
        return config.log_file or '.log'

    @property
    def level(self) -> int | None:
        config = api.config.get_doc()
        return config.log_level


log = _Log()
