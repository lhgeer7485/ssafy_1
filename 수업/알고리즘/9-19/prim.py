'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
import heapq


def prim(start):
    heap = []
    MST = [0] * V

    sum_weight = 0

    heapq.heappush(heap, (0, start))

    while heap:
        weight, v = heapq.heappop(heap)

        if MST[v]:
            continue

        MST[v] = 1

        sum_weight += weight

        for next in range(len(graph[v])):
            nw, nv = graph[v][next]
            if MST[nv]:
                continue

            heapq.heappush(heap, (nw, nv))

    return sum_weight


V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f].append((w, t))
    graph[t].append((w, f))

print(prim(0))