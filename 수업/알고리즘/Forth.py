def fnc():
    global top

    for x in data:
        if x == '+' or x == '-' or x == '*' or x == '/':
            if top < 1:
                return 'error'
            n1 = stack.pop()
            n2 = stack.pop()

            if x == '+':
                stack.append(n2 + n1)
            elif x == '-':
                stack.append(n2 - n1)
            elif x == '*':
                stack.append(n2 * n1)
            elif x == '/':
                stack.append(n2 // n1)
            top -= 1
        elif x == '.':
            if top == 0:
                return stack.pop()
            return 'error'
        else:
            stack.append(int(x))
            top += 1


T = int(input())

for tc in range(1, T + 1):
    data = list(input().split())

    stack = []
    top = -1
    print(f'#{tc} {fnc()}')
