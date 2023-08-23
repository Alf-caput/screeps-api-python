import screeps_py_api
import json
from collections import namedtuple
from random import randint
import constants

# Your code goes here
def main(api):
    _id = 'room'
    room_name = 'E17S26'
    name = 'destroyStructure'
    shard = 'shard3'
    structure_id = '5beef6af57e410647929e1e7'
    intent = [{'id': structure_id}]
    response = api.add_object_intent(_id=_id,
                                    room=room_name,
                                    intent=intent,
                                    name=name,
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