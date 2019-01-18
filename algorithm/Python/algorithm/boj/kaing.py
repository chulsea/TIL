def solution(M, N, x, y):
    answer = 1
    i = j = 1
    if M % 2 == 0 and N % 2 == 0:
        total = M * N // 2
    else:
        total = M * N
    count = 0
    while count < total and (i != x or j != y):
        answer += 1
        i = 1 if i + 1 > M else i + 1
        j = 1 if j + 1 > N else j + 1
        count += 1
    if total == count:
        return -1
    return answer

def main():
    n = int(input())
    for _ in range(n):
        M, N, x, y = map(int, input().split())
        print(solution(M, N, x, y))

if __name__ == '__main__':
    main()