import sys

sys.stdin = open('inputs/inorder_input.txt')


def solution(nodes, idx):
    if idx:
        solution(nodes, nodes[idx][1])
        print(nodes[idx][0], end="")
        solution(nodes, nodes[idx][2])


def main():
    for test_case in range(10):
        n = int(input())
        nodes = [[0] * 4 for _ in range(n + 1)]
        for _ in range(n):  # [값, left, right, parent]
            i = input().split()
            idx = int(i[0])
            nodes[idx][0] = i[1]
            if len(i) >= 3:
                l = int(i[2])
                nodes[idx][1] = l
                nodes[l][3] = idx
                if len(i) == 4:
                    r = int(i[3])
                    nodes[idx][2] = r
                    nodes[r][3] = idx
        print('#%d ' % (test_case + 1), end="")
        solution(nodes, 1)
        print()


if __name__ == '__main__':
    main()
