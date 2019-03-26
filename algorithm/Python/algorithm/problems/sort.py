def partition(arr, l, r):
    pivot = arr[l]
    i, j = l, r
    while i < j:
        while arr[i] <= pivot:
            i += 1
            if i == r:
                break
        while arr[j] >= pivot:
            j -= 1
            if j == l:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def quicksort(arr, l, r):
    if l < r:
        mid = partition(arr, l, r)
        quicksort(arr, l, mid-1)
        quicksort(arr, mid+1, r)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, n-1)
    print(*arr)


if __name__ == '__main__':
    main()
