def merge(arr, temp, l, mid, r):
    if r - l < 1:
        return arr[l]
    i = l
    k, t = l, mid + 1
    while k <= mid and t <= r:
        if arr[k] < arr[t]:
            temp[i] = arr[k]
            k += 1
        else:
            temp[i] = arr[t]
            t += 1
        i += 1
    while k <= mid:
        temp[i] = arr[k]
        i += 1
        k += 1
    while t <= r:
        temp[i] = arr[t]
        i += 1
        t += 1
    for i in range(l, r+1):
        arr[i] = temp[i]


def merge_sort(arr, temp, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, temp, l, mid)
        merge_sort(arr, temp, mid+1, r)
        merge(arr, temp, l, mid, r)


arr = [55, 7, 78, 12, 42, 33, 25]
temp = [0]*len(arr)
merge_sort(arr, temp, 0, len(arr)-1)
print(temp)