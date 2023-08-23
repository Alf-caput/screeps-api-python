import screeps_py_api
import json
from collections import namedtuple
from random import randint
import constants

# Your code goes here
def main(api):
    # structure_id = '5beefa90c817d76880ba3d2a'
    # room_name = 'E17S26'
    # user_id = 'Alf_'  # maybe??
    # shard = 'shard3'
    # # response = api.room_overview().json()
    # response = api.add_object_intent(_id="room",
    #                                 room='E17S26',
    #                                 name='destroyStructure',
    #                                 intent=[{'id': structure_id,
    #                                          'roomName': room_name,
    #                                          'user': user_id},],
    #                                 shard=shard).json()
    
    # structure_id = '64e5c7e6489cac4d15a95621'
    # room_name = 'E17S26'
    # user_id = 'Alf_'
    # shard = 'shard3'
    # creep_id = ''
    # intent2 = [
    #     {'id': structure_id,
    #      'roomName': room_name,
    #      'user': user_id,
    #      'body': ['move'],
    #      'name': 'Alf'}
    # ]
    # intent = [
    #     {'id': structure_id,
    #      'roomName': room_name,
    #      'user': user_id,
    #      'body': ['move'],
    #      'name': 'Alf'}
    # ]
    # # response = api.room_overview().json()
    # response = api.add_object_intent(_id=structure_id,
    #                                 room='E17S26',
    #                                 name='StructureSpawn',
    #                                 intent=intent,
    #                                 shard=shard).json()

    structure_id = '5beefaa9b100ae2e78d91f4c'
    room_name = 'E17S26'
    user_id = 'Alf_'  # maybe??
    shard = 'shard3'
    response = api.add_object_intent(_id="room",
                                    room='E17S26',
                                    name='destroyStructure',
                                    intent=[{'id': structure_id,
                                             'roomName': room_name,
                                             },],
                                    shard=shard).json()

    # key1 = 'x'
    # key2 = 'y'
    # value1 = 0
    # value2 = 0
    # _id_spawn1 = "64e5c7e6489cac4d15a95621"
    # for d in response['terrain']:
    #     print(f'{d[key1] = }, {d[key2] = }')
    #     if d[key1] == value1 and d[key2] == value2:
    #         searched_dict = d.copy()
    # print(searched_dict)
    print(json.dumps(response, indent=4))
    # print(api.room_overview().json())
    return

if __name__ == '__main__':
    # Retriving user's token from config.json
    with open('config.json') as config_file:
        config = json.load(config_file)
    token = config.get('token')

    # Context that creates and closes the session with the api
    with screeps_py_api.api_client_context(token) as game_api:
        main(game_api)