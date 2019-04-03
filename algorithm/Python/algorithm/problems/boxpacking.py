def __comb(n, start, i, idx):
    global ans
    if n == i:
        A = B = 0
        for i in range(n):
            if chk[i]:
                A += boxes[i]
            else:
                B += boxes[i]
        result = A + B
        if ans < result:
            ans = result
    else:
        pass


tcs = int(input())
for _ in range(tcs):
    n = int(input())
    boxes = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        chk = [0]*n
        __comb(n, i, i+1, i)
    print(ans)
