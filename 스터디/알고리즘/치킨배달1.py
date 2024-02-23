def fnc(tmp):
    global result
    new = []
    for x in range(len(tmp)):
        if tmp[x]:
            new.append(chicken[x])
    sum_v = 0
    for hi, hj in house:
        min_v = 0xffff
        for ci, cj in new:
            min_v = min(min_v, abs(hi-ci) + abs(hj-cj))
        sum_v += min_v
    result = min(result, sum_v)

def cnr(i, cnt):
    if cnt == M:
        fnc(choice)
        return
    if i == chicken_cnt:
        return

    choice[i] = 1
    cnr(i + 1, cnt + 1)
    choice[i] = 0
    cnr(i + 1, cnt)


N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

result = 0xfffff

for a in range(N):
    for b in range(N):
        if data[a][b] == 1:
            house.append((a, b))
        elif data[a][b] == 2:
            chicken.append((a, b))

chicken_cnt = len(chicken)
choice = [0] * chicken_cnt

cnr(0, 0)
print(result)