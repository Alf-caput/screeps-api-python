import utils
from collections import namedtuple
from dictdot import dictdot


class JsKeyword:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return self.value

    def __str__(self) -> str:
        return str(self.value)

_true = JsKeyword('true')
_null = JsKeyword('{}')

Creep = namedtuple('Creep', field_names=('body', 'name', 'opts'), defaults=(_null, _null, _null))

endpoints = dictdot()
endpoints.user = 'user/code'
endpoints.auth = 'auth/'
endpoints.game = 'game/'
