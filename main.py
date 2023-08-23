import screeps_py_api
import json
from collections import namedtuple
from random import randint
import constants

# Your code goes here
def main(api):
    endpoints = [
        'game/room-status',
        'game/create-object-intent',
        'user/memory',
        'user/sandbox-console',
        'user/messages',
        'user/notification-settings',
        'user/market-orders'
    ]
    for ep in endpoints:
        response = api._getdata(endpoint=f'game/room-overview')
        print(response, ep)
    # print(json.dumps(response, indent=4))
    return

if __name__ == '__main__':
    # Retriving user's token from config.json
    with open('config.json') as config_file:
        config = json.load(config_file)
    token = config.get('token')

    # Context that creates and closes the session with the api
    with screeps_py_api.api_client_context(token) as game_api:
        main(game_api)