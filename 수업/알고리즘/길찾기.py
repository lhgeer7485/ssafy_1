def dfs():
    start = 0
    goal = 99

    while True:

        for w in arr[start]:
            if w == goal:
                return 1
            if visited[w] == 0:
                visited[w] = 1
                stack.append(start)
                start = w
                break
        else:
            if len(stack) == 0:
                return 0
            start = stack.pop()


T = 10

for _ in range(T):
    TC, E = map(int, input().split())
    SIZE = 100
    data = list(map(int, input().split()))
    arr = [[] * x for x in range(1, SIZE + 1)]

    for x in range(E):
        arr[data[x * 2]].append(data[x * 2 + 1])

    visited = [0] * SIZE
    stack = []

    print(f'#{TC} {dfs()}')
