#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
from random import randint
import time

def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)
    return synced_func


class MyThread(threading.Thread):

    def __init__(self,func,args=()):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None


def worker():
    single_test = Test()
    # a=[1,'abc']
    print("id----> %s,b=%s" % (id(single_test),single_test.b))
    return single_test

class Test:
    instance=None

    @synchronized # 去掉的话就不是线程安全
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            time.sleep(0.5) # 加这一句是为了可以更方方便的看出错误
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self):
        self.b=randint(100,200)

if __name__ == "__main__":
    task_list = []
    for one in range(30):
        t = MyThread(func=worker)
        task_list.append(t)

    for one in task_list:
        one.start()

    for one in task_list:
        one.join()

    for one in task_list:
        print(one.result.b)