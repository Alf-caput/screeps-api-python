import utils
from collections import namedtuple


class JsKeyword:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return self.value

    def __str__(self) -> str:
        return str(self.value)

_true = utils.JsKeyword('true')
_null = utils.JsKeyword('{}')

Creep = namedtuple('Creep', field_names=('body', 'name', 'opts'), defaults=(_null, _null, _null))