
def __cal_donut(arr, k, x, y):
    sum_donut = 0
    m = 0
    ny, nx = y, x
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(1, k*4-3):
        ny += dy[m]
        nx += dx[m]
        sum_donut += arr[ny][nx]
        if i % (k - 1) == 0:
            m += 1
    return sum_donut


def solution(arr, k):
    n = len(arr)
    max_donut = 0
    for y in range(n-k+1):
        for x in range(n-k+1):
            my = y + k - 1
            mx = x + k - 1
            if 0 <= my < n and 0 <= mx < n:
                sum_donut = __cal_donut(arr, k, x, y)
                max_donut = max(max_donut, sum_donut)
    return max_donut


def main():
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    print(solution(arr, k))


if __name__ == '__main__':
    main()
