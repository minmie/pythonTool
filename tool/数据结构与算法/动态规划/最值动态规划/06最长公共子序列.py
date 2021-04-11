
"""
给定2个序列，求最长公共子序列(必须是递增的选)

x=[a,b,c,b,d,a,b]
y=[b,d,c,a,b,a]
结果:baba
"""


"""
状态:f[i,j]代表在x序列的前i个中，y序列的前j个中，所能取得的最长公共子序列长度
递推：f[i,j]=max(f[i-1][j],f[i][j-1]) if xi !=yj else f[i-1][j-1]
边界:f[0][0] =0


状态:g[i][j]是标记函数
取值1：左   2 ：左上   3 ：上
"""

x=["a","b","c","b","d","a","b"]
y=["b","d","c","a","b","a"]
# x=["a","b","c"]
# y=["b",'c']

def func(x,y):


    # init
    f = []
    g = []
    for i in range(len(x)+1):
        temp = []
        temp2 = []
        for j in range(len(y)+1):
            temp2.append(None)
            if i is 0 or j is 0:
                temp.append(0)
            else:
                temp.append(-1)
        f.append(temp)
        g.append(temp2)

    for i in range(1,len(x)+1):
        for j in range(1,len(y) + 1):
            if x[i-1] == y[j-1]:
                f[i][j] = f[i-1][j-1] +1
                g[i][j] = 2
            elif f[i-1][j] >= f[i][j-1]:
                f[i][j] = f[i-1][j]
                g[i][j] = 3
            else:
                f[i][j] = f[i][j-1]
                g[i][j] = 1

    print(f[-1][-1])
    # print(f)  # 最长公共子序列的长度
    print(g)
    # 求出序列
    row = len(x)
    col = len(y)
    ret = []
    while row > 0 and col > 0:
        if g[row][col] == 1:
            col -= 1
        elif g[row][col] == 2:
            ret.append(x[row-1])
            row -= 1
            col -= 1
        else:
            row -= 1
    ret.reverse()
    print("".join(ret))
func(x,y)