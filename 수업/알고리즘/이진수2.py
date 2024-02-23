T = int(input())

for tc in range(1, T + 1):
    num = float(input())

    arr = []

    result = ''

    while True:

        if num == 0:
            break

        num *= 2

        if num >= 1:
            num -= 1
            arr.append(1)
        else:
            arr.append(0)

    if len(arr) >= 13:
        result = 'overflow'

    else:
        for x in arr:
            result += str(x)

    print(f'#{tc} {result}')
