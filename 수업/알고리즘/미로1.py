def fnc(point_i, point_j):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    queue.append((point_i, point_j))
    visited[point_i][point_j] = 1

    while queue:
        point_i, point_j = queue.pop(0)

        if data[point_i][point_j] == '3':
            return 1

        for d in range(4):
            ni = point_i + di[d]
            nj = point_j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if data[ni][nj] != '1' and visited[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[point_i][point_j] + 1
    return 0


T = 10

for t in range(1, T + 1):
    tc = int(input())
    N = 16
    data = [input() for _ in range(N)]

    queue = []
    visited = [[0] * N for _ in range(N)]
    print(f'#{tc} {fnc(1, 1)}')
