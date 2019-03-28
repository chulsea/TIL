n = int(input())
temp = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append((temp[i*2], temp[i*2+1]))
check = []
for i in range(n):
    if i == n-1:
        j = 0
    else:
        j = i+1
    if arr[i][0] < arr[j][0] or arr[i][1] < arr[j][1]:
        check.append(1)
    else:
        check.append(0)
min_len = 0x7fffffff
for i in range(n):
    sl, sw = arr[i]
    cnt = 1
    for j in range(1, n):
        if cnt > min_len:
            break
        k = (i + j) % n
        if check[k-1]:
            cnt += 1
    min_len = min(min_len, cnt)
print(min_len)

