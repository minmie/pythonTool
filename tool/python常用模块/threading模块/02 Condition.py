from threading import Condition,Event,Lock,Thread
import time

l=Lock()
# help(type(l))
condition = Condition(l)


def func1():
    time.sleep(5)
    print(111)
    condition.acquire()
    print(222)
    condition.notify_all()
    print(333)
    condition.release()


if __name__ == '__main__':


    t1 = Thread(target=func1)

    t1.start()

    print('aa')
    condition.acquire()
    print('bb')
    w=condition.wait()
    print('w',w)
    print('cccc')
    condition.release()