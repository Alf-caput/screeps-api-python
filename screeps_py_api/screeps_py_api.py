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
    
    def add_object_intent(self, _id='room', room='E17S26', name='destroyStructure', intent=[{'id': '5beef69780a5196874bb6987'},], shard='shard3'):
        return self._postdata(endpoint='game/add-object-intent',
                              _id=_id,
                              room=room,
                              name=name,
                              intent=intent,
                              shard=shard)   

    def room_objects(self, room='E17S26', shard='shard3'):
        return self._getdata(endpoint=f'game/room-objects?room={room}',
                             shard=shard)

    def room_overview(self, shard='shard3'):  
        return self._getdata(endpoint='game/room-overview',
                             shard=shard)

    def spawn_creep(self, spawn_name='Spawn1', creep_body=["move"], creep_name='worker', opts='{}', shard='shard3'):
        spawn_str = f'Game.spawns[{spawn_name.__repr__()}].spawnCreep({creep_body},{creep_name.__repr__()}, {opts})'
        print(spawn_str)
        return self.console(expression=spawn_str, shard=shard)

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
        