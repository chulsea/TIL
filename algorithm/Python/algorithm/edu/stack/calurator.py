
def convert_postfix(inorder):
    stack = []
    operators = ['+', '-', '*', '/']
    for s in inorder:
        if s in operators:
            stack.append(s)
        else:
            print(s, end='')
    while stack:
        print(stack.pop(), end='')


def main():
    inorder = input()
    convert_postfix(inorder)


if __name__ == '__main__':
    main()
