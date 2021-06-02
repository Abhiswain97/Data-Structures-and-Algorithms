import random
from typing import List


class Stack:
    MAX_SIZE = 100

    def __init__(self):
        self.data: List[int] = [0] * Stack.MAX_SIZE
        self.top: int = -1
        self.size: int = Stack.MAX_SIZE

    def push(self, data: int):
        if self.top == (self.size - 1):
            print("Stack Overflow")
            return

        self.top += 1

        self.data[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        data = self.data[self.top]
        self.top -= 1
        print(f"Popped: {data}")

    def peek(self):
        print(f"Element at top: {self.data[self.top]}")


if __name__ == "__main__":
    stack: Stack = Stack()

    for i in range(5):
        n = random.randint(0, 100)

        print(f"Pushing {n}")

        stack.push(n)

    stack.pop()
    stack.pop()

    stack.peek()
