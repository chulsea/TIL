import sys

sys.stdin = open('inputs/distance_node_input.txt')


def solution(adj_list, s, f):
    queue = [s]
    n = len(adj_list)
    visited = [0 for _ in range(n+1)]
    visited[s] = 1
    while queue:
        cur = queue.pop(0)
        if cur == f:
            return visited[cur] - 1
        for i in adj_list[cur]:
            if not visited[i]:
                visited[i] = visited[cur] + 1
                queue.append(i)
    return 0


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n, m = map(int, input().split())
        adj_list = [[] for _ in range(n+1)]
        for i in range(m):
            s, f = map(int, input().split())
            adj_list[s].append(f)
            adj_list[f].append(s)
        s, f = map(int, input().split())
        print(f'#{test_case + 1} {solution(adj_list, s, f)}')


if __name__ == '__main__':
    main()
