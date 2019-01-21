def sequential_search(data, n, key):
    for i in range(n):
        if data[i] == key:
            return i
    else:
        return -1


data = [4, 9, 11, 23, 2, 19, 7]
key = 19
print(sequential_search(data, len(data), key))
