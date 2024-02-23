'''
V E
7 8
v1 w1 v2 w2 ...
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


# def dfs(n, V, adj_m):
#     stack = []
#     visitied = [0] * (V + 1)
#     visitied[n] = 1
#     print(n)
#     while True:
#         # 방문할 지점이 있는지 확인
#         for w in range(1, V + 1):
#             # 방문안한 지점이 있으면
#             if adj_m[n][w] == 1 and visitied[w] == 0:
#                 stack.append(n)
#                 visitied[w] = 1
#                 n = w
#                 print(n)
#                 break
#         else:
#             if len(stack) == 0:
#                 break
#             else:
#                 n = stack.pop()


# # V는 정점 E는 간선 수
# V, E = map(int, input().split())
# arr = list(map(int, input().split()))
# adj_m = [[0] * (V + 1) for _ in range(V + 1)]
# for i in range(E):
#     v1, v2 = arr[i * 2], arr[i * 2 + 1]
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1

# dfs(1, V, adj_m)

############################################

# dfs
# 7 8
# 1 2 1 3 2 4 2 5 3 5 4 6 5 6 6 7
def dfs(now):
    visited = [0] * (V + 1)
    stack = [now]
    visited[now] = 1
    print(now)
    while stack:

        for next in link[now]:
            if not visited[next]:
                print(next)
                visited[next] = 1
                stack.append(now)
                now = next
                break
        else:
            now = stack.pop()


V, E = map(int, input().split())

data = list(map(int, input().split()))
link = [[] for _ in range(V + 1)]
for x in range(E):
    link[data[x * 2]].append(data[x * 2 + 1])

dfs(1)


###############################
# 재귀
# N = 5
# arr = [[0] * N for _ in range(N)]
# def solve(row):
#     if row == N:
#         return
#     # 작업후에
#     for i in range(row+1):
#         if i == 0:
#             arr[row][i] = 1
#             continue
#         arr[row][i] = arr[row-1][i] + arr[row-1][i-1]
#         # 위쪽 값과 좌측 상단값 더하기
#     solve(row+1)

# solve(0)
# for row in arr:
#     print(*row)