"""
给定一组数，从中挑选出不相邻的一组数，使得值最大，求出最大值

arr=[1,2,4,1,7,8,3]

"""

"""
状态:f[i]代表从前i个数中挑选出的最佳方案所获得的最大值
递推:f[i] = max(f[i-1],f[i-2]+arr[i])
边界:f[0] = arr[0]
"""


arr=[1,2,4,1,7,8,3]


def func(arr):
    length = len(arr)

    f = [0 for _ in range(length)]
    f[0] = arr[0]
    for i in range(1,length):
        if i>=2:
            f[i] = max([f[i-1],f[i-2]+arr[i]])
        else:
            f[i] = max([f[i-1],arr[i]])
    print(f)
    return f[-1]


print(func(arr))