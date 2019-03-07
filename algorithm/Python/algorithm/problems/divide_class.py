def solution(point_list, min_num, max_num):
    points = [0]*101
    answer = 1000
    for point in point_list:
        points[point] += 1
    for i in range(1, len(points)):
        points[i] += points[i-1]
    max_point = max(points)
    for t1 in range(2, 101):
        if points[t1] == max_point:
            break
        for t2 in range(t1+1, 101):
            a = points[t1-1]
            b = points[t2-1] - a
            c = points[100] - points[t2-1]
            if min_num <= a <= max_num and min_num <= b <= max_num and min_num <= c <= max_num:
                temp_max = max(a, b, c)
                temp_min = min(a, b, c)
                answer = min(answer, temp_max - temp_min)
            if points[t2] == max_point:
                break
    return -1 if answer == 1000 else answer


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n, min_num, max_num = map(int, input().split())
        point_list = list(map(int, input().split()))
        print(solution(point_list, min_num, max_num))


if __name__ == '__main__':
    main()
