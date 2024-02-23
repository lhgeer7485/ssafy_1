from pprint import pprint


def find(start_i, start_j, n):
    global cnt
    queue = []
    queue.append((start_i, start_j))
    visited[start_i][start_j] = n

    while queue:
        point_i, point_j = queue.pop(0)

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni = point_i + di
            nj = point_j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if data[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = n
                    queue.append((ni, nj))
                    cnt += 1
    result.append(cnt)
    cnt = 1


N = int(input())
data = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
num = 1
cnt = 1
result = []

for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and not visited[i][j]:
            find(i, j, num)
            num += 1

print(len(result))
result.sort()
for x in result:
    print(x)
