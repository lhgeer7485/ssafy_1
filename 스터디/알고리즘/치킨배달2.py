def fnc2(tmp):
    sum_d = 0
    for hi, hj in house:
        min_d = 0xffff
        for ci, cj in tmp:
            min_d = min(min_d, abs(hi - ci) + abs(hj - cj))
        sum_d += min_d

    return sum_d


def fnc(i, tmp):
    global result
    if i == chicken_cnt:
        if len(tmp) == M:
            result = min(result, fnc2(tmp))

        return

    fnc(i + 1, tmp + [chicken[i]])
    fnc(i + 1, tmp)


N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for a in range(N):
    for b in range(N):
        if data[a][b] == 1:
            house.append((a, b))
        elif data[a][b] == 2:
            chicken.append((a, b))
result = 0xffff
chicken_cnt = len(chicken)
fnc(0, [])

print(result)