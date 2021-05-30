import random


class Stack:
    def __init__(self, size):
        self.data = [0] * size
        self.top = -1
        self.size = size

    def push(self, data):
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
    stack = Stack(5)

    for i in range(5):
        n = random.randint(0, 100)

        print(f"Pushing {n}")

        stack.push(n)

    stack.pop()
    stack.pop()

    stack.peek()
