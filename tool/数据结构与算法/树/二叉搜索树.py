
"""
二叉搜索树，又叫二叉查找树，二叉排序树
特点：
左子树的值小于根节点，右子树的值大于根节点

课程地址:https://www.icourse163.org/learn/ZJU-93001?tid=1207006212#/learn/content?type=detail&id=1212031635&cid=1215166214&replay=true

"""

class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value

# 递归查找
def find(value, bst):
    if not bst: return None
    if value > bst.value:
        return find(value, bst.right)
    elif value < bst.value:
        return find(value, bst.left)
    else:
        return bst

# 迭代查找
def iter_find(value, bst):
    while bst:
        if value > bst.value:
            bst = bst.right
        elif value < bst.value:
            bst = bst.left
        else:
            return bst


# 深度优先遍历-递归遍历
def pre_travel(bst):
    """
    先序遍历
    :param bst:
    :return:
    """
    if bst:
        print(bst.value, end=' ')
        pre_travel(bst.left)
        pre_travel(bst.right)


def in_travel(bst):
    """
    中序遍历
    :param bst:
    :return:
    """
    if bst:
        in_travel(bst.left)
        print(bst.value, end=' ')
        in_travel(bst.right)

def post_travel(bst):
    """
    后续遍历
    :param bst:
    :return:
    """
    if bst:
        post_travel(bst.left)
        post_travel(bst.right)
        print(bst.value, end=' ')

# 深度优先遍历——栈的递归消除

def pre_travel_stack(bst):
    stack = []
    while bst or stack:
        while bst:
            print(bst.value, end=' ')
            stack.append(bst)
            bst = bst.left

        if stack:
            bst = stack.pop()
            bst = bst.right



def in_travel_stack(bst):
    stack = []
    while bst or stack:
        while bst:
            stack.append(bst)
            bst = bst.left

        if stack:
            bst = stack.pop()
            print(bst.value, end=' ')
            bst = bst.right

def post_travel_stack(bst):
    stack = []
    q = None
    p = bst
    while p or stack:
        while p:
            stack.append(p)
            p = p.left

        if stack:
            p = stack[-1]
            if p.right is None or p.right is q:
                print(p.value, end=' ')
                stack.pop()
                q = p
                p = None
            else:
                p = p.right



def level_travel(bst):
    queue = [bst]
    while queue:
        node = queue.pop(0)
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# 最大值在最右边，最小值在最左边
def find_max(bst):
    if not bst: return None
    while bst.right:
        bst = bst.right
    return bst.value

def find_min(bst):
    if not bst: return None
    while bst.left:
        bst = bst.left
    return bst.value



def insert(value, bst):
    if not bst:
        bst = Node(value)
    elif value < bst.data:
        bst.left = insert(value, bst.left)
    elif value > bst.data:
        bst.right = insert(value, bst.right)

    return bst





def delete(value, bst):
    """
    BinTree Delete( BinTree BST, ElementType X )
{
    Position Tmp;

    if( !BST )
        printf("要删除的元素未找到");
    else {
        if( X < BST->Data )
            BST->Left = Delete( BST->Left, X );   /* 从左子树递归删除 */
        else if( X > BST->Data )
            BST->Right = Delete( BST->Right, X ); /* 从右子树递归删除 */
        else { /* BST就是要删除的结点 */
            /* 如果被删除结点有左右两个子结点 */
            if( BST->Left && BST->Right ) {
                /* 从右子树中找最小的元素填充删除结点 */
                Tmp = FindMin( BST->Right );
                BST->Data = Tmp->Data;
                /* 从右子树中删除最小元素 */
                BST->Right = Delete( BST->Right, BST->Data );
            }
            else { /* 被删除结点有一个或无子结点 */
                Tmp = BST;
                if( !BST->Left )       /* 只有右孩子或无子结点 */
                    BST = BST->Right;
                else                   /* 只有左孩子 */
                    BST = BST->Left;
                free( Tmp );
            }
        }
    }
    return BST;
}
    :param value:
    :param bst:
    :return:
    """
    pass


if __name__ == '__main__':

    """
               30
         /          \
        15          40
       /   \      /   \
     7     16    35   45
    """

    node7 = Node(value=7)
    node16 = Node(value=16)
    node35 = Node(value=35)
    node45 = Node(value=45)
    node40 = Node(value=40)
    node15 = Node(value=15)
    bst = Node(value=30)
    bst.left = node15
    bst.right = node40
    node15.left = node7
    node15.right = node16
    node40.left = node35
    node40.right = node45
    bst.left = node15
    bst.right = node40

    pre_travel(bst)
    print()
    pre_travel_stack(bst)
    print('*' * 50)

    in_travel(bst)
    print()
    in_travel_stack(bst)
    print('*'*50)

    post_travel(bst)
    print()
    post_travel_stack(bst)
    print('*' * 50)

    level_travel(bst)  # 30 15 40 7 16 35 45

