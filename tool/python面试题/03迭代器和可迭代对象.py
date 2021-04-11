from collections import Iterable, Iterator



class A:

    def __iter__(self):
        pass


class B:
    def __next__(self):
        pass





class C:
    def __next__(self):
        pass


    def __iter__(self):
        pass


d = (i for i in range(99))

def func():
    for i in range(9):
        yield i
f= func()
if __name__ == '__main__':
    print(isinstance(A(), Iterator))  # False
    print(isinstance(A(), Iterable))  # True
    print(isinstance(B(), Iterator))  # False
    print(isinstance(B(), Iterable))  # False
    print(isinstance(C(), Iterator))  # True
    print(isinstance(C(), Iterable))  # True
    print(isinstance(d, Iterable))  # True
    print(isinstance(d, Iterable))  # True
    print(d)
    print(isinstance(f, Iterable))  # True
    print(isinstance(f, Iterable))  # True
    print(f)

"""
总结：
可迭代对象：实现了__iter__方法
迭代器:同时实现了__iter__和__next__
生成器也是迭代器
"""