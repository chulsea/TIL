# boj 2531 회전초밥
def solution(belt, kind, k, c):
    n = len(belt)  # 회전초밥 목록
    check = 0
    for i in range(n - k, n):
        # idx 0부터 탐색할 수 있도록 setting
        if kind[belt[i]] == 0:
            check += 1
        kind[belt[i]] += 1
    """
        처음 setting, kind의 idx는 현재 먹은 초밥의 종류이며
        해당 idx의 값은 초밥을 얼마나 먹었는지 알려준다.
        check는 현재 위치에서 초밥을 먹은 갯수를 의미
    """
    max_sushi = 0
    for i in range(n):
        if kind[belt[i]] == 0:
            check += 1
        kind[belt[i]] += 1
        del_sushi = (n + i - k) % n
        # 맨 뒤 스시는 계산에서 제외
        if kind[belt[del_sushi]] == 1:
            check -= 1
        # 먹었던 스시라면 먹은 종류 -1
        kind[belt[del_sushi]] -= 1
        # 먹은 종류도 -1
        max_sushi = max(max_sushi, check + (kind[c] == 0))
    return max_sushi


def main():
    n, d, k, c = map(int, input().split())
    belt = []
    kind = [0] * 3001
    for i in range(n):
        belt.append(int(input()))
        # belt.append(int(input()))
    print(solution(belt, kind, k, c))


if __name__ == '__main__':
    main()
