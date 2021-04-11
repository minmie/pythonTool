# 树的单个结点
class Node:
    def __init__(self, data):
        # 结点数据
        self.elem = data
        # 左子树和右子树
        self.child = []



class MyTree:
    def __init__(self):
        self.root = None

    # 树添加元素，广度遍历 + 队列
    def add(self, item):
        # 创建新结点
        node = Node(item)
        # 特殊情况
        if self.root is None:
            self.root = node
            return
        else:
            # 队列的方式实现，队列最开始存根
            queue = [self.root]
            # 循环处理队列，直到将新结点添加进树为止
            while queue:
                # 取出第一个未处理的结点
                cur_node = queue.pop(0)
                # 判断取出的结点有没有左或右
                # 左结点是空，则添加新结点
                if cur_node.lchild is None:
                    cur_node.lchild = node
                    return
                else:
                    # 左结点不是空，则将左结点添加进队列
                    queue.append(cur_node.lchild)
                if cur_node.rchild is None:
                    cur_node.rchild = node
                    return
                else:
                    queue.append(cur_node.rchild)

    def tree_travle(self):
        if self.root is None:
            return
        else:
            # 队列先存根结点
            queue = [self.root]
            while queue:
                # 取第一个未处理的结点
                cur_node = queue.pop(0)
                print(cur_node.elem, end=' ')
                if cur_node.lchild is not None:
                    queue.append(cur_node.lchild)
                if cur_node.rchild is not None:
                    queue.append(cur_node.rchild)

    @classmethod
    def f(cls, node):
        if node != None:
            hl = cls.f(node.lchild)
            hr = cls.f(node.rchild)
            max = hl if hl > hr else hr
            return max + 1
        else:
            return 0

    # 求二叉树的深度
    def get_depth(self):
        d = self.f(self.root)
        return d

    @classmethod
    def f2(cls, node):
        hl = 0
        hr = 0
        if node != None:
            hl = cls.f2(node.lchild)
            hr = cls.f2(node.rchild)
            if node.lchild == None and node.rchild == None:
                return hl + hr + 1
        return hl + hr

    def count_leaf(self):
        n = self.f2(self.root)
        return n

    def __dlr_handler(self, node):
        if node is None:
            return
        print(node.elem)
        self.__dlr_handler(node.lchild)
        self.__dlr_handler(node.rchild)

    # 先序遍历
    def dlr_travel(self):
        self.__dlr_handler(self.root)


if __name__ == '__main__':
    #
    # tree = MyTree()
    # for i in range(2**8-1):
    #     tree.add(i)
    # # tree.tree_travle()
    # print()
    # # print(tree.root.lchild.elem)
    # print('深度',tree.get_depth())
    # print('叶子节点数',tree.count_leaf(),'真实数目',2**(8-1))
    # -------------------先序遍历测试
    tree = MyTree()
    # for i in range(1,4):
    #     tree.add(i)
    tree.add(2)
    tree.add(1)
    tree.add(3)
    # tree.dlr_travel()
