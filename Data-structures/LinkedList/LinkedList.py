import random

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBegin(self, data: int):
        temp = Node(data)
        temp.link = self.head
        self.head = temp

    def insertEnd(self, data: int):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        
        while temp.link:
            temp = temp.link

        temp.link = new_node

    def insertafterNth(self, data: int, n: int):

        if self.head is None:
            self.insertBegin()
            return

        temp = self.head

        i = 1

        while temp.link:
            if i == n:
                new_node = Node(data)
                new_node.link = temp.link
                temp.link = new_node

            temp = temp.link

            i += 1

    def deleteBegin(self):
        temp = self.head
        temp = temp.link

        self.head = temp

        del temp

        self.print_list()

    def deleteEnd(self):
        prev = self.head
        temp = prev.link

        while temp.link:
            temp = temp.link
            prev = prev.link

        prev.link = None

        del prev, temp

        self.print_list()

    def deleteAfterNth(self, n: int):
        prev = self.head
        temp = prev.link

        i = 1

        while temp.link:
            if i == n:
                prev.link = temp.link
                temp.link = None

                del temp, prev
                break

            temp = temp.link
            prev = prev.link

            i += 1

        self.print_list()

    def reverse(self):
        prev, curr = None, self.head

        while curr:
            next = curr.link
            curr.link = prev
            prev = curr
            curr = next

        self.head = prev

        self.print_list()

    def reverse_recursive(self, curr, prev):
        next = curr.link
        curr.link = prev
        
        self.reverse_recursive(next, curr)

    def reverse_print(self, curr):
        if curr is not None:
            return

        self.reverse_print(curr.link)
        print(curr.data, end=' ')

    def print_list(self):
        temp = self.head 
        print("The list is: ", end='')   
        while temp:
            print(temp.data, end=' ')
            temp = temp.link
        print()

    def __len__(self):
        temp = self.head 
        c = 0   
        while temp:
            c += 1
            temp = temp.link
        return c



if __name__ == '__main__':
    
    ll = LinkedList()
    
    for i in range(5):
        n = random.randint(0, 100)

        print(f"Inserting {n} at the beginning \n")

        ll.insertBegin(n)
        ll.print_list()

    ll.insertafterNth(400, 3)

    for i in range(3):
        n = random.randint(0, 100)

        print(f"Inserting {n} at the end \n")

        ll.insertEnd(n)
        ll.print_list()

    ll.deleteBegin()
    ll.deleteBegin()

    ll.deleteEnd()

    ll.deleteAfterNth(3)

    print(len(ll))



    