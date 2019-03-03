def solution(n, items, moves):
    pass


def main():
    n = int(input())
    k = int(input())
    items = []
    for _ in range(k):
        items.append(tuple(map(int, input().split())))
    l = int(input())
    moves = []
    for _ in range(l):
        x, c = map(int, input().split())
        moves.append((int(x), c))
    print(solution(n, items, moves))

if __name__ == '__main__':
    main()