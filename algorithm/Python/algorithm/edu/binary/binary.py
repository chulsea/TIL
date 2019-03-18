bin = input()
for i in range(len(bin) // 7):
    temp = list(map(int, bin[i * 7:(i + 1) * 7]))
    result = 0
    for j in range(len(temp)):
        if temp[7 * i - j - 1] & 1:
            result += 2 ** j
    print(result, end=', ')

a = 0x8
p = 0xf


def print_8bit(num):
    for i in range(3, -1, -1):
        if num & (1 << i):
            print(1, end='')
        else:
            print(0, end='')
    print()


print_8bit(a)
a^=p
print_8bit(a)
a^=p
print_8bit(a)
