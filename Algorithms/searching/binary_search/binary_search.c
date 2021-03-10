#include <stdio.h>

int binary_Search(int arr[], int l, int r, int key)
{
    while (l <= r)
    {
        int mid = (l + r) / 2;

        if (arr[mid] == key)
            return mid;

        else if (arr[mid] > key)
            l = mid - 1;

        else
            r = mid + 1;
    }

    return -1;
}

int main()
{
    int arr[] = {1, 3, 2, 0, 5, 4, -1};
    int key = 3, n = sizeof(arr) / sizeof(arr[0]);
    if (binary_Search(arr, 0, n - 1, key))
        printf("%d found at index %d\n", key, binary_Search(arr, 0, n - 1, key));
    else
        printf("%d not found", key);
    return 0;
}