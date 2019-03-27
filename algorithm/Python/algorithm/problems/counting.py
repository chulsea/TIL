def bs(arr, num, l, r):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def solution(arr, find):
    dp = {}
    for f in find:
        if f in dp:
            print(dp[f], end=' ')
            continue
        idx = bs(arr, f, 0, len(arr)-1)
        if idx == -1:
            dp[f] = 0
            print(dp[f], end=' ')
        else:
            l = r = idx
            while True:
                l -= 1
                if l < 0 or arr[l] != f:
                    break
            while True:
                r += 1
                if r >= len(arr) or arr[r] != f:
                    break
            dp[f] = r - l - 1
            print(r - l - 1, end=' ')


def main():
    n, arr = int(input()), list(map(int, input().split()))
    m, find = int(input()), list(map(int, input().split()))
    solution(arr, find)


if __name__ == '__main__':
    main()

"""
15
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
2
1 2
"""