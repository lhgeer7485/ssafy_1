def fnc1():
    result = ''
    stack = []

    for x in data:
        if x == '+':
            stack.append(x)
        else:
            result += x

    for x in stack:
        result += x

    return result


def fnc2(arr):
    stack = []

    for x in arr:
        if x == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1 + n2)
        else:
            stack.append(int(x))

    return stack[-1]


T = 10

for tc in range(1, T + 1):
    N = int(input())
    data = input()

    print(f'#{tc} {fnc2(fnc1())}')
