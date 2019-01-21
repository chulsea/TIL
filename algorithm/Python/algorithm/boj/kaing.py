def solution(M, N, x, y):
    temp = []
    total = N // 2 if N % 2 == 0 and M % 2 == 0 else N - 1
    a = 1
    for _ in range(total):
        a = (a + M) % N
        a = N if a == 0 else a
        temp.append(a)
    print(temp)
    answer = 1

    return answer

def main():
    n = int(input())
    for _ in range(n):
        M, N, x, y = map(int, input().split())
        print(solution(M, N, x, y))

if __name__ == '__main__':
    main()