from pprint import pprint


def tomato(sx, si, sj):
    dd = [[0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1], [-1, 0, 0], [1, 0, 0]]
    data[sx][si][sj] = day + 1

    for dx, di, dj in dd:
        nx = sx + dx
        ni = si + di
        nj = sj + dj
        if 0 <= nx < H and 0 <= ni < N and 0 <= nj < M:
            if data[nx][ni][nj] != day and data[nx][ni][nj] != -1:
                data[nx][ni][nj] = day + 1


def check1():
    for x in range(H):
        for i in range(N):
            for j in range(M):
                if data[x][i][j] == 1:
                    return True
    return False


def check2():
    for x in range(H):
        for i in range(N):
            for j in range(M):
                if data[x][i][j] == 0:
                    return False
    return True


M, N, H = map(int, input().split())

data = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
after = data[:]
day = 1
zero_cnt = 0

if not check1():
    print(0)

else:
    while True:
        print(data)
        for x in range(H):
            for i in range(N):
                for j in range(M):
                    if data[x][i][j] == day:
                        tomato(x, i, j)
                        day += 1
        if check2():
            break

print(day)