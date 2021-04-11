
# 单利的四种实现
"""
一、使用python模块来实现单利，因为模块再第一次导入后会生成pyc，当第二次导入时，直接加载pyc文件，而不会再次执行代码。

# file1.py
class Single:
    def foo(self):
        pass

singleton = Single()
# file2.y
from file1 import singleton
singleton.foo()

"""


# 二、重写new方法
class A:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if A.__instance is None:
            A.__instance = object.__new__(cls)
        return A.__instance

    def __init__(self, name='a',age=10):
        self.name = name
        self.age = age
obj1 = A('arivn')
obj2 = A('alex')
print(id(obj1))
print(id(obj2))


# 三、使用装饰器

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls in instances:
            return instances[cls]
        obj = cls(*args, **kwargs)
        instances[cls] = obj
        return obj

    return get_instance

@singleton
class B:
    pass

b1 = B()
b2 = B()
print(id(b1) == id(b2))


# 四、