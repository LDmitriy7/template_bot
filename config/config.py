import toml

_config = toml.load('config.toml')


class Database:
    _data = _config['Database']

    NAME = _data['NAME']
    HOST = _data.get('HOST', 'localhost')
    PORT = _data.get('PORT', 27017)
    USERNAME = _data.get('USERNAME')
    PASSWORD = _data.get('PASSWORD')
    AUTH_SOURCE = _data.get('AUTH_SOURCE', 'admin')


class Bot:
    _data = _config['Bot']

    TOKEN = _data['TOKEN']
    SKIP_UPDATES = _data.get('SKIP_UPDATES', False)


class Users:
    _data = _config['Users']

    ADMINS_IDS = _data['ADMINS_IDS']


class Log:
    _data = _config['Log']

    FILE = _data.get('FILE')
    LEVEL = _data.get('LEVEL')
