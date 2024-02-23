def dfs(start, goal):
    visited[start] = 1

    while True:

        for w in arr[start]:
            if w == goal:
                return 1
            if visited[w] == 0:
                stack.append(start)
                start = w
                visited[w] = 1
                break
        else:
            if len(stack) == 0:
                return 0
            start = stack.pop()


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    arr = [[] * x for x in range(1, V + 2)]
    visited = [0] * (V + 1)
    stack = []

    for x in data:
        arr[x[0]].append(x[1])

    print(f'#{tc} {dfs(S, G)}')
