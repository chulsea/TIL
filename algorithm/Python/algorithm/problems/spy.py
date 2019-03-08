def solution(n, s):
    stack = []
    i = 0
    while i < len(s):
        a = s[i]
        if a == '<':
            stack.append(a)
        elif a == '>':
            stack.pop()
        else:
            temp = a
            while s[i+1] != '<' and s[i+1] != '>':
                i += 1
                temp += s[i]
            if len(stack) == n:
                print(temp, end=" ")
        i += 1


def main():
    n, s = input().split()
    n = int(n)
    solution(n, s)


if __name__ == '__main__':
    main()
