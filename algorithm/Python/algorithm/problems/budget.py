def solution(budgets, total):
    ans = 0
    budgets.sort(reverse=True)
    for i in range(len(budgets)):
        base = budgets[i]
        temp = sum(budgets[i:])
        if temp + i*base <= total:
            if i == 0:
                ans = base
            else:
                ans = (total - temp) // i
            break
    return ans


def main():
    n = int(input())
    budgets = list(map(int, input().split()))
    total = int(input())
    print(solution(budgets, total))


if __name__ == '__main__':
    main()