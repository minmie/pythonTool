
"""
https://www.lintcode.com/problem/116/
有n块石子，青蛙在第i块石头上，最后能跳ai块石子，请问青蛙能否跳到最后一块石子

a=[2,3,1,1,4]  True
b=[3,2,1,0,4] False
"""

"""
状态：f[i]表示青蛙能否跳到第i块石头
递推方程：f[i] = or(f[j] and j+a[j] >= i) 0<=j<i
边界条件：
f[0]=True
"""

def func(arr:list):
    length = len(arr)
    f = [None for _ in range(length)]
    f[0] = True
    for i in range(1,length):
        f[i] = False
        for j in range(i):
            if f[j] and j+arr[j]>=i:
                f[i] = True
                break
    return f[-1]

class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        length = len(A)
        f = [None for _ in range(length)]
        f[0] = True
        for i in range(1, length):
            f[i] = False
            for j in range(i):
                if f[j] and j + A[j] >= i:
                    f[i] = True
                    break
        return f[-1]


print(func([2,3,1,1,4]))
print(func([3,2,1,0,4]))