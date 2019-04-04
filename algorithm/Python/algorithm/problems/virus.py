def find_set(x):
    if x == group[x]:
        return x
    return find_set(group[x])

n = int(input())
m = int(input())
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
group = [i for i in range(n+1)]
for edge in edges:
    s, f = edge
    g1 = find_set(s)
    g2 = find_set(f)
    if g1 != g2:
        group[g1] = g2
ans = 0
base = find_set(1)
for i in range(1, n+1):
    if find_set(group[i]) == base:
        ans += 1
print(ans-1)