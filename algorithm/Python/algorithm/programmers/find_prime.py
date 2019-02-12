def __is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    n = len(numbers)
    check_list = set()
    for i in range(1 << n):
        temp = ''
        for j in range(n):
            if i & (1 << j):
                temp += numbers[j]
        if temp == '':
            continue

    return answer


print(solution("17"))
print()
print(solution("011"))