# Standard Queue

import random
from typing import List


class Queue:
    MAX_SIZE: int = 100

    def __init__(self):
        self.data: List[int] = [0] * Queue.MAX_SIZE
        self.size: int = Queue.MAX_SIZE
        self.front: int = -1
        self.rear: int = -1

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def isFull(self):
        return self.rear == (self.size - 1)

    def push(self, data: int):
        if self.isFull():
            print("Queue is full")
            return
        elif self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear += 1

        self.data[self.rear] = data

    def pop(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        elif self.front == self.rear:
            print(f"Popped: {self.data[self.front]}")
            self.front = self.rear = -1
        else:
            print(f"Popped: {self.data[self.front]}")
            self.front += 1

    def Qfront(self):
        print(
            f"Element at front: {self.data[self.front]}"
        ) if self.front != -1 else print("Queue is empty")

    def Qrear(self):
        print(f"Element at rear: {self.data[self.rear]}") if self.rear != -1 else print(
            "Queue is empty"
        )


if __name__ == "__main__":

    Q: Queue = Queue()

    for i in range(5):
        n = random.randint(0, 100)

        print(f"Pushing {n} into queue")

        Q.push(n)

    for i in range(4):
        Q.pop()

    Q.Qfront()
    Q.Qrear()
