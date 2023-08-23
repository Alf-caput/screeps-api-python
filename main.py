import screeps_py_api
import json
from collections import namedtuple
from random import randint
import constants

# Your code goes here
def main(api):
    # Replace this code's structure_id and room_name variables with yours
    _id = 'room'
    room_name = 'E17S26'
    action = 'destroyStructure'
    shard = 'shard3'
    structure_id = '5beef69780a5196874bb6987'
    intent = [{'id': structure_id}]
    response = api.add_object_intent(_id=_id,
                                    room=room_name,
                                    intent=intent,
                                    name=action,
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