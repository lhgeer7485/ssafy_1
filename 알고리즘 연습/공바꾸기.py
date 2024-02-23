N, M = map(int, input().split())

data = []
basket = [i for i in range(1, N+1)]

for a in range(M):
    data.append(list(map(int, input().split())))

for b in range(M):
    st = data[b][0] - 1
    ed = data[b][1] - 1

    temp = basket[st]
    basket[st] = basket[ed]
    basket[ed] = temp

for c in range(N):
    print(basket[c], end=' ')
