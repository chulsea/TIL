data = [1, 2, 3]
n = len(data)
T = [0]*n
def __comb(n, r):
    if r == 3:
        print(*T)
    elif n == r:
        return
    else:
        T[r] = data[r]
        __comb(n, r+1)
        T[r] = 0
        __comb(n, r+1)
__comb(3, 0)