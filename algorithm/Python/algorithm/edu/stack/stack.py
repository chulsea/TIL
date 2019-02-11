SIZE = 100
stack = [0] * SIZE
top = -1


def push(data):
    global top
    top += 1
    stack[top] = data


def pop():
    global top
    if top < 0:
        return None
    pop_data = stack[top]
    stack[top] = 0
    top -= 1
    return pop_data


def is_empty():
    global top
    return top == -1


def peek():
    global top
    return stack[top]


push(1)
print(pop())
push(2)
push(3)
push(4)
print(pop())
print(is_empty())
print(peek())
