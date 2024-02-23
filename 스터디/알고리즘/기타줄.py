N, M = map(int, input().split())
data = []

min_six = 1001
min_one = 1001

for x in range(M):
    data.append(list(map(int, input().split())))
    if min_six > data[x][0]:
        min_six = data[x][0]
    if min_one > data[x][1]:
        min_one = data[x][1]

cost = 0

if min_six == 0 or min_one == 0:
    cost = 0

elif  min_six > min_one * 6:
    cost += min_one * N
else:
    cost = (N//6) * min_six
    N %= 6
    if min_six < N * min_one:
        cost += min_six
    else:
        cost += N * min_one

print(cost)