#include <stdio.h>

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

int binary_Search(int arr[], int l, int r, int key)
{
    while (l <= r)
    {
        int mid = (l + r) / 2;

        if (arr[mid] == key)
            return mid;

        else if (arr[mid] > key)
            r = mid - 1;

        else
            l = mid + 1;
    }

    return -1;
}

int main()
{
    int arr[] = {1, 3, 2, 0, 5, 4, -1};
    int key = 4, n = sizeof(arr) / sizeof(arr[0]);

    insertionSort(arr, n);

    if (binary_Search(arr, 0, n - 1, key))
        printf("%d found at index %d\n", key, binary_Search(arr, 0, n - 1, key));
    else
        printf("%d not found", key);
    return 0;
}