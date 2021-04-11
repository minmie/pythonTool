

"""
有2 , 5 ,7 三种硬币，拼出27最少用几枚硬币

"""

"""
状态：f[i]代表拼出i最少需要用的硬币数
递推:f[i]=min(f[i-7]+1,f[i-5]+1,f[i-2]+1)
f[0]=0
f[i<0]=无穷大
"""

arr=[2,5,7]
sum = 27
MAX_NUM = 99999

def func():
    f=[MAX_NUM for _ in range(sum+1)]
    f[0] = 0
    for i in range(1,sum+1):
        for j in arr:
            if i>=j and f[i-j] != MAX_NUM:
                f[i] = min([f[i],f[i-j]+1])

    print(f)

func()