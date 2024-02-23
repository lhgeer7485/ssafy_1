N, M = map(int, input().split())

data = [list(map(str, input())) for _ in range(N)]

# 우 하
di = [0, 1]
dj = [1, 0]

my_min = 2501

for a in range(N):

    for b in range(M):

        for i in range(a, a+8):
            cnt = 0

            for j in range(b, b+8):

                if 0 <= i < N and 0 <= j < M:
                    for r in range(2):
                        ni = i + di[r]
                        nj = j + dj[r]
                        if 0 <= ni < N and 0 <= nj < M:

                            if data[i][j] == 'B' and data[ni][nj] == 'B':
                                data[ni][nj] = 'W'
                                cnt += 1

                            elif data[i][j] == 'W' and data[ni][nj] == 'W':
                                data[ni][nj] = 'B'
                                cnt += 1
                        print(cnt)

    if my_min > cnt:
                my_min = cnt

#print(my_min)
