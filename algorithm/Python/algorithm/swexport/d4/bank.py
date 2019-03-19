def __to_decimal(num, k):
    result = 0
    n = len(num)
    for i in range(n-1, -1, -1):
        if num[i] != '0':
            result += int(num[i])*(k**(n-i-1))
    return result


def solution(b, t):
    t_dec = __to_decimal(t, 3)
    b_dec = __to_decimal(b, 2)
    n = len(b) - 1
    for i in range(len(b)-1, -1, -1):
        temp = b_dec
        if b[i] == '0':
            temp += 2 ** (n-i)
        else:
            temp -= 2 ** (n-i)
        for j in range(len(t)-1, -1, -1):
            tet = int(t[j])
            for k in range(3):
                temp2 = t_dec
                if tet == k:
                    continue
                temp2 += (3 ** (len(t)-1-j)) * (k - tet)
                if temp2 == temp:
                    return temp2


tcs = int(input())
for tc in range(tcs):
    b, t = input(), input()
    print('#{} {}'.format(tc+1, solution(b, t)))
