import timeit
import time


#1. 使用is比较布尔值
# print(timeit.timeit('3 is True', number=100000))  # 0.001767799999999986
# print(timeit.timeit('3 == True', number=100000))  # 0.002581900000000026


# 2. 对于and，应该把满足条件少的放在前面，对于or，把满足条件多的放在前面


# 3. in 的效率比find高
# print(timeit.timeit('char in text', setup='text = "sample string"; char = "g"'))  # 0.03681910000000005
# print(timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"'))  # 0.1478601


# 4. 使用加法拼接字符串最快，其次是%s
# print(timeit.timeit("'abc%s%s' % (s1, s2)", setup="s1, s2 = 'ax', 'bx'", ))  # 0.21390569999999998
# print(timeit.timeit("'abc{0}{1}'.format(s1, s2)", setup="s1, s2 = 'ax', 'bx'", ))  # 0.26528909999999994
# print(timeit.timeit("'abc' + s1 + s2", setup="s1, s2 = 'ax', 'bx'",))  # 0.08197680000000007

# 5. 不借助中间变量交换两个变量的值



# 6. while 1 比 while True 速度快
# def while_1():
#     n = 10000000
#     while 1:
#         n -= 1
#         if n <= 0: break
#
# def while_true():
#     n = 10000000
#     while True:
#         n -= 1
#         if n <= 0: break
#
# print(timeit.timeit("while_1()", setup="from __main__ import while_1",number=1))
# print(timeit.timeit("while_true()", setup="from __main__ import while_true", number=1))



# 7.提前将方法赋值给变量，会加快运行速度
# def f1():
#     upper = str.upper
#     li = []
#     append =li.append
#     for i in range(10000000):
#         append(upper('asdfxz'))
#
#
# def f2():
#     li = []
#     for i in range(10000000):
#         li.append('asdfxz'.upper())
#
# print(timeit.timeit("f1()", setup="from __main__ import f1",number=1))  # 1.3080634
# print(timeit.timeit("f2()", setup="from __main__ import f2", number=1))  # 1.491859



#8. -5~256的整数比较用 is来

# print(timeit.timeit("a+b==6", setup="a, b = 2,4", ))  # 0.06123479999999998
# print(timeit.timeit("a+b is 6", setup="a, b = 2,4", ))  # 0.04260600000000003


# 9
# arr = [None for _ in range(1000000)]  # 速度慢
# arr = [None] * 1000000    #速度更快
# def f1():
#     arr = [None for _ in range(1000000)]
#
#
#
# def f3():
#     arr = [None] * 1000000
#     # for i in range(1000000):
#     #     arr[i]=[i]
#
# print(timeit.timeit("f1()", setup="from __main__ import f1",number=1))  # 0.04370669999999999
# print(timeit.timeit("f3()", setup="from __main__ import f3", number=1))  # 0.004238999999999993