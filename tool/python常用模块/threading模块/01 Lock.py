from threading import Thread, Lock
import time

n = 1
lock = Lock()

def func1():
    global n
    lock.acquire()
    n += 1
    print('func1',n)
    time.sleep(3)
    lock.release()

def func2():
    global n
    lock.acquire()
    n = n*n
    print('func2', n)
    lock.release()

if __name__ == '__main__':

    t1 = Thread(target=func1)
    t2 = Thread(target=func2)
    t1.start()
    t2.start()

    t2.join()
    print('main',n)
