
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


def quick(arr, l, r):
    if l < r:
        mid = partition(arr, l, r)
        quick(arr, l, mid-1)
        quick(arr, mid+1, r)


def main():
    arr = [3, 4, 6, 1, 8, 2]
    quick(arr, 0, len(arr)-1)
    print(arr)


if __name__ == '__main__':
    main()
