def inOder(i):
    global result
    if i <= N:
        inOder(i * 2)
        result += tree[i]
        inOder(i * 2 + 1)


T = 10

for tc in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)

    for x in range(N):
        arr = list(input().split())
        node, data = arr[0], arr[1]
        node = int(node)
        #left = int(left_i)
        #right = int(right_i)

        tree[node] = data
    result = ''
    inOder(1)

    print(f'#{tc} {result}')
