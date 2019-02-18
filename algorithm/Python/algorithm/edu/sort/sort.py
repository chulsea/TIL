def bubble(input_list):
    arr = input_list[:]
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection(input_list):
    arr = input_list[:]
    n = len(arr)
    for i in range(n - 1):
        min_num = i
        for j in range(i + 1, n):
            if arr[min_num] > arr[j]:
                min_num = j
        arr[i], arr[min_num] = arr[min_num], arr[i]
    return arr


def insertion(input_list):
    arr = input_list[:]
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


def counting(input_list):
    m, n = max(input_list), len(input_list)
    temp, answer = [0] * (m + 1), [0] * n
    for i in input_list:
        temp[i] += 1
    for i in range(1, len(temp)):
        temp[i] += temp[i - 1]
    for i in input_list:
        temp[i] -= 1
        answer[temp[i]] = i
    return answer


def __partition(input_list, l, r):
    pivot = input_list[l]
    i, j = l, r
    while i < j:
        while input_list[i] <= pivot:
            i += 1
            if i == r:
                break
        while input_list[j] >= pivot:
            j -= 1
            if j == l:
                break
        if i < j:
            input_list[i], input_list[j] = input_list[j], input_list[i]
    input_list[l], input_list[j] = input_list[j], input_list[l]
    return j


def quick(input_list, l, r):
    if l < r:
        mid = __partition(input_list, l, r)
        quick(input_list, l, mid - 1)
        quick(input_list, mid + 1, r)


def main():
    arr = [55, 7, 78, 12, 42]
    # count = [1, 4, 5, 1, 2, 4, 5, 7, 9, 3]
    print(bubble(arr))
    print(insertion(arr))
    print(counting(arr))
    print(selection(arr))
    quick(arr, 0, len(arr)-1)
    print(arr)

if __name__ == "__main__":
    main()
