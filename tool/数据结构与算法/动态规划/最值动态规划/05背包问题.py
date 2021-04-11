"""
有一个背包，可以放入n种物品，每种物品的重量和价值分别为wi和vi，如果背包的最大重量限制是b，每种物品可以放多个，怎样选择
放入背包的物品可以使背包的价值最大？设wi,vi,b都是正整数。

实例：
n=4
b=10
v=[1,3,5,9]
w=[2,3,4,7]

"""


"""
状态:f[k,y]代表装前k种物品，重量不超过y时所能达到的最大价值
递推:f[k,y]=max(f[k-1,y],f[k,y-w[k]]+v[k]) y >= w[k] or  f[k-1,y]
边缘条件:f[0,:]=0，f[:,0]=0


状态:index[k,y]代表装前k种物品，总重不超过y，背包达到最大价值时，装入物品的最大标号
递推:index[k,y]=index[k-1,y] if f[k-1,y] > f[k,y-w[k]]+v[k] else k
        f[k-1,y] > f[k,y-w[k]]+v[k]  说不装第K种物品比装了效果更好，所以index[k,y]与index[k-1,y] 取值一致
边界:index[0,y]= -1 if y < w else 0   ,-1代表啥也没装，0代表装了第0个序号的物品
"""

# n=4
b=10
v=[1,3,5,9]
w=[2,3,4,7]


def func(b,v,w):
    # init
    f=[]
    for row in range(len(v)):
        temp = []
        for col in range(b+1):
            if col is 0 :
                temp.append(0)
            elif row is 0:
                temp.append(int((col//w[row])*v[row]))
            else:
                temp.append(-1)
        f.append(temp)

    # 计算最优解
    for i in range(1,len(v)):
        for j in range(1,b+1):
            if j >= w[i]:
                f[i][j]= max([f[i-1][j],f[i][j-w[i]]+v[i]])
            else:
                f[i][j] = f[i-1][j]
    print(f[-1][-1])
    return f

def index_track(b,v,w):
    f = func(b,v,w)

    index= []
    for row in range(len(v)):
        temp = []
        for col in range(b+1):
            if row is 0:
                temp.append(-1 if col < w[0] else 0)
            else:
                temp.append(-1)
        index.append(temp)
    print(index)

    for i in range(1,len(v)):
        for j in range(b+1):
            if j >= w[i]:
                index[i][j] = index[i-1][j] if f[i-1][j] > f[i][j-w[i]] + v[i] else i
            else:
                index[i][j] = index[i - 1][j]
    print(index)
    i = len(v)-1
    weight = b
    result = []
    while 1:
        print('i=',i,';weight=',weight,'index=',index[i][weight])
        result.append(index[i][weight])
        i = index[i][weight]
        weight -= w[index[i][weight]]
        if index[i][weight] is -1:
            break

    print(result)  # 存的是物品的序号

if __name__ == '__main__':

    index_track(b,v,w)
