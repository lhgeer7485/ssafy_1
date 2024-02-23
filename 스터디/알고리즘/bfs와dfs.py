def dfs(start):
    stack = []
    visited = [0] * (V + 1)

    point = start
    visited[point] = 1
    result = []
    result.append(start)

    while True:

        for a in arr[point]:
            if visited[a] == 0:
                stack.append(point)
                point = a
                visited[point] = 1
                result.append(point)
                break
        else:
            if not stack:
                return result
                break
            point = stack.pop()
    return result

def bfs(start):
    queue = []
    visited = [0] * (V + 1)

    queue.append(start)
    visited[start] = 1
    result = []

    while queue:
        point = queue.pop(0)
        result.append(point)
        for a in arr[point]:
            if visited[a] == 0:
                queue.append(a)
                visited[a] = visited[point] + 1

    return result


V, E, S = map(int, input().split())

arr = [[] for _ in range(V + 1)]

for x in range(E):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)


for x in range(V+1):
    arr[x].sort()

#print(arr)

print(*dfs(S))
print(*bfs(S))
