import json
import requests
from contextlib import contextmanager


class APIClient:
    def __init__(self, token, base_url):
        self.base_url = base_url
        self.token = token
        self.session = requests.Session()
        self.session.headers = {'X-Token': self.token, 'X-Username': self.token}
    
    def _getdata(self, endpoint, **params):
        response = self.session.get(self.base_url+endpoint, params=params)
        response.raise_for_status()
        return response.json()
    
    def _postdata(self, endpoint, **data):
        response = self.session.post(self.base_url+endpoint, json=data)
        response.raise_for_status()
        return response.json()
        
    def me(self):
        return self._getdata('auth/me')

    def console(self, expression='', shard='shard0'):
        return self._postdata('user/console', expression=f'console.log("{expression}")', shard=shard)
    
    def game(self):
        return self._getdata('game/room-overview', shard='shard3')
        
    def close(self):
        return self.session.close()

@contextmanager
def api_client_context(token, base_url='https://screeps.com/api/'):
    print(f'connecting to {base_url}...')
    client = APIClient(token, base_url)
    try:
        yield client
    finally:
        print('closing connection...')
        client.close()
