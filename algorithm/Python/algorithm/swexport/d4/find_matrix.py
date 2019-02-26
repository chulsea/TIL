import sys

sys.stdin = open('inputs/find_matrix_input.txt')

dx = [1, 0]
dy = [0, 1]


def __bfs(visited, n, sy, sx):
    queue = [(sy, sx)]
    visited[sy][sx] = True
    while queue:
        y, x = queue.pop(0)
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < n and ny < n and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))
    return y, x


def solution(warehouse, n):
    answers = []
    visited = [[False if warehouse[y][x] else True
                for x in range(n)] for y in range(n)]
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                row, col = __bfs(visited, n, y, x)
                row -= y - 1
                col -= x - 1
                answers.append((row, col))
    return answers


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n = int(input())
        warehouse = []
        for _ in range(n):
            warehouse.append(list(map(int, input().split())))
        answers = solution(warehouse, n)
        answers.sort(key=lambda l: (l[0]*l[1], l[0]))
        print(f'#{test_case+1} {len(answers)}', end=' ')
        for a in answers:
            print(f'{a[0]} {a[1]}', end=' ')
        print()


if __name__ == '__main__':
    main()
