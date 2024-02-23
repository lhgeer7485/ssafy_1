def heap(num):
    if len(node) == 1:
        node.append(num)
        return

    node.append(num)
    point = len(node) - 1

    while point > 0:
        # 부모가 더 크다면
        if node[point // 2] > node[point]:
            node[point // 2], node[point] = node[point], node[point // 2]
            point //= 2
        else:
            break


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    data = list(map(int, input().split()))

    node = [0]

    for x in data:
        heap(x)

    point = len(node) - 1

    result = 0

    while point > 0:
        point //= 2
        result += node[point]

    print(f'#{tc} {result}')
