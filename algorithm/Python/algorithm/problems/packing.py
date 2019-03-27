def change(arr, l):
    base = arr[l]
    k = l
    for i in range(l+1, len(arr)):
        if arr[i] < base:
            arr[k], arr[i] = arr[i], arr[k]
            k += 1
        if arr[i] > base:
            break

def solution(candies):
    ans = 0
    n = len(candies)
    candies.sort()
    for i in range(n-1):
        change(candies, i)
        candies[i+1] += candies[i]
        ans += candies[i+1]
    return ans


def main():
    n = int(input())
    candies = list(map(int, input().split()))
    print(solution(candies))


if __name__ == '__main__':
    main()
