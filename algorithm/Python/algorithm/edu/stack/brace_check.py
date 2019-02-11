def brace_check(braces):
    stack = []
    for brace in braces:
        if brace == '(':
            stack.append(brace)
        elif len(stack) <= 0 or brace == stack.pop():
            return False
    return not len(stack)


if __name__ == '__main__':
    print(brace_check('()()((()))'))
    print(brace_check('()()(())((()))()'))
    print(brace_check('((()((((()()((()())((())))))'))