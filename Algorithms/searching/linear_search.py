def search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i

    return -1


if __name__ == "__main__":

    a = [1, 3, 2, 0, 5, 4, -1]
    key = 9
    print(f"{key} found at index {search(a, key)}") if search(a, key) != -1 else print(
        f"{key} not found"
    )
