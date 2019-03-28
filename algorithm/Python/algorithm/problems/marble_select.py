# data = [1, 2, 3]
# def perm(n, r):
#     if r == 3:
#         print(*data)
#     else:
#         for i in range(r, 3):
#             data[i], data[r] = data[r], data[i]
#             perm(n, r+1)
#             data[i], data[r] = data[r], data[i]
# perm(3, 0)
marble = [1, 2, 3]
n = len(marble)
T = [0]*n
chk = [0]*n


def dfs(a, k):
    global n
    chk[k] = 1
    T[a] = marble[k]
    if a+1 == n:
        print(*T)
        chk[k] = 0
        return
    for i in range(n):
        if not chk[i]:
            dfs(a+1, i)
    chk[k] = 0


# for i in range(n):
#     dfs(0, i)


a = [1, 2, 3]
b = [0]*3
chk = [0]*3
N = 3
def dfs_pro(no):
    if no >= N:
        for i in range(N):
            print(b[i], end=' ')
        print()
    else:
        for i in range(N):
            if not chk[i]:
                chk[i] = 1
                b[no] = a[i]
                dfs_pro(no+1)
                chk[i] = 0

dfs_pro(0)