def binarysearch(data, key):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] < key:
            start = mid + 1
        elif data[mid] > key:
            end = mid - 1
        else:
            return mid
    return -1

data = [2, 4, 7, 9, 11, 19, 23]
key = 22

print(binarysearch(data, key))