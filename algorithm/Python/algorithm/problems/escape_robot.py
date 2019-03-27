dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def __is_wall(x, y, i, j):
    return i < 0 or i >= x or j < 0 or j >= y


def solution(x, y, cord, maze):
    s1, s2, f1, f2 = cord
    queue = [(s1-1, s2-1)]
    maze[s2-1][s1-1] = 1
    while queue:
        a, b = queue.pop(0)
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if not __is_wall(x, y, nx, ny) and maze[ny][nx] == 0:
                maze[ny][nx] = maze[b][a] + 1
                queue.append((nx, ny))


def main():
    x, y = map(int, input().split())
    cord = list(map(int, input().split()))
    maze = []
    for _ in range(y):
        maze.append(list(map(int, input())))
    solution(x, y, cord, maze)
    print(maze[cord[3]-1][cord[2]-1] - 1)


if __name__ == '__main__':
    main()