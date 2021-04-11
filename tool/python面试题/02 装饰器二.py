"""
python装饰器本质上就是一个函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外的功能，装饰器的返回值也是一个函数对象

下面是装饰器的四种用法：

"""


# 一、函数装饰函数
import time
def timmer(flag):
    def wrapper(f):
        def inner(*args, **kwargs):
            print('f.__name__',f.__name__)
            if flag:
                start_time = time.time()
                ret = f(*args, **kwargs)
                end_time = time.time()
                print('执行时间%s' % (end_time-start_time))
                return ret
            else:
                ret = f(*args, **kwargs)
                return ret
        return inner
    return wrapper

# 第一步,将@ 与后面 分开,只是单纯的执行timmer(flag1)函数 第二部 将@ 与 wrapper相结合,形成装饰器,
# 等同于 func1=wrapper(func1) ，即func1=inner
flag1 = True
@timmer(flag1)
def func1():
    time.sleep(0.3)
    print('in func1')
func1()


# 二、类装饰函数
class Profiled:

    def __init__(self, func):
        # wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        print("call")
        return self.func(*args, **kwargs)


@Profiled # @Profiled等同于 add = Profiled(add),即add变成Profiled实例化的一个对象
def add(x, y):
    return x + y
result = add(1, 2)
print(result)


# 三、函数装饰类

def wrapClass(cls):
    def inner(*args, **kwargs):
        print('class name:', cls.__name__)
        return cls(*args, **kwargs)
    return inner

@wrapClass
class Foo:
    def __init__(self, a):
        self.a = a

    def fun(self):
        print('self.a =', self.a)

m = Foo('xiemanR')
m.fun()

# 四、类装饰类
class ShowClassName(object):
    def __init__(self, cls):
        self._cls = cls

    def __call__(self, a):
        print('class name:', self._cls.__name__)
        return self._cls(a)

@ShowClassName
class Foobar(object):
    def __init__(self, a):
        self.value = a

    def fun(self):
        print(self.value)

a = Foobar('xiemanR')
a.fun()