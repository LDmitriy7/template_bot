import yaml

print('You should set environment variables\n')

fp = 'docker-compose.yml'
file = open(fp, mode='r')

content = yaml.load(file, yaml.Loader)

app = content['services']['app']
environment_new = []

for string in app['environment']:
    key, value = string.split('=', maxsplit=1)

    value_new = input(f'${key} [{value}]: ') or value
    string_new = f'{key}={value_new}'

    environment_new.append(string_new)

app['environment'] = environment_new

file = open(fp, mode='w')

yaml.dump(content, file, yaml.Dumper)
