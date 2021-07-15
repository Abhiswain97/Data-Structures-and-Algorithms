#include<stdio.h>
#include<stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct node* newNode(int data){
    struct node *new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = data;
    return new_node;
}


int main(int argc, char const *argv[])
{
    return 0;
}
