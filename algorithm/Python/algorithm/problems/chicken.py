
def solution(A, B, C, x, y):
    answer = 0
    min_num, max_num = min(x, y), max(x, y)
    more = A if x > y else B
    if A+B > (2*C):
        answer += (min_num * 2 * C)
        if more > 2*C:
            answer += (max_num - min_num) * (2*C)
        else:
            answer += (max_num - min_num) * more
    else:
        answer += A*x + B*y
    return answer


def main():
    A, B, C, x, y = map(int, input().split())
    print(solution(A, B, C, x, y))


if __name__ == '__main__':
    main()
