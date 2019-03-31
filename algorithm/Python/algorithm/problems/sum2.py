def __comb(n, r, l):
    if n < r:
        return
    if r == 0:
        result = 0
        for i in range(l):
            result += T[i]
        if result not in check:
            check.append(result)
    else:
        T[r-1] = nums[n-1]
        __comb(n-1, r-1, l)
        __comb(n-1, r, l)


n, k = map(int, input().split())
nums = list(map(int, input().split()))
T = [0]*n
check = []
for i in range(n):
    __comb(n, i+1, i+1)
check.sort(reverse=True)
print(check.index(k)+1)
