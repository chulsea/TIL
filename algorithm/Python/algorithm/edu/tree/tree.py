def solution(tree_list, idx):
    if idx:
        print(idx, end=" ")
        solution(tree_list, tree_list[idx][0])
        solution(tree_list, tree_list[idx][1])


def main():
    n, e = map(int, input().split())
    tree_list = [[0]*3 for _ in range(n+1)]
    preorder = list(map(int, input().split()))
    for i in range(0, len(preorder), 2):
        p, c = preorder[i], preorder[i+1]
        if tree_list[p][0]:
            tree_list[p][1] = c
        else:
            tree_list[p][0] = c
        tree_list[c][2] = p
    for i in range(1, n+1):
        print(i, *tree_list[i])
    print("preorder result :", end=" ")
    solution(tree_list, 1)


if __name__ == '__main__':
    main()
