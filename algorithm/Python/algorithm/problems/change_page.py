def solution():
    for k in range(500):
        for i in range(500):
            if k == i or adj[i][k] == 1000:
                continue
            for j in range(500):
                if k == j or i == j or adj[k][j] == 1000:
                    continue
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

n = int(input())
adj = [[1000]*500 for _ in range(500)]
for _ in range(n):
    s, f = map(lambda x: int(x)-1, input().split())
    adj[s][f] = 1
solution()
total = cnt = 0
for i in range(500):
    for j in range(500):
        if adj[i][j] != 1000:
            total += adj[i][j]
            cnt += 1
print('%.3f' % (total / cnt))