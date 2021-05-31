import random


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BST:
    def Insert(self, root, data):
        new_node = Node(data)

        if root is None:
            root = new_node
            return

        if root.data >= data:
            root.left = self.Insert(root.left, data)
        else:
            root.right = self.Insert(root.right, data)
