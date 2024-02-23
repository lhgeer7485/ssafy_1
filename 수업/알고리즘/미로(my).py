def fnc():
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for y in range(N):
        for x in range(N):
            if data[x][y] == 3:
                start_x, start_y = x, y

    stack = [(start_x, start_y)]

    visited = [[0] * N for _ in range(N)]
    visited[start_x][start_y] = 1

    while stack:

        i, j = stack[-1]

        for a in range(4):
            ni = i + di[a]
            nj = j + dj[a]

            if 0 <= ni < N and 0 <= nj < N:
                if data[ni][nj] == 2:
                    return 1

                if data[ni][nj] == 0 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    stack.append((ni, nj))
                    break
        else:
            stack.pop()

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    data = [list(map(int, input().strip())) for _ in range(N)]

    result = fnc()
    print(f'#{tc} {result}')
