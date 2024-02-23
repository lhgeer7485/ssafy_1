T = int(input())

for tc in range(1, T + 1):
    N, data = input().split()
    N = int(N)

    result = ''

    stack = []

    for x in data:
        try:
            num = int(x)
        except:
            num = ord(x) - 55

        while True:
            if num == 0:
                break

            if num == 1:
                stack.append(num)
                break

            stack.append(num % 2)
            num //= 2

        while len(stack) != 4:
            stack.append(0)

        for _ in range(4):
            result += str(stack.pop(-1))

    print(f'#{tc} {result}')

