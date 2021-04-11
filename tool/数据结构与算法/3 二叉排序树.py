# 二叉排序树又称为二叉查找树，它是一种特殊的二叉树。
# 其定义为：二叉树排序树或者是一棵空树，或者是具有如下性质的二叉树：
# （1）若它的左子树非空，则左子树上所有结点的值均小于根结点的值；
# （2）若它的右子树非空，则右子树上所有结点的值均大于（或大于等于）根结点的值；
# （3）它的左右子树也分别为二叉排序树。


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
class BSTree:
    """
    二叉排序树（二叉搜索树）
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
    # 求满二叉树的节点个数
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

if __name__ == '__main__':

    bstree=BSTree() # 创建一颗空的二叉排序树
    # 插入节点
    bstree.create_bst()
    bstree.ldr_travel()
    bstree.dlr_travel()

    ret=bstree.search_bst(11)
    # print(ret.key)
    print('节点个数=',bstree.count_node())
    print('树的深度=',bstree.get_depth())