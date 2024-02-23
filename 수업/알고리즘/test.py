def dfs(start):
    stack = []
    visited = [0] * (V + 1)

    point = start
    visited[point] = 1
    print(point, end= ' d')
    while True:

        for a in arr[point]:
            if visited[a] == 0:
                stack.append(point)
                point = a
                visited[point] = 1
                print(point, end=' ')
                break
        else:
            if not stack:
                break
            point = stack.pop()


def bfs(start):
    pass


V, E, S = map(int, input().split())

arr = [[] for _ in range(V + 1)]

for x in range(E):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

    dfs(S)
    #bfs(S)
