import toml

_env = toml.load('secrets/env.toml')


class Bot:
    _data = _env['Bot']

    token = _data['token']
    skip_updates = _data.get('skip_updates', False)


class Database:
    _data = _env['Database']

    name = _data['name']
    host = _data.get('host', 'localhost')


class Users:
    _data = _env['Users']

    admins_ids = _data['admins_ids']


class Log:
    _data = _env['Log']

    file = _data.get('file')
    level = _data.get('level')
