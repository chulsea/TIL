import sys

sys.stdin = open('dfs.txt', 'r')


def dfs_recursion(v, adj):
    print(v, end=" ")
    visited[v] = True
    for w in range(1, len(adj[v])):
        if adj[v][w] and not visited[w]:
            dfs_recursion(w, adj)


def dfs(v, adj):
    stack = [v]
    visited = [0] * len(adj)
    while stack:
        s = stack[-1]
        if not visited[s]:
            print(s, end=" ")
        visited[s] = True
        flag = False
        for i in range(1, len(adj[s])):
            if adj[s][i] and not visited[i]:
                stack.append(i)
                flag = True
                break
        if not flag:
            stack.pop()


n = 7
visited = [0] * (n + 1)
input_adj = list(map(int, input().split(", ")))
adj = [[0] * (n+1) for _ in range(n+1)]
for i in range(0, len(input_adj), 2):
    adj[input_adj[i]][input_adj[i+1]] = 1
    adj[input_adj[i+1]][input_adj[i]] = 1

start = 1
dfs_recursion(start, adj)
print()
dfs(start, adj)