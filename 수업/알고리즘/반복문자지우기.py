def stack_pop():
    global top

    my_stack.pop()
    top -= 1

def stack_push(item):
    global top
    top += 1
    my_stack.append(item)


T = int(input())

for tc in range(1, T + 1):
    data = input()

    top = -1
    SIZE = len(data)

    my_stack = []

    for x in data:
        if top == -1:
            stack_push(x)
            continue

        if my_stack[top] != x:
            stack_push(x)
        else:
            stack_pop()
    
    print(f'#{tc} {len(my_stack)}')


