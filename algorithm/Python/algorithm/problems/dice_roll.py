ans = []
def perm(dice, T, n, r, k, s):
    if s > k:
        return
    if r == 0:
        if s == k:
            temp = T[:]
            ans.append(temp)
        return
    else:
        for i in range(6):
            dice[i], dice[n-1] = dice[n-1], dice[i]
            T[r-1] = dice[n-1]
            perm(dice, T, n, r-1, k, s+dice[n-1])
            dice[i], dice[n-1] = dice[n-1], dice[i]


def main():
    r, k = map(int, input().split())
    dice = [i+1 for i in range(6)]
    T = [0]*r
    perm(dice, T, 6, r, k, 0)
    ans.sort(key=lambda x: [x[i] for i in range(r)])
    for i in range(len(ans)):
        print(*ans[i])

if __name__ == '__main__':
    main()
