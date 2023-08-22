import json
import requests
from contextlib import contextmanager


class APIClient:
    def __init__(self, token, base_url):
        self.base_url = base_url
        self.token = token
        self.session = requests.Session()
        self.session.headers = {'X-Token': self.token, 'X-Username': self.token}
    
    def _getdata(self, endpoint, dict_format=True, **params):
        response = self.session.get(f'{self.base_url}/{endpoint}', params=params)
        response.raise_for_status()
        return response.json() if dict_format else json.dumps(response.json())
    
    def _postdata(self, endpoint, dict_format=True, **data):
        response = self.session.post(f'{self.base_url}/{endpoint}', json=data)
        response.raise_for_status()
        return response.json() if dict_format else json.dumps(response.json())
        
    def me(self):
        return self._getdata('auth/me')

    def console(self, expression='', shard='shard3'):
        return self._postdata('user/console', expression=expression, shard=shard)
    
    def game(self):
        return self._getdata('game/room-overview', shard='shard3')
    
    def spawn(self, spawn, creep):
        # command = f"Game.spawns['{spawn}'].spawnCreep({', '.join((body[part]).__repr__() for part in body)});"
        command = f"Game.spawns['{spawn}'].spawnCreep{str(creep)[5:]};"
        print(command)
        return self.console(expression=command, shard='shard3')
    
    def close(self):
        return self.session.close()

@contextmanager
def api_client_context(token, base_url='https://screeps.com/api'):
    print(f'connecting to {base_url}...')
    client = APIClient(token, base_url)
    try:
        yield client
    finally:
        print('closing connection...')
        client.close()
