import screeps_py_api as screeps_api
import json
from collections import namedtuple
from random import randint

class JsKeyword:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return self.value
    
_true = JsKeyword('true')
_null = JsKeyword('{}')


Creep = namedtuple('Creep', field_names=('body', 'name', 'opts'), defaults=(_null, _null, _null))

# Your code goes here
def main(api):
    spawn = 'Spawn1'
    for _ in range(1):
        new_worker = Creep(['move'], f'worker{randint(1000, 9999)}', {'dryRun': _true})
        print(json.dumps(api.spawn(spawn, new_worker), indent=4))
    # print(api.read_console)
    return

if __name__ == '__main__':
    # Retriving user's token from config.json
    with open('config.json') as config_file:
        config = json.load(config_file)
    token = config.get('token')

    # Context that creates and closes the session with the api
    with screeps_api.api_client_context(token) as game_api:
        main(game_api)