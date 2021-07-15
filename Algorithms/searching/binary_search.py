def recBinarySearch(arr, l, r, key):

    if l <= r:
        mid = (l + r) // 2
        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            return recBinarySearch(arr, l, mid - 1, key)

        else:
            return recBinarySearch(arr, mid + 1, r, key)

    else:
        return -1


def iterBinarySearch(arr, l, r, key):

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            r = mid - 1

        else:
            l = mid + 1

    return -1


if __name__ == "__main__":

    a = [1, 3, 2, 0, 5, 4, -1]

    key = 3

    a.sort()

    print(
        f"{key} found at index {recBinarySearch(a, 0, len(a)-1, key) - 1}"
    ) if recBinarySearch(a, 0, len(a) - 1, key) != -1 else print(f"{key} not found")

    print(
        f"{key} found at index {iterBinarySearch(a, 0, len(a)-1, key) - 1}"
    ) if iterBinarySearch(a, 0, len(a) - 1, key) != -1 else print(f"{key} not found")
