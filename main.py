import screeps_py_api as screeps_api
import json
from collections import namedtuple
from random import randint

Creep = namedtuple('Creep', field_names=('body', 'name', 'opts'), defaults=(None, None, None))

# Your code goes here
def main(api):
    spawn = 'Spawn1'
    for _ in range(1, 4):
        new_worker = Creep(['move'], f'worker{randint(1000, 9999)}')
        print(api.spawn(spawn, new_worker))
    return

if __name__ == '__main__':
    # Retriving user's token from config.json
    with open('config.json') as config_file:
        config = json.load(config_file)
    token = config.get('token')

    # Context that creates and closes the session with the api
    with screeps_api.api_client_context(token) as game_api:
        main(game_api)