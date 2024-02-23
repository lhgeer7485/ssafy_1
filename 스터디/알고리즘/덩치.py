N = int(input())
data = []
result = []

for _ in range(N):
    data.append(list(map(int, input().split())))

for a in range(N):
    cnt = 0
    for b in range(N):
        if data[a][0] < data[b][0] and data[a][1] < data[b][1]:
            cnt += 1
    result.append(cnt+1)

print(*result)