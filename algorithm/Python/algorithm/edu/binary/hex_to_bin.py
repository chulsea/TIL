hex_num = input()
check = {
    'A': 10, 'B': 11, 'C': 12,
    'D': 13, 'E': 14, 'F': 15
}
def dec_to_bin(num):
    result = ''
    while num > 0:
        result = ('1' if num & 1 else '0') + result
        num >>= 1
    for _ in range(len(result), 4):
        result = '0' + result
    return result

bin = ''

for num in hex_num:
    if num in check:
        num = check[num]
    deci = int(num)
    bin += dec_to_bin(deci)


for i in range((len(bin) // 7) + 1):
    k = len(bin) if i == len(bin) // 7 else (i+1)*7
    temp = list(map(int, bin[i * 7:k]))
    result = 0
    if k == len(bin):
        t = len(bin) - 7 * (len(bin) // 7)
        for j in range(t):
            if temp[t - j - 1] & 1:
                result += 2 ** j
    else:
        for j in range(len(temp)):
            if temp[7 - j - 1] & 1:
                result += 2 ** j
    print(result, end=', ')