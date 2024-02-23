def find(i):
    global cnt

    if i <= E + 1:
        if len(arr[i]) == 1:
            find(arr[i][0])
            cnt += 1
        elif len(arr[i]) == 2:
            cnt += 2
            find(arr[i][0])
            find(arr[i][1])


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())

    arr = [[] for _ in range(E + 2)]

    data = list(map(int, input().split()))

    for x in range(E):
        arr[data[x * 2]].append(data[x * 2 + 1])

    cnt = 1
    find(N)

    print(f'#{tc} {cnt}')
