#include <iostream>

struct Node
{
    int data;
    Node *link;
};

Node *head = NULL;

void InsertNode(int x);
void PrintNode();
void InsertNth(int x, int n);

void InsertNode(int x)
{
    Node *temp = new Node();

    temp->data = x;
    temp->link = head;

    head = temp;
}

void PrintNode()
{
    struct Node *temp = head;

    std::cout << "The list is: ";
    while (temp != NULL)
    {
        std::cout << temp->data << " ";
        temp = temp->link;
    }
}

int main(int argc, char const *argv[])
{
    std::cout << "How many numbers?" << std::endl;

    int n, i, x;

    std::cin >> n;

    while (n-- > 0)
    {
        std::cin >> x;
        InsertNode(x);
        PrintNode();
    }

    return 0;
}
