import json
import requests
from contextlib import contextmanager


class APIClient:
    def __init__(self, token, base_url):
        self.base_url = base_url
        self.token = token
        self.session = requests.Session()
        self.session.headers = {'X-Token': self.token,
                                'X-Username': self.token}
    
    def _getdata(self, endpoint, **params):
        return self.session.request(method='GET',
                                    url=f'{self.base_url}/{endpoint}',
                                    params=params)
    
    def _postdata(self, endpoint, **json):
        return self.session.request(method='POST',
                                    url=f'{self.base_url}/{endpoint}',
                                    json=json)

    def me(self):
        return self._getdata('auth/me')

    def console(self, expression='', shard='shard3'):
        return self._postdata(endpoint='user/console',
                              expression=expression,
                              shard=shard)
    
    def add_object_intent(self, _id='', room='', name='', intent='', shard=''):
        return self._postdata(endpoint=f'game/add-object-intent',
                              _id=_id,
                              room=room,
                              name=name,
                              intent=intent,
                              shard=shard)   

    def room_objects(self, room='', shard=''):
        return self._getdata(endpoint=f'game/room-objects?room={room}',
                             shard='shard3')

    def room_overview(self):  
        return self._getdata(endpoint='game/room-overview',
                             shard='shard3')

    # def spawn(self, spawn, creep):
    #     # command = f"Game.spawns['{spawn}'].spawnCreep({', '.join((body[part]).__repr__() for part in body)});"
    #     command = f"Game.spawns['{spawn}'].spawnCreep{str(creep)[5:]};"
    #     print(command)
    #     return self.console(expression=command, shard='shard3')
    
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
        