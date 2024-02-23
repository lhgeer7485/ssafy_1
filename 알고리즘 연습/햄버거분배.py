N, K  = map(int, input().split())

st = input()
cnt = 0
lst = [x for x in st]

for x in range(N):
    if lst[x] == 'P':
        for y in range(x-K, x+K+1):
            if y >= 0 and y < N and lst[y] == 'H':
                cnt += 1
                lst[y] = 'N'
                break

print(cnt)
