import sys

sys.stdin = open('inputs/distance_maze_input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def __dfs(maze, visited, y, x):
    visited[y][x] = True
    n = len(maze)
    if maze[y][x] == 3:
        return 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and \
                not visited[ny][nx] and maze[ny][nx] != 1:
            result = __dfs(maze, visited, ny, nx)
            if result:
                return result + 1


def __bfs(maze, visited, y, x):
    n = len(maze)
    queue = [(y, x)]
    visited[y][x] = 1
    while queue:
        py, px = queue.pop(0)
        if maze[py][px] == 3:
            return visited[py][px]
        for i in range(4):
            ny = py + dy[i]
            nx = px + dx[i]
            if 0 <= ny < n and 0 <= nx < n and \
                    not visited[ny][nx] and maze[ny][nx] != 1:
                visited[ny][nx] = visited[py][px] + 1
                queue.append((ny, nx))


def solution(maze, n):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if maze[y][x] == 2:
                sy, sx = y, x
    answer = __bfs(maze, visited, sy, sx)
    return answer - 2 if answer else 0


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n = int(input())
        maze = []
        for i in range(n):
            maze.append(list(map(int, input())))
        print(f'#{test_case + 1} {solution(maze, n)}')


if __name__ == '__main__':
    main()
