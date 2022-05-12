import yaml

_file = open('secrets/env.yml')
_env = yaml.load(_file, yaml.Loader)


class Bot:
    _data = _env['bot']

    token = _data['token']
    skip_updates = _data.get('skip_updates', False)


class Database:
    _data = _env['database']

    name = _data['name']
    host = _data.get('host', 'localhost')


class Users:
    _data = _env['users']

    admins_ids = _data['admins_ids']


class Log:
    _data = _env['log']

    file = _data.get('file')
    level = _data.get('level')
