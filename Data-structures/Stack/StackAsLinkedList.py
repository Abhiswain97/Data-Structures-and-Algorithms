import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, size):
        self.top = None
        self.size = size

    def __len__(self):
        return self.size

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def push(self, data: int):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
            return

        new_node = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return

        data = self.top.data
        self.top = self.top.next

        print(f"Popped {data}")

    def peek(self):
        print(f"Element at top: {self.top.data}")


if __name__ == '__main__':

    stack = Stack(4)

    for i in range(5):
        n = random.randint(0, 100)

        print(f"Pushing {n}")
        stack.push(n)

    stack.peek()
    stack.pop()
    stack.peek()
