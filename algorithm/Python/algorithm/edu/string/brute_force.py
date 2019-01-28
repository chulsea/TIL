def brute_force(string, pattern):
    n, m = len(string), len(pattern)  # n은 문자열의 총 길이 / m은 패턴의 총 길이
    i = j = 0  # 초기화
    while j < m and i < n:
        if string[i] != pattern[j]:  # 패턴 탐색하다가 하나라도 어긋나는 것이 있다면 초기화
            i -= j
            j = -1
        i += 1
        j += 1
    if j == m:
        return i - m
    else:
        return -1


def main():
    string = "this is a book~! that is a pencil!"
    pattern = "that"
    result = brute_force(string, pattern)
    assert result != -1
    print(result)

if __name__ == '__main__':
    main()