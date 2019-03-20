import sys

sys.stdin = open('inputs/pw_scan_input.txt')


def __make_bin(num):
    result = ''
    while num > 0:
        result = ('0' if num & 1 == 0 else '1') + result
        num >>= 1
    l = len(result)
    for _ in range(l, 4):
        result = '0' + result
    return result


def __hex_to_bin(hex_num):
    over_ten = {
        'A': 10, 'B': 11, 'C': 12,
        'D': 13, 'E': 14, 'F': 15
    }
    result = ''
    for h in hex_num:
        if h not in over_ten:
            num = int(h)
        else:
            num = over_ten[h]
        result += __make_bin(num)
    return result


def __decode(pw):
    decoder = [
        '3211', '2221', '2122', '1411', '1132',
        '1231', '1114', '1312', '1213', '3112'
    ]
    p = []
    check = pw[0]
    cnt = 1
    for i in range(1, len(pw)):
        if pw[i] != check:
            p.append(cnt)
            cnt = 1
            check = pw[i]
        else:
            cnt += 1
    p.append(cnt)
    min_cnt = min(p)
    p = list(map(lambda x: str(x // min_cnt), p))
    decoded = "".join(p)
    for i in range(10):
        if decoded == decoder[i]:
            return i


def solution(code, n, m):
    answer = 0
    check = set()
    password = []
    inp = []
    for j in range(n):
        temp = code[j].strip('0').split('0000')
        for i in temp:
            i = i.strip('0')
            if i not in inp:
                inp.append(i)
    for temp in inp:
        for i in check:
            temp = temp.replace(i, "")
        temp = temp.strip('0')
        check.add(temp)
    real = set()
    for cd in check:
        for i in check:
            if i != cd:
                cd = cd.replace(i, "")
        real.add(cd)
    real -= {''}
    for t in real:
        h = __hex_to_bin(t)
        for j in range(len(h)-1, -1, -1):
            if h[j] == '1':
                p = []
                ck = '1'
                cnt = 1
                for l in range(j-1, -1, -1):
                    if h[l] != ck:
                        p.append(cnt)
                        cnt = 1
                        ck = h[l]
                    else:
                        cnt += 1
                    if len(p) == 4:
                        break
                base = min(p)
                a = j - (56 * base) + 1
                if a > 0:
                    pw = list(h[a:j + 1])
                else:
                    pw = ['0' for _ in range(-a)] + list(h[:j+1])
                even = odd = 0
                for k in range(8):
                    encode = pw[k*base*7:(k+1)*base*7]
                    decoded = __decode(encode)
                    if k & 1:
                        even += decoded
                    else:
                        odd += decoded
                if (odd * 3 + even) % 10 == 0:
                    password.append((odd + even, t, odd, even))
                    answer += odd + even
                break
    return answer


def main():
    tcs = int(input())
    for tc in range(tcs):
        n, m = map(int, input().split())
        code = []
        for _ in range(n):
            code.append(input())
        print('#{} {}'.format(tc+1, solution(code, n, m)))


if __name__ == '__main__':
    main()
