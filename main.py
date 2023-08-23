import screeps_py_api as screeps_api
import json
from collections import namedtuple
from random import randint

# Your code goes here
def main(api):
    response = api.console(expression='console.log("hi")').json()
    print(type(response))
    print(json.dumps(response, indent=4))
    # print(api.room_overview().json())
    return

if __name__ == '__main__':
    # Retriving user's token from config.json
    with open('config.json') as config_file:
        config = json.load(config_file)
    token = config.get('token')

    # Context that creates and closes the session with the api
    with screeps_api.api_client_context(token) as game_api:
        main(game_api)