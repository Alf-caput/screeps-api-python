import screeps_py_api
import json
from collections import namedtuple
from random import randint
import constants
import time
# Your code goes here
def main(api):
    _id = '64e5c7e6489cac4d15a95621'  # Spawn id
    room_name = 'E17S26'
    shard = 'shard3'
    spawn_name = 'Spawn1'
    creep_body = ['move']
    print('Reading room objects...')
    response = api.room_objects(room=room_name, shard=shard).json()['objects']
    spawn_info = api.find_dict_in_listdicts("_id", _id, response)
    if spawn_info['store']['energy'] >= 300 and not spawn_info['spawning']:
        print('Spawning creep...')
        creep_name = f'worker{randint(1000, 9999)}'
        response = api.spawn_creep(spawn_name=spawn_name,
                                   creep_body=creep_body,
                                   creep_name=creep_name,
                                   shard=shard).json()
    else:
        print('Spawning not available')
    return

if __name__ == '__main__':
    # Retriving user's token from config.json
    with open('config.json') as config_file:
        config = json.load(config_file)
    token = config.get('token')

    # Context that creates and closes the session with the api
    with screeps_py_api.api_client_context(token) as game_api:
        main(game_api)