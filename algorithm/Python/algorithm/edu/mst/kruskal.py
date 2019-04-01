def kruskal(n, edges, g):
    ans = 0
    cnt = i = 0
    while cnt < n-1:
        x, y, w = edges[i]
        u = find_group(g, x)
        v = find_group(g, y)
        if u != v:
            ans += w
            g[v] = u
            cnt += 1
        i += 1
    return ans


def find_group(g, n):
    if n == g[n]:
        return n
    return find_group(g, g[n])


tcs = int(input())
for tc in range(tcs):
    v, e = map(int, input().split())
    n = v + 1
    edges = []
    for _ in range(e):
        edges.append(list(map(int, input().split())))
    inf = 0x7fffffff
    edges.sort(key=lambda x: x[2])
    g = list(range(n))
    print('#{} {}'.format(tc + 1, kruskal(n, edges, g)))