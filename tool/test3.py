


class A:

    def __new__(cls, *args, **kwargs):
        print(id(cls))
        obj = object.__new__(cls)
        print(id(obj))
        return obj


    def __init__(self):
        print(id(self))


A()
