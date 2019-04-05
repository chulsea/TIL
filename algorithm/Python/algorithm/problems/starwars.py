def solution(n, d):
    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if k == i or i == j:
                    continue
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
    max_cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if adj[i][j] < d:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    return max_cnt + 1


n, m, d = map(int, input().split())
adj = [[0x7fffffff]*n for _ in range(n)]
for _ in range(m):
    s, f, e = map(int, input().split())
    adj[s-1][f-1] = e
print(solution(n, d))