# M=1: 중복순열
# M=2: 중복조합
# M=3: 순열
dice = [i+1 for i in range(6)]
result = [0]*3
def comb(n, s):
    if n >= 3:
        print(*result)
    else:
        for i in range(s, 6):
            result[n] = dice[i]
            comb(n+1, i)
comb(0, 0)
