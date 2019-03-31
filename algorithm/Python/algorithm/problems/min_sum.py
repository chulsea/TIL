n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
T = [0]*n
min_num = 0x7fffffff
def perm(n, r, sum):
    global min_num
    if min_num < sum:
        return
    if r == n:
        if sum < min_num:
            min_num = sum
    else:
        for i in range(n):
            if not T[i]:
                T[i] = 1
                perm(n, r+1, sum+arr[r][i])
                T[i] = 0
real_min = 0
for i in range(n):
    temp = 0x7fffffff
    for j in range(n):
        if arr[i][j] < temp:
            temp = arr[i][j]
    real_min += temp
print(real_min)
perm(n, 0, 0)
print(min_num)