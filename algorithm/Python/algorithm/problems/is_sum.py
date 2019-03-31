def solution(nums, T, n, r, k, s):
    global ans
    if ans:
        return
    if s > k:
        return
    if r == 0:
        if k == s:
            ans = True
    elif n < r:
        return
    else:
        T[r-1] = nums[n-1]
        solution(nums, T, n-1, r-1, k, s+nums[n-1])
        solution(nums, T, n-1, r, k, s)


def main():
    global ans
    test_cases = int(input())
    for test_case in range(test_cases):
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        ans = False
        for i in range(1, n+1):
            T = [0]*i
            solution(nums, T, n, i, k, 0)
        if ans:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()