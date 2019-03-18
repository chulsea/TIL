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

pattern = [
    '001101', '010011', '111011', '110001', '100011',
    '110111', '001011', '111101', '011001', '101111'
]

i = len(bin)-1
ans = []
while i >= 0:
    if bin[i] == '1':
        for j in range(10):
            if bin[i-5:i+1] == pattern[j]:
                ans.insert(0, j)
                i -= 5
                break
    i -= 1
print(*ans)