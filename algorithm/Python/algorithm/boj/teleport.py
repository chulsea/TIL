n, t = list(map(int, input().split()))
nodes = []
for _ in range(n):
    nodes.append(list(map(int, input().split())))
m = int(input())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))


def dijkstra(n, t, s, f):
    visited = [0]*n
    dist = [0x7fffffff]*n
    queue = [s]
    dist[s] = 0
    while queue:
        node = queue.pop(0)
        visited[node] = 1
        is_t, x, y = nodes[node]
        for i in range(n):
            is_nt, nx, ny = nodes[i]
            d = abs(x - nx) + abs(y - ny) # i에서 node까지 가는 거리 d
            if is_t & is_nt and d > t:
                d = t
            dist[i] = min(dist[i], dist[node] + d)
            queue.append(i)
        if 0 not in visited:
            break
    return dist[f]


for i in range(m):
    s, f = arr[i]
    print(dijkstra(n, t, s-1, f-1))

