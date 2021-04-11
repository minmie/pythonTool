import time
"""
装饰器在加载到被装饰函数的时候运行,只执行一次

"""

def wrapper(f):

    print(1111)
    def inner(*args, **kwargs):
        s = time.time()
        f(*args, **kwargs)
        e = time.time()
        print('耗时',e - s)
    return inner

@wrapper
def func(a):
    print(a)
    time.sleep(1)

def func2(a):
    print(a)
    time.sleep(1)

print('aaaa')
if __name__ == '__main__':

    print('bbbbb')
    func(1)