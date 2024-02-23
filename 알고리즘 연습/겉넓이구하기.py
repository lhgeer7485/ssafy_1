import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = []

for x in range(N):
    data.append(list(map(int, input().split())))

sum1 = 0
sum2 = 0
sum2 = N * M * 2
sum3 = 0



if N == 1:
    for x in range(M):
        sum1 += (data[0][x] * 2)
    sum1 += data[0][0] + data[0][M-1]

    for b in range(M-1):
        sum3 += abs(data[0][b] - data[0][b+1])

elif M == 1:
    for x in range(N):
        sum1 += (data[x][0] * 2)
    sum1 += data[0][0] + data[N-1][0]

    for b in range(N-1):
        sum3 += abs(data[b][0] - data[b+1][0])

else:
    new_data = list(map(list, zip(*data)))
    

    for x in range(M):
        sum1 += data[0][x]
        sum1 += data[N-1][x]

    for a in range(N):
        for b in range(M-1):
            sum3 += abs(data[a][b] - data[a][b+1])

    

    for x in range(N):
        sum1 += new_data[0][x]
        sum1 += new_data[M-1][x]

    for a in range(M):
        for b in range(N-1):      
            sum3 += abs(new_data[a][b] - new_data[a][b+1])

print(sum1 + sum2 + sum3)