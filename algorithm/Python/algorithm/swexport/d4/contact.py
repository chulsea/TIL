import sys

sys.stdin = open('inputs/contact_input.txt')


def solution(adj_list, start):
    answer = start
    queue = [start]
    visited = [0 for _ in range(101)]
    visited[start] = 1
    while queue:
        t = queue.pop(0)
        if visited[answer] < visited[t]:
            answer = t
        elif visited[answer] == visited[t]:
            answer = max(answer, t)
        for k in adj_list[t]:
            if not visited[k]:
                visited[k] = visited[t] + 1
                queue.append(k)
    return answer


def main():
    for test_case in range(10):
        n, start = map(int, input().split())
        adj_list = [[] for _ in range(101)]
        temp = list(map(int, input().split()))
        for i in range(0, n, 2):
            s, f = map(int, temp[i:i + 2])
            if f not in adj_list:
                adj_list[s].append(f)
        print(f'#{test_case+1} {solution(adj_list, start)}')


if __name__ == '__main__':
    main()
