import sys

sys.stdin = open('inputs/arithmetic_input.txt')

arith = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x*y,
    "/": lambda x, y: x // y,
}


def solution(nodes, idx):
    answer = 0
    if type(nodes[idx][0]) != int:
        left_result = solution(nodes, nodes[idx][1])
        right_result = solution(nodes, nodes[idx][2])
        answer += arith[nodes[idx][0]](left_result, right_result)
    else:
        return nodes[idx][0]
    return answer


def main():
    for test_case in range(10):
        n = int(input())
        nodes = [[0]*4 for _ in range(n+1)]
        for _ in range(n):
            inputs = input().split()
            if len(inputs) > 2:
                p = int(inputs[0])
                nodes[p][0] = inputs[1]
                l = int(inputs[2])
                nodes[p][1] = l
                nodes[l][3] = p
                r = int(inputs[3])
                nodes[p][2] = r
                nodes[r][3] = p
            else:
                nodes[int(inputs[0])][0] = int(inputs[1])
        print("#{} {}".format(test_case+1, solution(nodes, 1)))


if __name__ == '__main__':
    main()
