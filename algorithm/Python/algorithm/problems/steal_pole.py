def solution(arr):
    answer = 0
    n = len(arr)
    stack = []
    for i in range(n):
        if arr[i] == "(":
            stack.append(arr[i])
        else:
            prev = arr[i-1]
            stack.pop()
            if prev == "(":
                answer += len(stack)
            elif prev == ")":
                answer += 1
    return answer



def main():
    arr = list(input())
    print(solution(arr))


if __name__ == '__main__':
    main()