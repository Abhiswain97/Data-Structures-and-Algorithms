# From: https://stackoverflow.com/questions/5444394/how-to-implement-a-binary-search-tree-in-python
import random

# Create a binary search tree


class BST:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val: int = val

    def __str__(self) -> str:
        return "%s: [%s, %s]" % (str(self.val), self.left, self.right)

    def isEmpty(self) -> bool:
        return self.left == self.right == self.val == None

    def insert(self, val: int) -> None:
        if self.isEmpty():
            self.val = val
        elif val < self.val:
            if self.left is None:
                self.left = BST(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BST(val)
            else:
                self.right.insert(val)

    def search(self, key):
        if not self:
            return None
        if self.val == key:
            return True
        elif self.val > key:
            self.left.search(key=key)
        else:
            self.right.search(key)


if __name__ == "__main__":
    bst = BST(1)
    for i in range(10):
        val = random.randint(0, 100)
        bst.insert(val)

    print(bst)

    print(bst.search(2))
