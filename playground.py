from collections import namedtuple
class JsKeyword:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return self.value
    
true = JsKeyword('true')
Foo = namedtuple('Foo', 'a b c')
my_var = Foo(true, True, False)
print(my_var)