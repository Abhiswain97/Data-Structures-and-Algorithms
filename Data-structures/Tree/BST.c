#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *left, *right;   
};

struct node* newNode(int data){
    struct node *temp = (struct node*)malloc(sizeof(struct node));
    temp->data = data;
    temp->left = temp->right = NULL;
    return temp;    
}

struct node* insert(struct node *root, int data){
    if(root == NULL){
        root = newNode(data);
    }
    else{
        if(data < root->data){
            if(root->left == NULL){
                root->left = newNode(data);
            }
            else{
                insert(root->left, data);
            }
        }
        else {
            if(root->right == NULL){
                root->right = newNode(data);
            }
            else{
                insert(root->right, data);
            }
        }       
    }
}

int search(struct node *root, int data){
    if(root == NULL) return 0;

    if(root->data == data) return 1;

    if(data < root->data){
        return search(root->left, data);
    }
    else{
        return search(root->right, data);
    }

    return 0;
}

void inorder_traversal(struct node *root){
    if(root == NULL)
        return;
    inorder_traversal(root->left);
    printf("%d ", root->data);
    inorder_traversal(root->right);    
}

int main(){
    struct node *root = newNode(1);
    int n, data;
    printf("Enter the number of elements to be inserted: ");
    scanf("%d", &n);
    printf("Enter the elements: ");
    for(int i = 0; i < n; i++){
        scanf("%d", &data);
        insert(root, data);
    }
    printf("Inorder traversal of the BST: ");
    inorder_traversal(root);
    printf("\nSearch for a node with value 5: %d", search(root, 5));
    return 0;    
}