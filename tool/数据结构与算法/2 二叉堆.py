
# 二叉堆是一个特殊的满二叉树
# 基于最小根堆
# 堆定义：父节点的key小于左右子节点的key
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # 节点插入后重新调整列表使其满足堆定义
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]

                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    # 插入节点
    def insert(self, k):
        self.heapList.append(k)

        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)

            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2

        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1


    # 取出根元素
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop(self.currentSize)
        self.currentSize = self.currentSize - 1
        self.percDown(1)
        return retval


    def buildHeap(self, alist):
        i = len(alist) // 2

        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def heap_sort(self):
        from copy import deepcopy
        heaplist=deepcopy(self.heapList) # 保护原有数据
        #堆排序操作
        while self.currentSize >= 2:
            root_val = self.delMin() #取出跟元素
            # print(root_val)
            self.heapList.insert(self.currentSize+1,root_val) # 将跟元素出入尾部
            # print(self.heapList)
        temp= self.heapList

        # 恢复之前的数据
        self.heapList=heaplist
        self.currentSize=len(self.heapList)-1
        return temp

if __name__ == '__main__':
    a = [9,8,7,6,5,4]
    heap=BinHeap()
    heap.buildHeap(a)
    print(heap.heapList)
    # heap.insert(1)
    # print(heap.heapList)
    print('堆排序的结果：',heap.heap_sort())
    print('原堆',heap.heapList)
    print('堆排序的结果2：', heap.heap_sort2())
    print('原堆', heap.heapList)