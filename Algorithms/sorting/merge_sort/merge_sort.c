#include <stdio.h>
#include <limits.h>

void merge(int arr[], int start, int mid, int end)
{

    int n1 = mid - start + 1, n2 = end - mid;

    int L[100], R[100];

    for (int i = 0; i < n1; i++)
    {
        L[i] = arr[start + i];
    }

    for (int j = 0; j < n2; j++)
    {
        R[j] = arr[mid + 1 + j];
    }

    int i = 0, j = 0, k = start;

    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n1)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int start, int end)
{

    int mid;

    if (start < end)
    {
        mid = (start + end) / 2;

        mergeSort(arr, start, mid);
        mergeSort(arr, mid + 1, end);

        merge(arr, start, mid, end);
    }
}

void print(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    printf("\n");
}

int main()
{

    int arr[] = {1, 3, 2, 0, 5, 4, -1};

    mergeSort(arr, 0, sizeof(arr) / sizeof(arr[0]));

    print(arr, sizeof(arr) / sizeof(arr[0]));

    return 0;
}