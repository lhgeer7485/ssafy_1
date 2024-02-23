graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
]




def bfs(start):
    visited = [0] * 5

    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        for next in range(5):
            if graph[now][next] == 0:
                continue
            if visited[next]:
                continue
            visited[next] = 1
            queue.append(next)

bfs(0)



##################################




# graph = [
#     [1, 3],
#     [0, 2, 3, 4],
#     [1],
#     [0, 1, 4],
#     [1, 3],
# ]


# def bfs(start):
#     visited = [0] * 5

#     queue = [start]
#     visited[start] = 1

#     while queue:
#         now = queue.pop(0)
#         print(now, end=' ')

#         for next in range(len(graph[now])):

#             if not visited[graph[now][next]]:
#                 visited[graph[now][next]] = 1

#                 queue.append(graph[now][next])


# bfs(0)
