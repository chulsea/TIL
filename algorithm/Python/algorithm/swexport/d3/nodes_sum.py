
def solution(n, leafs, l):
    tree = [0]*(n+1)
    s = n // 2
    for idx, val in leafs:
        tree[idx] = val
    for i in range(s, 0, -1):
        if n >= i*2:
            tree[i] += tree[i*2]
            if n >= i*2+1:
                tree[i] += tree[i*2+1]
    return tree[l]


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n, m, l = map(int, input().split())
        leafs = []
        for _ in range(m):
            leafs.append(list(map(int, input().split())))
        print("#{} {}".format(test_case+1, solution(n, leafs, l)))


if __name__ == '__main__':
    main()
