def selectionSort(arr):
    for i in range(len(arr) - 1):
        imin = i
        for j in range(i + 1, len(arr)):
            print(j, imin)
            if arr[j] < arr[imin]:
                imin = j

        arr[i], arr[imin] = arr[imin], arr[i]


if __name__ == "__main__":
    arr = [5, 4, 6, 2, 7]

    print(arr)

    print(len(arr))

    selectionSort(arr)

    print(arr)
