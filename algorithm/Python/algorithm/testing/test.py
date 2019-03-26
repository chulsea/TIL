data = [1, 5, 10, 50]
ans = 0
check = set()


def solution(n, r):
    global ans
    if n == 0:
        return
    if r == 0:
        if sum(A) not in check:
            ans += 1
            check.add(sum(A))
    else:
        A[r-1] = data[n-1]
        solution(n-1, r)
        A[r-1] = data[n-1]
        solution(n, r-1)


r = int(input())
A = [0]*r
solution(4, r)
print(ans)