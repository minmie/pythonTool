"""

如图
有n项任务，完成的花费时间和收益如图，给定一组任务，请问收益最大是多少。（不能同一时间做多个任务）

a=[(1,4,5),(3,5,1)]

"""

"""
状态f[i] 代表从前i项任务中挑任务做，最大所能获得的收益
递推:f[i] = max(f[i-1],f[prev(i)]+a[i])   要么做第i项，要么不做第i项，求两个中的大值
prev(i):代表如过做了第i项任务，那么还能从前prev(i)项任务中挑任务做
a=[5,1,8,4,6,3,2,4] 任务收益
prev = [0,0,0,1,0,2,3,5]  
边界:
f[1] = 5
f[0] = 0
"""
a=[5,1,8,4,6,3,2,4]
prev = [-1,-1,-1,0,-1,1,2,4]
def func():

    length = len(a)
    # init
    f = [-1 for _ in range(length)]
    f[0] = 5
    for i in range(1,length):
        try:
            if prev[i] != -1:
                f[i] = max([f[i - 1], f[prev[i]]+ a[i]])
            else:
                f[i] = max([f[i - 1], a[i]])
            print(f[i])
        except:
            print(i)

    print(f)

if __name__ == '__main__':
    func()