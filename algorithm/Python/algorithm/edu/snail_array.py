def find_min(arr):
    min = 100
    minx = miny = -1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if min > arr[i][j]:
                min = arr[i][j]
                minx, miny = j, i
    arr[miny][minx] = 100
    return min


def make_snail_array(arr, x, y):
    n = len(arr)
    m = len(arr[0])
    answer = [[0 for _ in range(m)] for _ in range(n)]
    move = 0
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    for _ in range(n * m):
        min = find_min(arr)
        nextX = x + dx[move]
        nextY = y + dy[move]
        if nextY < 0 or nextY >= n or nextX < 0 or nextX >= m or answer[nextY][nextX] != 0:
            move = (move + 1) % 4
            nextX = x + dx[move]
            nextY = y + dy[move]
        x = nextX
        y = nextY
        answer[nextY][nextX] = min
    return answer

def main():
    arr = [
        [9, 20, 2, 18, 11],
        [19, 1, 25, 3, 21],
        [8, 24, 10, 17, 7],
        [15, 4, 16, 5, 6],
        [12, 13, 22, 23, 14]]
    arr2 = [
        [9, 20, 2, 18, 11],
        [19, 1, 12, 3, 14],
        [8, 13, 10, 17, 7],
        [15, 4, 16, 5, 6]]
    answer1 = make_snail_array(arr, -1, 0)
    answer2 = make_snail_array(arr2, -1, 0)
    for a in answer1:
        print(a)
    for a in answer2:
        print(a)


if __name__ == '__main__':
    main()
