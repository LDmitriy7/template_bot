DEFAULT_ENV = {
    'BOT_TOKEN': '',
    'OWNER_ID': 724477101,
    'DATABASE_NAME': 'TemplateBot',
    'DATABASE_HOST': 'localhost',
}

GUIDE_TEXT = """
You should set environment variables.
You can skip any variable, it will be taken from "[]"
"""

END_TEXT = """
Starting docker...
"""

FP = '.env'


def extract_vars(text):
    _vars = {}

    for string in text.strip().split('\n'):
        key, value = string.split('=', maxsplit=1)
        _vars[key] = value

    return _vars


def dump_vars(_vars: dict):
    text = ''

    for key, value in _vars.items():
        text += f'{key}={value}\n'

    return text


print(GUIDE_TEXT)

try:
    file = open(FP, mode='r')
except FileNotFoundError:
    env = {}
else:
    env = extract_vars(file.read())

for k, v in DEFAULT_ENV.items():
    cur_v = env.get(k, v)
    new_v = input(f'${k} [{cur_v}]: ') or cur_v
    env[k] = new_v

file = open(FP, mode='w')
file.write(dump_vars(env))

print(END_TEXT)
