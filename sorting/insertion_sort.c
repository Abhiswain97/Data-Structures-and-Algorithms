#include <stdio.h>

void print(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    printf("\n");
}

void insertionSort(int a[], int n)
{
    int key, j;
    for (int i = 1; i < n; i++)
    {
        key = a[i];
        j = i - 1;

        while (j >= 0 && a[j] > key)
        {
            a[j + 1] = a[j];

            j--;
        }

        a[j + 1] = key;
    }
}

int main()
{
    int a[] = {1, 3, 2, 0, 5, 4, -1};

    int n = sizeof(a) / sizeof(a[0]);

    print(a, n);

    insertionSort(a, n);

    print(a, n);

    return 0;
}