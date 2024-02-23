T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    # back_ground = [[0] * M for _ in range(M)]

    # 우 하
    di = [0, 1]
    dj = [1, 0]
    result = 0

    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:

                for a in range(2):
                    length = 1
                    for b in range(1, 101):
                        ni = i + di[a] * b
                        nj = j + dj[a] * b

                        if 0 <= ni < N and 0 <= nj < M:
                            if data[ni][nj] == 1:
                                length += 1
                                if result < length:
                                    result = length
                            else:
                                break
    print(f'#{tc} {result}')