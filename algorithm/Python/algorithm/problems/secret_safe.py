def solution(n, pw):
    m = 2 * n - 1
    counts = [0]*m
    k, r = 0, n*(n+1) // 2 - 1
    t = -1
    for i in range(m-1, n-2, -1):
        for j in range(i, t, -2):
            counts[j] += pw[r-k]
            k += 1
        t += 1
    t = k = 1
    for _ in range(n):
        for i in range(t, m-t, 2):
            counts[i] += pw[r+k]
            k += 1
        t += 1
    return max(counts)


def main():
    n = int(input())
    pw = list(map(int, input().split()))
    print(solution(n, pw))


if __name__ == '__main__':
    main()
