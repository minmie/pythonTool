# 树的单个结点
class Node:
    def __init__(self,data):
        # 结点数据
        self.elem = data
        # 左子树和右子树
        self.lchild = None
        self.rchild = None


# 递归实现遍历
# 先序遍历
def pre_travel(root):
        if root is None:
            return
        print(root.elem)
        pre_travel(root.lchild)
        pre_travel(root.rchild)


# 中续遍历
def in_travel(root):
    if root is None:
        return
    pre_travel(root.lchild)
    print(root.elem)
    pre_travel(root.rchild)

# 后续遍历
def post_travel(root):
    if root is None:
        return
    pre_travel(root.lchild)
    pre_travel(root.rchild)
    print(root.elem)


# 求树的高度
# 二叉树的高度（深度）为二叉树中结点层次的最大值，也可视为其左、右子
# 树高度的最大值加 1。
def get_tree_depth(root):
    if root is not None:
        hl = get_tree_depth(root.lchild)
        hr = get_tree_depth(root.rchild)
        _max = hl if hl > hr else hr
        return _max + 1
    else:
        return 0



if __name__ == '__main__':

    # 定义节点
    tree = Node(1)
    node_2=Node(2)
    node_3=Node(3)
    node_4=Node(4)
    node_5=Node(5)
    node_6=Node(6)
    node_7=Node(7)

    # 构造树
    tree.lchild=node_2
    tree.rchild=node_3
    node_2.lchild = node_4
    node_2.rchild = node_5
    node_3.rchild = node_6
    node_3.rchild = node_7


    #求树的深度
    depth=get_tree_depth(tree)
    print('tree的深度=',depth)