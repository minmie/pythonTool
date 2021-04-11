"""

给定一组数和一个数，能否从这组数选出一个组合，使得其值等于给定的数?每个数字只能用一次
arr = [3,34,4,12,5,2]
num = 14
"""


"""

状态:f[i,j]表示从前i个数中能否凑出j
递推f[i,j] = f[i-1,j-arr[i]] or f[i-1,j]
边界:
f[0,:]=F and f[0,arr[0]]=T and f[0,0] = True

"""

arr = [3,34,4,12,5,2]
num = 14

def func(arr,num):

    f=[]
    for i in range(len(arr)):
        tmp=[]
        for j in range(num+1):
            if i == 0 and (j == arr[0] or j == 0):
                tmp.append(True)
            else:
                tmp.append(False)
        f.append(tmp)
    # print('-----------')
    for i in range(1,len(arr)):
        for j in range(num + 1):
            if arr[i] > j:
                # print('arr[i]=',arr[i],";j=",j)
                f[i][j] = f[i-1][j]
            else:
                f[i][j] = f[i-1][j-arr[i]] or f[i-1][j]
    # print(f)
    return f[-1][-1]


print(func(arr,9))
print(func(arr,10))
print(func(arr,11))
print(func(arr,12))
print(func(arr,13))
print(111111111111111)
# print(func(arr,4))
# # print(func(arr,5))
# # print(func(arr,9))
