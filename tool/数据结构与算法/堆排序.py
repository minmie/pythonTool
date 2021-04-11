def rebuild_heap(array,first,last):
    """
    :param array: 待排序数组
    :param first: 数组第一个元素的索引
    :param last: 数组最后一个元素的索引
    :return:
    """
    x=array[first]
    i=first+1  # 二叉树中的索引
    j=2*i  # 二叉树中索引
    finish=False
    while j-1<=last and not finish:
        if j-1<last and array[j-1]<array[j]:
            j += 1
        if x>array[j-1]:
            finish=True
        else:
            array[i-1]=array[j-1]
            i=j
            j=2*i
    array[i-1]=x
    # return array

def create_heap(array,length):
    """
    :param array:
    :param length: 数组长度
    :return:
    """
    n=length
    i=int(n/2) # 二叉树中的序号
    while i:
        rebuild_heap(array,i-1,length-1)
        i -=1

def heap_sort(array,length):
    create_heap(array,length)
    i=length
    while i>=2:
        array[0],array[i-1]=array[i-1],array[0]
        rebuild_heap(array,0,i-2)
        i -= 1

if __name__ == '__main__':
    li=[9,8,7,6,5,4,3,2,1]
    # li=[1,2,3,4]
    heap_sort(li,len(li))
    print(li)