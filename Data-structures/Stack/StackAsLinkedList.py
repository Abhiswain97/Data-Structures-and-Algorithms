# Needs fixing

import random


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: None = None


class Stack:
    MAX_SIZE = 100

    def __init__(self):
        self.top = None
        self.size = Stack.MAX_SIZE

    def __len__(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        if self.top is None:
            return True
        else:
            return False

    def push(self, data: int) -> None:
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
            return

        new_node = self.top
        self.top = new_node

    def pop(self) -> None:
        if self.isEmpty():
            print("Stack is empty")
            return

        data = self.top.data
        self.top = self.top.next

        print(f"Popped {data}")

    def peek(self) -> None:
        print(f"Element at top: {self.top.data}")


if __name__ == "__main__":

    stack = Stack()

    for i in range(5):
        n = random.randint(0, 100)

        print(f"Pushing {n}")
        stack.push(n)

    stack.peek()
    stack.pop()
    stack.peek()
