"""
求两个列表的交集，元素可重复

a = [1,2,4,2]
b = [2,2]

"""

"""

"""

a = [1,2,4,2,3]
b = [2,2,3]
a.sort()
b.sort()
l_a = len(a)
l_b = len(b)
ret=[]
i,j =0, 0
while i <l_a and j<l_b:
    if a[i] == b[j]:
        ret.append(a[i])
        i +=1
        j +=1
    else:
        if a[i] >= b[j]:
            j += 1
        else:
            i += 1
print(ret)