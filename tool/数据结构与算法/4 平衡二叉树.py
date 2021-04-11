


# 树的单个结点
class Node:
    def __init__(self,data):
        # 结点数据
        self.key = data
        # 左子树和右子树
        self.lchild = None
        self.rchild = None

    # 先序遍历
def pre_travel(root):
    # pre_travel(root)
    if root is None:
        print(1111)
        return
    print(root.key)
    pre_travel(root.lchild)
    pre_travel(root.rchild)

# 求树的高度
# 二叉树的高度（深度）为二叉树中结点层次的最大值，也可视为其左、右子
# 树高度的最大值加 1。
# 中序遍历一个二叉排序树，可以得到一个递增有序序列
class AVLTree:
    """
    平衡二叉排序树（平衡二叉搜索树）
    """
    def __init__(self):
        self.root = None

    @classmethod
    def __f(cls,node):
        if node is not None:
            hl = cls.__f(node.lchild)
            hr = cls.__f(node.rchild)
            max = hl if hl > hr else hr
            return max + 1
        else:
            return 0
    # 求二叉树的深度
    def get_depth(self):
        d = self.__f(self.root)
        return d
    @classmethod
    def __f2(cls,node):
        hl=0
        hr=0
        if node != None:
            if node.lchild == None and node.rchild == None:
                return 1
            hl = cls.__f2(node.lchild)
            hr = cls.__f2(node.rchild)
            # if node.lchild == None and node.rchild == None:
            #     return hl+hr+1
        else:
            return 0
        return hl+hr+1
    # 求二叉树的节点个数
    def count_node(self):
        n = self.__f2(self.root)
        return n


    def __dlr_handler(self,node):
        if node is None:
            return
        print(node.key,end=',')
        self.__dlr_handler(node.lchild)
        self.__dlr_handler(node.rchild)

    # 先序遍历
    def dlr_travel(self):
        print('先序遍历：',end='')
        self.__dlr_handler(self.root)
        print()

    def __ldr_handler(self,node):
        if node is None:
            return
        self.__ldr_handler(node.lchild)
        print(node.key,end=',')
        self.__ldr_handler(node.rchild)

    # 中序遍历
    def ldr_travel(self):
        print('中序遍历：', end='')
        self.__ldr_handler(self.root)
        print()

    # 从键盘接收一个数，并且插入树当中
    def create_bst(self):

        key = input('输入key:')
        while key != '':
            if self.root:

                self.insert_node(self.root,int(key))
            else:
                self.root=Node(int(key))
            key = input('输入key:')
        print('输入结束')

    # 插入节点
    @classmethod
    def insert_node(cls,node,key):

        if key < node.key :
            # cls.insert_node(node.lchild, key)
            if node.lchild:
                cls.insert_node(node.lchild,key)
            else:
                node.lchild = Node(key)
        elif key > node.key :
            # cls.insert_node(node.rchild, key)
            if node.rchild:
                cls.insert_node(node.rchild,key)
            else:
                node.rchild = Node(key)


    # 二叉搜索
    def search_bst(self,key):
        return  self._search_bst(self.root,key)

    def _search_bst(self,node,key):
        if node is None:
            print('查不到')
            return
        if node.key == key:
            print('查找成功',node.key)
            return node
        elif key < node.key:
            return  self._search_bst(node.lchild,key)
        else:
            return  self._search_bst(node.rchild,key)

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)

            else:
                currentNode.leftChild = Node(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = Node(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return

    def rotateLeft(self,rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
            newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rebalance(self,node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)