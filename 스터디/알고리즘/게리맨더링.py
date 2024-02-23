from collections import deque


def bfs(lst):
    visited = [0] * (N + 1)
    queue = deque()
    queue.append(lst[0])
    visited[lst[0]] = 1

    while queue:
        now = queue.popleft()

        for next in data[now]:
            if visited[next]:
                continue
            if next not in lst:
                continue
            queue.append(next)
            visited[next] = 1

    for x in range(1, len(visited)):
        if x not in lst:
            continue
        if not visited[x]:
            return False

    return True


def check(lst1, lst2):
    global min_v, is_pass

    is_lst1 = bfs(lst1)
    is_lst2 = bfs(lst2)

    if not is_lst1 or not is_lst2:
        return

    is_pass = True

    sm_1 = 0
    sm_2 = 0

    for x in lst1:
        sm_1 += people[x - 1]

    for x in lst2:
        sm_2 += people[x - 1]

    min_v = min(min_v, abs(sm_1 - sm_2))


def com(i, c):
    if i == len(bit):
        if c == M:
            result = []

            for x in range(len(bit)):
                if bit[x]:
                    result.append(num[x])

            result2 = []
            for x in num:
                if x not in result:
                    result2.append(x)

            check(result, result2)

        return

    bit[i] = 1
    com(i + 1, c + 1)
    bit[i] = 0
    com(i + 1, c)


N = int(input())

people = list(map(int, input().split()))

data = [[] for _ in range(N + 1)]

min_v = 0xffffff
is_pass = False

for x in range(1, N+1):
    link = list(map(int, input().split()))
    for i in range(1, len(link)):
        data[x].append(link[i])

# 구역을 나눈다.
bit = [0] * N
num = [i for i in range(1, N + 1)]

for M in range(1, N // 2 + 1):
    com(0, 0)

if is_pass:
    print(min_v)
else:
    print(-1)
