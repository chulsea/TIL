def findset(x):
    if x==p[x]:
        return x
    else:
        return findset(p[x])

# main-------------------------
T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    p = list(range(n+1))

    data = list(map(int, input().split()))

    for i in range(0, 2*m, 2):
        a = findset(min(data[i], data[i+1]))
        b = findset(max(data[i], data[i+1]))
        # if a==b:
        #     continue
        p[b]=a
    print(p)

    print('#{} {}'.format(tc+1, len(set(p))-1)) # 0 제거
