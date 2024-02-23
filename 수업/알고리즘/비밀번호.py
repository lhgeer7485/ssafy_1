def stack_pop():
    global top

    my_stack.pop()
    top -= 1

def stack_push(item):
    global top
    top += 1
    my_stack.append(item)


T = 10

for tc in range(1, T + 1):
    SIZE, data = input().split()

    top = -1
    SIZE = int(SIZE)

    my_stack = []

    for x in data:
        if top == -1:
            stack_push(x)
            continue

        if my_stack[top] != x:
            stack_push(x)
        else:
            stack_pop()

    result = ''

    for x in my_stack:
        result += x

    print(f'#{tc} {result}')


