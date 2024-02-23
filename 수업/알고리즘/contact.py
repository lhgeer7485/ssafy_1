def fnc(start):
    queue = []
    visited = [0] * 101

    queue.append(start)
    visited[start] = 1
    my_max = 0

    while queue:
        point = queue.pop(0)

        for a in arr[point]:
            if visited[a] == 0:
                queue.append(a)
                visited[a] = visited[point] + 1
                if my_max < visited[a]:
                    my_max = visited[a]

    for a in range(101):
        if visited[a] == my_max:
            result = a

    return result


T = 10

for tc in range(1, T + 1):
    N, S = map(int, input().split())

    data = list(map(int, input().split()))

    arr = [[] for _ in range(101)]

    for x in range(N // 2):
        arr[data[x * 2]].append(data[x * 2 + 1])

    print(f'#{tc} {fnc(S)}')
