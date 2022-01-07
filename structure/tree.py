
# 定义子节点
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 定义树结构
class Tree():
    def __init__(self, root=None):
        self.root = root

    # 判断受否为空
    def isEmpty():
        return self.root == None

    # 树的总节点数
    def numNode(self, root):
        if not root:
            return 1
        res = numNode(root.left) + numNode(root.right)
        return res

