import screeps_py_api
import json
from collections import namedtuple
from random import randint
import constants

# Your code goes here
def main(api):
    room_name = 'E17S26'
    shard = 'shard3'
    response = api.room_objects(room=room_name, 
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