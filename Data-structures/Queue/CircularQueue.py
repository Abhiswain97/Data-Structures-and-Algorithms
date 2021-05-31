# More memory efficient as it utilises De-queued cells

import random
from typing import List


class CircularQueue:
    MAX_SIZE = 100

    def __init__(self):
        self.data: List[int] = [0] * CircularQueue.MAX_SIZE
        self.size: int = CircularQueue.MAX_SIZE
        self.front: int = -1
        self.rear: int = -1

    def __len__(self) -> int:
        return len(list(filter(lambda x: x != 0, self.data)))

    def isEmpty(self) -> bool:
        return self.front == -1 and self.rear == -1

    def isFull(self) -> bool:
        return ((self.rear + 1) % self.size) == self.front

    def push(self, data: int) -> None:
        if self.isFull():
            print("CircularQueue is full")
            return
        elif self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.data[self.rear] = data

    def pop(self) -> None:
        if self.isEmpty():
            print("CircularQueue is empty")
            return
        elif self.front == self.rear:
            print(f"Popped: {self.data[self.front]}")
            self.front = self.rear = -1
        else:
            print(f"Popped: {self.data[self.front]}")
            self.front = (self.front + 1) % self.size

    def Qfront(self) -> None:
        print(
            f"Element at front: {self.data[self.front]}"
        ) if self.front != -1 else print("CircularQueue is empty")

    def Qrear(self) -> None:
        print(f"Element at rear: {self.data[self.rear]}") if self.rear != -1 else print(
            "CircularQueue is empty"
        )


if __name__ == "__main__":

    Q: CircularQueue = CircularQueue()

    for i in range(5):
        n: int = random.randint(0, 100)

        print(f"Pushing {n} into CircularQueue")

        Q.push(n)

    Q.push(101)

    for i in range(4):
        Q.pop()

    Q.Qfront()
    Q.Qrear()

    print(f"No. of elements in Queue: {len(Q)}")
