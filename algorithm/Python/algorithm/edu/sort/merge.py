def merge(arr, l, mid, r):
    i, j, k = l, mid+1, l


def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, r)
        merge(arr, l, mid, r)


arr = [55, 7, 78, 12, 42, 33, 25]
result = [0]*len(arr)
merge_sort(arr, 0, len(arr)-1)
print(result)