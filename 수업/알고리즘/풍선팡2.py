T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    # 상 우 하 좌
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    max = 0

    for i in range(N):
        for j in range(M):
            sum = data[i][j]
            for a in range(4):
                ni = i + di[a]
                nj = j + dj[a]

                if 0 <= ni < N and 0 <= nj < M:
                    sum += data[ni][nj]

            if max < sum:
                max = sum

    print(f'#{test_case} {max}')