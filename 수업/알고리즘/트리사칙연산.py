def post(i):
    global result

    if i <= N:
        # 왼쪽 오른쪽 자식이 있다면 노드는 연산자임
        if left[i] and right[i]:
            n1 = post(left[i])
            n2 = post(right[i])

            if node[i] == '+':
                result = n2 + n1
            elif node[i] == '-':
                result = n1 - n2
            elif node[i] == '*':
                result = n1 * n2
            elif node[i] == '/':
                result = n1 / n2

            return result
        # 자식이 없다면
        return node[i]

    return


T = 10

for tc in range(1, T + 1):
    N = int(input())

    node = [0] * (N + 1)

    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        arr = list(input().split())
        # 연산자라면
        if arr[1] in '+-*/':
            node[int(arr[0])] = arr[1]
            left[(int(arr[0]))] = int(arr[2])
            right[(int(arr[0]))] = int(arr[3])
        else:
            node[int(arr[0])] = int(arr[1])

    result = 0
    post(1)
    print(f'#{tc} {int(result)}')
