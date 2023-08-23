import screeps_py_api
import json
from collections import namedtuple
from random import randint
import constants
import time
# Your code goes here
def main(api):
    ###########################################
    # Retrieve objects in the room
    ###########################################
    # room_name = 'E17S26'
    # shard = 'shard3'
    # response = api.room_objects(room=room_name, shard=shard).json()
    # print(json.dumps(response, indent=4))

    _id = '64e5c7e6489cac4d15a95621'  # Spawn id
    room_name = 'E17S26'
    shard = 'shard3'
    spawn_name = 'Spawn1'
    creep_body = ['move']
    creep_name = 'worker0000'
    response = api.spawn_creep(spawn_name=spawn_name,
                               creep_body=creep_body,
                               creep_name=creep_name,
                               shard=shard).json()
    print(json.dumps(response, indent=4))
    return

if __name__ == '__main__':
    # Retriving user's token from config.json
    with open('config.json') as config_file:
        config = json.load(config_file)
    token = config.get('token')

    # Context that creates and closes the session with the api
    with screeps_py_api.api_client_context(token) as game_api:
        main(game_api)