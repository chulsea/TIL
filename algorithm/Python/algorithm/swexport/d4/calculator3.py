import sys

sys.stdin = open('inputs/calculator3_input.txt')


def solution(case):
    oper_stack = []
    num_stack = []
    operators = ['+', '(', '*', ')']
    for s in case:
        if s in operators:
            if s == ')':
                oper = oper_stack.pop()
                while oper != '(':
                    if oper == '+':
                        s_num = num_stack.pop()
                        f_num = num_stack.pop()
                        num_stack.append(f_num + s_num)
                    if oper == '*':
                        s_num = num_stack.pop()
                        f_num = num_stack.pop()
                        num_stack.append(f_num * s_num)
                    oper = oper_stack.pop()
            else:
                oper_stack.append(s)
        else:
            num_stack.append(int(s))
    while oper_stack:
        oper = oper_stack.pop()
        if oper == '+':
            s_num = num_stack.pop()
            f_num = num_stack.pop()
            num_stack.append(f_num + s_num)
        if oper == '*':
            s_num = num_stack.pop()
            f_num = num_stack.pop()
            num_stack.append(f_num * s_num)
    print(num_stack)
    print(oper_stack)

def main():
    for test_case in range(10):
        input()
        case = input()
        print(f'#{test_case + 1} {solution(case)}')


if __name__ == '__main__':
    main()
