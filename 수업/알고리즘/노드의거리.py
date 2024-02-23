def bfs(start, goal):
    visited = [0] * (V + 1)
    queue = []

    queue.append(start)
    visited[start] = 1

    while queue:
        point = queue.pop(0)
        if point == goal:
            return visited[point]
        for a in arr[point]:
            if visited[a] == 0:
                queue.append(a)
                visited[a] = visited[point] + 1

    return 1


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    arr = [[] for _ in range(V + 1)]

    for x in range(E):
        n1, n2 = map(int, input().split())
        arr[n1].append(n2)
        arr[n2].append(n1)

    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, G) - 1}')
