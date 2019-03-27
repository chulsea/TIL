def bs(arr, num, l, r):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == num:
            return mid+1
        if arr[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    return 0


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    find = list(map(int, input().split()))
    for i in range(m):
        print(bs(nums, find[i], 0, len(nums)-1))


if __name__ == '__main__':
    main()
