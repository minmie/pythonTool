import threading
from random import randint


def singleton(cls):
    cls.__lock__ = threading.Lock()
    def inner(*args, **kwargs):
        if not cls.instance:
            with cls.__lock__:
                cls.instance = cls(*args, **kwargs)
        return cls.instance
    return inner

@singleton
class Test:
    instance = None
    def __init__(self):
        self.b=randint(100,200)


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