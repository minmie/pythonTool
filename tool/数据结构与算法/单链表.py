class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def is_empty(self):
        return False if self.head  else True

    # @property
    def get_length(self):
        return self.length

    def travel(self):
        cur = self.head
        while cur:
            print(cur.data,end=', ')
            cur = cur.next

    # 尾插发添加节点
    def append(self,data):
        node = Node(data)
        self.length += 1
        # 如果是空链表
        if self.is_empty():
            self.head = node
            self.tail = node
        else: # 如果链表原本已经有数据
            self.tail.next = node
            self.tail = node

    # 头插法添加节点
    def add_from_head(self,data):
        node = Node(data)
        self.length += 1
        # 如果是空链表
        if self.is_empty():
            self.head = node
            self.tail = node
        else:  # 如果链表原本已经有数据
            node.next = self.head
            self.head = node

    # 在指定位置添加节点

    def insert(self,pos,data):
        node = Node(data)

        if pos < 1 :
            self.add_from_head(data)
        elif pos > self.length:
            self.append(data)
        else:
            cur = self.head
            count = 1
            while count < pos-1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node
            self.length += 1

    # 按值查找节点,返回索引
    def search(self,data):
        cur = self.head
        count = 1
        while cur != None:

            if cur.data == data:
                return count
            count += 1
            cur = cur.next
        return None

    def remove(self,data):

        # 如果删除的数据在第一个节点
        # if not self.is_empty() and self.head.data == data :
        #     self.head = self.head.next
        #     self.length -= 1

        cur = self.head
        pre = None

        while cur != None:
            self.length -= 1
            if cur.data == data:
                if self.head == cur:
                    self.head = cur.next
                else:
                    pre.next = cur.next
            pre = cur
            cur = cur.next


if __name__ == '__main__':
    l = SingleLinkList()
    print(l.is_empty())
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    print(l.get_length())
    # 验证insert
    l.travel()
    print()
    l.insert(5,33)
    l.insert(7,22)
    l.append(44)
    print('------',l.get_length())
    l.travel()

    # 验证search
    print()
    print('验证search')
    l.travel()
    print()
    print(l.search(333))

    # 验证remove
    print()
    l.append(3)
    print('验证remove')
    l.travel()
    print()
    l.remove(3)
    l.travel()
    print()