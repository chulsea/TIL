import sys

sys.stdin = open('inputs/subtree_input.txt')

def solution(idx, nodes):
    answer = left_size = right_size = 0
    if idx:
        answer += 1
        left_size = solution(nodes[idx][0], nodes)
        right_size = solution(nodes[idx][1], nodes)
    return answer + left_size + right_size


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        e, r = map(int, input().split())
        n = e+1
        nodes = [[0]*2 for _ in range(n+1)]
        inputs = list(map(int, input().split()))
        for i in range(e):
            p = i * 2
            if not nodes[inputs[p]][0]:
                nodes[inputs[p]][0] = inputs[p + 1]
            else:
                nodes[inputs[p]][1] = inputs[p + 1]
        print("#{} {}".format(test_case+1, solution(r, nodes)))


if __name__ == '__main__':
    main()
