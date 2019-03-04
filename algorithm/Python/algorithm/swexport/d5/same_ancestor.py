import sys

sys.stdin = open('inputs/same_ancestor_input.txt')


def __find_ancestor(tree_list, idx):
    result= []
    p = tree_list[idx][2]
    while p:
        result.append(p)
        p = tree_list[p][2]
    return result


def __get_tree_size(tree_list, idx):
    answer = left_result = right_result = 0
    if idx:
        answer += 1
        left_result = __get_tree_size(tree_list, tree_list[idx][0])
        right_result = __get_tree_size(tree_list, tree_list[idx][1])
    return answer + left_result + right_result


def solution(tree_list, a, b):
    a_ancestors = __find_ancestor(tree_list, a)
    b_ancestors = __find_ancestor(tree_list, b)
    flag = False
    same_anc = 0
    for i in range(len(a_ancestors)):
        a_anc = a_ancestors[i]
        if flag:
            break
        for j in range(len(b_ancestors)):
            if a_anc == b_ancestors[j]:
                same_anc = a_anc
                flag = True
                break
    return same_anc, __get_tree_size(tree_list, same_anc)


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n, e, a, b = map(int, input().split())
        tree_list = [[0]*3 for _ in range(n+1)] # left right parent
        edges = list(map(int, input().split()))
        for i in range(e):
            p = edges[2*i]
            c = edges[2*i+1]
            if not tree_list[p][0]:
                tree_list[p][0] = c
            else:
                tree_list[p][1] = c
            tree_list[c][2] = p
        idx, size = solution(tree_list, a, b)
        print('#{} {} {}'.format(test_case+1, idx, size))


if __name__ == '__main__':
    main()
