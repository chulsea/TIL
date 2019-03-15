def solution(n, r, q):
    if r == 0:
        __myprint(q)
    else:
        for i in range(n-1, -1, -1):
            A[i], A[n-1] = A[n-1], A[i]
            T[r-1] = A[n-1]
            solution(n, r-1, q)
            A[i], A[n-1] = A[n - 1], A[i]


def __myprint(q):
    while q:
        q -= 1
        print(T[q], end=" ")
    print()


A = [i+1 for i in range(3)]
T = [0]*3

solution(3, 2, 2)

