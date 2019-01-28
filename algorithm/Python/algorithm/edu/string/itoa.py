def itoa(num):
    answer = []
    minus = False if num > 0 else True
    temp = abs(num)
    while temp > 0:
        answer.append(chr(temp % 10 + ord('0')))
        temp //= 10
    if minus:
        answer.append("-")
    answer.reverse()
    return "".join(answer)


def main():
    a = -123
    answer = itoa(a)
    print(answer, type(answer))


if __name__ == '__main__':
    main()
