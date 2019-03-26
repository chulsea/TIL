import sys

sys.stdin = open('inputs/electronic_cart_input.txt')


def perm(n, r, prev, b):
    global ans
    if b > ans:
        return
    if r == 0:
        ans = min(ans, b + arr[prev][0])
    else:
        for i in range(1, n):
            T[i], T[n-1] = T[n-1], T[i]
            perm(n-1, r-1, T[r], b + arr[prev][T[r]])
            T[i], T[n-1] = T[n-1], T[i]


tcs = int(input())
for tc in range(tcs):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    T = [i for i in range(n)]
    ans = float('inf')
    perm(n, n - 1, 0, 0)
    print('#{} {}'.format(tc+1, ans))
