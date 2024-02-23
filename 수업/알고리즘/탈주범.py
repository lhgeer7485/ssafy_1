from pprint import pprint

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    pipe = {1: [[-1, 0], [1, 0], [0, -1], [0, 1]],
            2: [[-1, 0], [1, 0]],
            3: [[0, -1], [0, 1]],
            4: [[-1, 0], [0, 1]],
            5: [[1, 0], [0, 1]],
            6: [[1, 0], [0, -1]],
            7: [[-1, 0], [0, -1]]
            }

    link = {(-1, 0) : [1, 2, 5, 6],
            (1, 0): [1, 2, 4, 7],
            (0, -1): [1, 3, 4, 5],
            (0, 1): [1, 3, 6, 7]
            }


    visited = [[0] * M for _ in range(N)]

    queue = []

    queue.append((R, C))
    visited[R][C] = 1

    while queue:
        point_i, point_j = queue.pop(0)
        if data[point_i][point_j] == 0:
            continue
        didj = pipe[data[point_i][point_j]]

        for di, dj in didj:
            ni = point_i + di
            nj = point_j + dj

            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] and data[ni][nj]:
                    if data[ni][nj] in link[(di, dj)]:
                        queue.append((ni, nj))
                        visited[ni][nj] = visited[point_i][point_j] + 1

    #pprint(visited)
    cnt = 0
    for a in range(N):
        for b in range(M):
            if 0 < visited[a][b] <= L:
                cnt += 1
    print(f'#{tc} {cnt}')
