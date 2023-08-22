import screeps_py_api as screeps_api
import json
import requests

# Your code goes here
def main(api):
    # print(json.dumps(api.me()))
    # print(json.dumps(api.console(expression='I made my own api!!!', shard='shard3'), indent=4))
    # type(api.game())
    # print('Here')
    # print((x:=json.dumps(api.game())), type(x))
    # print(json.dumps(api.game(), indent=4))
    body = {"creepName": "'Worker2'",
            "body": "[MOVE]"}
    spawn = "'Spawn1'"
    api.spawn(spawn, body)
    # print(json.dumps(api.console(expression='I made my own api!!!', shard='shard3'), indent=4))
    return

if __name__ == '__main__':
    # Retriving user's token from config.json
    with open('config.json') as config_file:
        config = json.load(config_file)
    token = config.get('token')

    # Context that creates and closes the session with the api
    with screeps_api.api_client_context(token) as game_api:
        main(game_api)