def solution(candies):
    ans = 0x7fffffff
    candies.sort()
    l = len(candies)
    temp = candies[0] + candies[1]
    for i in range(2, l):
        temp = temp*2 + candies[i]
    ans = min(ans, temp)
    return ans


def main():
    n = int(input())
    candies = list(map(int, input().split()))
    print(solution(candies))


if __name__ == '__main__':
    main()
