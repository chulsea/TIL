def __is_same_type(choco):
    n = len(choco)
    for i in range(n):
        temp = choco[i]
        flag = False
        for j in range(i + 1, n):
            if temp == choco[j]:
                flag = True
                break
        if flag:
            return True
    return False


def solution(products):
    answer = 0
    for l, h in products:
        check = 0
        if __is_same_type(l) or __is_same_type(h):
            answer += 1
            continue
        for i in l:
            for j in h:
                if i == j:
                    check += 1
            if check > 2:
                answer += 1
                break
    return answer


def main():
    n = int(input())
    products = []
    for _ in range(n):
        products.append(input().split())
    print(solution(products))


if __name__ == '__main__':
    main()
