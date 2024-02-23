def fnc(start):
    distance = [[0xffffff] * N for _ in range(N)]
    visited = set(start)

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    si, sj = start

    distance[si][sj] = 0

    while len(visited) < N * N:

        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                if (ni, nj) not in visited:
                    if data[ni][nj] - data[si][sj] > 0:
                        if distance[ni][nj] > distance[si][sj] + data[ni][nj] - data[si][sj] + 1:
                            distance[ni][nj] = distance[si][sj] + data[ni][nj] - data[si][sj] + 1
                    else:
                        if distance[ni][nj] > distance[si][sj] + 1:
                            distance[ni][nj] = distance[si][sj] + 1

        min_dis = 0xffffff
        min_i = -1
        min_j = -1

        for a in range(N):
            for b in range(N):
                if distance[a][b] < min_dis:
                    min_dis = distance[a][b]
                    min_i = a
                    min_j = b

        visited.add((min_i, min_j))

        si = min_i
        sj = min_j

    return distance








T = int(input().split())

for tc in range(1, T + 1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    print(fnc((0, 0)))