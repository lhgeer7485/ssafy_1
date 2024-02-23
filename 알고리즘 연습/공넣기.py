N, M = map(int, input().split())

basket = [0] * N
data = []

for a in range(M):
    data.append(list(map(int, input().split())))

for b in range(M):
    st = data[b][0]
    ed = data[b][1]
        
    for c in range(st-1, ed):
        basket[c] = data[b][2]

for x in range(len(basket)):
    print(basket[x], end=' ')