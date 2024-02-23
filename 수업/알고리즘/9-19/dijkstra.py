def dijkstra(start):
    distance = [0xffffff] * V
    visited = [start]
    now = start

    distance[now] = 0
    while len(visited) < V:

        for next in range(V):
            if next not in visited and graph[now][next] != -1:
                if distance[next] > graph[now][next] + distance[now]:
                    distance[next] = graph[now][next] + distance[now]

        min_dis = 0xffffff
        min_node = -1
        for node in range(V):
            if node not in visited and min_dis > distance[node]:
                min_dis = distance[node]
                min_node = node

        now = min_node
        visited.append(now)

    return distance


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    N = V
    V += 1

    graph = [[-1] * V for _ in range(V)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w

    result = dijkstra(0)

    print(f'#{tc} {result[N]}')
