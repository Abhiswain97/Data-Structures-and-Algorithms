import random


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: None = None
        self.prev: None = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, data: int):
        new_node: Node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head

        self.head = new_node

    def insertAtTail(self, data: int):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        prev = self.head
        temp = prev.next

        while temp:
            temp = temp.next
            prev = prev.next

        prev.next = new_node
        new_node.prev = prev

    def insertafterNth(self, data: int, n: int):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        prev = self.head
        current = prev.next

        i = 0

        while current:
            if i == n:
                prev.next = new_node
                new_node.prev = prev

                current.prev = new_node
                new_node.next = current

                break

            prev = prev.next
            current = current.next

            i += 1

    def deleteAtHead(self):
        pass

    def deleteAtTail(self):
        pass

    def deleteAfterNth(self):
        pass

    def print_list(self):
        temp = self.head
        print("The list is: ", end="")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == "__main__":
    dll: DoublyLinkedList = DoublyLinkedList()

    for i in range(5):
        n = random.randint(0, 100)

        print(f"Inserting {n} at the head \n")

        dll.insertAtHead(n)
        dll.print_list()

    for i in range(5):
        n = random.randint(0, 100)

        print(f"Inserting {n} at the tail \n")

        dll.insertAtTail(n)
        dll.print_list()

    dll.insertafterNth(101, 1)
    dll.print_list()
