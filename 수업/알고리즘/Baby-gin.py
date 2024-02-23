data = list(map(int, input()))

max_data = max(data)

counts = [0] * (max_data + 3)

is_trip = False
is_run = False

for i in data:
    counts[i] += 1

# 런이 있는 경우
for x in range(1, len(counts)):
    if counts[x] > 0:
        if counts[x+1] > 0 and counts[x+2] > 0:
            is_trip = True
            counts[x] -= 1
            counts[x+1] -= 1
            counts[x+2] -= 1
    # 트립을 확인
    if counts[x] >= 3:
        is_run = True

if is_run and is_trip:
    print('Baby Gin')
else:
    print('Lose')