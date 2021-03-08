#include <stdio.h>

int linearSearch(int arr[], int key, int n)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == key)
            return i;
    }
    return -1;
}

int main()
{
    int arr[] = {1, 3, 2, 0, 5, 4, -1};
    int key = 3, n;
    if (linearSearch(arr, key, n))
        printf("%d found at index %d\n", key, linearSearch(arr, key, n));
    else
        printf("%d not found", key);
    return 0;
}