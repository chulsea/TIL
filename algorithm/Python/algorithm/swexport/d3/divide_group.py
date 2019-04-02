def __find_set(groups, x):
    if x == groups[x]:
        return x
    return __find_set(groups, groups[x])


def solution(n, edges):
    groups = [i for i in range(n)]
    for s, f in edges:
        g1 = __find_set(groups, s - 1)
        g2 = __find_set(groups, f - 1)
        if g1 != g2:
            groups[g1] = g2
    group_list = []
    for g in groups:
        result = __find_set(groups, g)
        if result not in group_list:
            group_list.append(result)
    return len(group_list)


tcs = int(input())
for tc in range(tcs):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    edges = []
    for i in range(m):
        edges.append((temp[i*2], temp[i*2+1]))
    print('#{} {}'.format(tc+1, solution(n, edges)))
