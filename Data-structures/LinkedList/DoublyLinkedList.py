import random

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data: int):
        new_node = Node(data)

        self.head = new_node

        new_node.prev = self.head
        new_node.next = None
