def selection(arr, i, m, n):
    if i == n:
        arr[m], arr[i - 1] = arr[i - 1], arr[m]
        return
    if arr[i] > arr[m]:
        m = i
    selection(arr, i + 1, m, n)


def main():
    arr = [39, 54, 12, 8, 86, 47]
    for i in range(len(arr) - 1):
        selection(arr, 0, 0, len(arr) - i)
    print(arr)


if __name__ == '__main__':
    main()
