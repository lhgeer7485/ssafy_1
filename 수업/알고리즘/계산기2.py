def fnc1():
    st = ''
    stack = []
    op = {'+': 1, '*': 2}

    for x in data:
        if x in '+*':
            while True:
                if not stack:
                    stack.append(x)
                    break
                if op[stack[-1]] < op[x]:
                    stack.append(x)
                    break
                elif op[stack[-1]] >= op[x]:
                    st += stack.pop()
        else:
            st += x

    while stack:
        st += stack.pop()

    return st


def fnc2(post_data):
    stack = []

    for x in post_data:
        if x in '+*':
            n1 = stack.pop()
            n2 = stack.pop()
            if x == '+':
                stack.append(n1 + n2)
            else:
                stack.append(n1 * n2)
        else:
            stack.append(int(x))
    return stack[-1]


T = 10

for tc in range(1, T + 1):
    N = int(input())

    data = input()

    print(f'#{tc} {fnc2(fnc1())}')
