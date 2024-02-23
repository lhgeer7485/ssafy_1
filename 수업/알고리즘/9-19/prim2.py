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

V, E = map(int, input().split())

graph = [[-1] * V for _ in range(V)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w


# def prim(graph):
#     MST = set([0])
#     weight = [0xffffff] * V
#
#     weight = graph[0][:]
#     weight[0] = 0
#
#     while len(MST) < V:
#         min_weight = 0xffffff
#         min_node = -1
#         for i in range(V):
#             if i not in MST and weight[i] < min_weight:
#                 min_weight = weight[i]
#                 min_node = i
#         MST.add(min_node)
#         for i in range(V):
#             if i not in MST and graph[min_node][i] < weight[i]:
#                 weight[i] = graph[min_node][i]


def myPrim(start):
    distance = [0xffffff] * V
    MST = [start]
    now = start

    while len(MST) < V:
        for x in range(V):
            if x not in MST:
                if graph[now][x] != -1 and distance[x] > graph[now][x]:
                        distance[x] = graph[now][x]

        min_dis = 0xffffff
        min_node = -1

        for x in range(V):
            if x not in MST:
                if min_dis > distance[x]:
                    min_dis = distance[x]
                    min_node = x

        now = min_node
        MST.append(now)
    return MST

print(myPrim(0))


