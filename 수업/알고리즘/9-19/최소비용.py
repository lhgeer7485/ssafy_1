import heapq


def fnc(start):
    distance = [[0xffffff] * N for _ in range(N)]
    visited = set(start)

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    si, sj = start

    pq = []
    heapq.heappush(pq, (0, si, sj))

    distance[si][sj] = 0

    while len(visited) < N * N:

        dist, si, sj = heapq.heappop(pq)

        visited.add((si, sj))

        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                if (ni, nj) not in visited:
                    if data[ni][nj] - data[si][sj] > 0:
                        if distance[ni][nj] > dist + data[ni][nj] - data[si][sj] + 1:
                            w = dist + data[ni][nj] - data[si][sj] + 1
                            distance[ni][nj] = w

                            heapq.heappush(pq, (w, ni, nj))
                    else:
                        if distance[ni][nj] > dist + 1:
                            w = dist + 1
                            distance[ni][nj] = w

                            heapq.heappush(pq, (w, ni, nj))

    return distance


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    result = fnc((0, 0))

    print(f'#{tc} {result[-1][-1]}')
