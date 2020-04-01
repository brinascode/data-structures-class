#Basic Node definition. Each Node contains a Value, a left child, and a right child
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value

#insert Value into the appropiate spot in the tree
def insert(root, node):
    if root is None:
        root=node
    elif root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)


def inorder_traversal(root):
    # finish code to print all values with an inorder traversal. Two ways: loops or recursion (easier)
    if root is not None:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)


bst = Node(5)
insert(bst,Node(2))
insert(bst,Node(7))
insert(bst,Node(10))
insert(bst,Node(4))
insert(bst,Node(1))

inorder_traversal(bst)