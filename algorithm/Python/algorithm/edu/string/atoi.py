def atoi(string):
    value = i = 0
    while i < len(string):
        c = string[i]
        if '0' <= c >= '0':
            disit = ord(c) - ord('0')  # ASCII 코드로 바꾸는 Built-in 함수
        else:
            break
        value = (value * 10) + disit
        i += 1
    return value


def main():
    string = "123"
    result = atoi(string)
    assert result == 123
    print(result)


if __name__ == '__main__':
    main()
