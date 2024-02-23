from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def fnc(i, j, cnt):
    queue = deque()

    visited[i][j] = cnt

    queue.append((i, j))

    result = [(i, j)]

    n = 1
    sm = data[i][j]

    while queue:
        si, sj = queue.popleft()

        for x in range(4):
            ni = si + di[x]
            nj = sj + dj[x]

            if 0 > ni or ni >= N or 0 > nj or nj >= N:
                continue

            if visited[ni][nj]:
                continue

            sub = abs(data[ni][nj] - data[si][sj])

            if L > sub or R < sub:
                continue

            visited[ni][nj] = cnt
            queue.append((ni, nj))
            result.append((ni, nj))
            n += 1
            sm += data[ni][nj]

    return result, n, sm


N, L, R = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

cnt = 1



day = 0

while True:

    uni = []
    sums = []
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result, n, sm = fnc(i, j, cnt)
                if len(result) > 1:
                    uni.append(result)
                    sums.append(sm)

    if uni:
        for a in range(len(uni)):
            for i, j in uni[a]:
                data[i][j] = sums[a] // len(uni[a])

        day += 1

    else:
        break

print(day)
