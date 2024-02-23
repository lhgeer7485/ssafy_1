N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

sum = 0

for i in range(N):
    for j in range(N):
        
        for a in range(4):
            ni = i + di[a]
            nj = j + dj[a]
            if 0 <= ni < N and 0 <= nj < N:
                sum += abs(data[i][j] - data[ni][nj])
print(sum)
        