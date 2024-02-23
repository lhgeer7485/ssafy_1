def bfs(start):
    queue.append(start)
    visited[start] = 1

    while queue:
        point = queue.pop(0)
        print(point, end=' ')

        for b in arr[point]:
            if visited[b] == 0:
                queue.append(b)
                visited[b] = visited[point] + 1


N = 7
E = 8
data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

arr = [[] for _ in range(N + 1)]
queue = []
visited = [0] * (N + 1)

for x in range(E):
    arr[data[x * 2]].append(data[x * 2 + 1])

bfs(1)
