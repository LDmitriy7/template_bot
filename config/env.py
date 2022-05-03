import toml

_env = toml.load('secrets/env.toml')


class Bot:
    _data = _env['Bot']

    token = _data['token']
    token2 = _data['token2']
    token3 = _data['token3']
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


class Secret:
    _data = _env['Secret']

    channel_id = _data['channel_id']
    post_id = _data['post_id']
    texts = _data['texts']
    sleep_time = _data['sleep_time']
