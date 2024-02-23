graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
]

def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        if now in visited:
            continue

        visited.append(now)

        for next in range(5):
            if graph[now][next] == 0:
                continue
            if next in visited:
                continue

            stack.append(next)
    return visited


print(*dfs_stack(0))


###################################################

# visited = [0] * 5
# path = []


# def dfs(now):
#     visited[now] = 1
#     print(now, end=' ')

#     for next in range(5):
#         if graph[now][next] == 0:
#             continue
#         if visited[next]:
#             continue

#         dfs(next)

# dfs(0)


#################################################

graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3],
]

def dfs_stack(start):
    visited = [0] * 5
    stack = [start]

    while stack:

        now = stack.pop()
        if visited[now]:
            continue

        visited[now] = 1
        print(now, end=' ')

        for next in range(len(graph[now])):
            if not visited[graph[now][next]]:
                stack.append(graph[now][next])



dfs_stack(0)

