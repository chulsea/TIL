data = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0
n = len(data)
for i in range(n):
    for j in range(n):
        for k in range(4):
            cord_x = j + dx[k]
            cord_y = i + dy[k]
            if 0 <= cord_x < 5 and 0 <= cord_y < 5:
                answer += abs(data[i][j] - data[cord_y][cord_x])
print(answer)