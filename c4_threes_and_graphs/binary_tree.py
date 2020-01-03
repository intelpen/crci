# BinaryTree property all_left < node < all_right

class BTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def visit(node):
    print(node.data)
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        visit(node)
        in_order_traversal(node.roght)

#S