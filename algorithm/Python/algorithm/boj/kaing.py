def solution(M, N, x, y):
    if x == y:
        return x
    temp = []
    answer = -1
    total = N // 2 if N % 2 == 0 and M % 2 == 0 else N
    a = 1
    for _ in range(total - 1):
        a = (a + M) % N
        a = N if a == 0 else a
        temp.append(a)
    y = y - (x - 1)
    y = N + y if y <= 0 else y
    for i in range(len(temp)):
        if temp[i] == y:
            answer = (i + 1) * M + x
            return answer
    return answer


def main():
    n = int(input())
    for _ in range(n):
        M, N, x, y = map(int, input().split())
        print(solution(M, N, x, y))


if __name__ == '__main__':
    main()
