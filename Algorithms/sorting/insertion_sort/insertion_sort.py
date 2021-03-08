def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]

        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key


if __name__ == "__main__":

    a = [1, 3, 2, 0, 5, 4, -1]

    print(a)

    insertionSort(a)

    print(a)