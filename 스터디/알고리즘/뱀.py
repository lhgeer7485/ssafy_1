from collections import deque

# import pprint
r_dic = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1],
}


def fnc():
    time = 0
    queue = deque()
    # queue.append((0, 0))
    data[0][0] = 1
    r = 1

    change_time, nr = re.popleft()

    head_i, head_j = 0, 0
    tail_i, tail_j = 0, 0

    while True:

        if time == change_time:
            if nr == 'L':
                r = (r - 1) % 4
                if r < 0:
                    r = 0

            elif nr == 'D':
                r = (r + 1) % 4

            if re:
                change_time, nr = re.popleft()

        time += 1
        # pprint.pprint(data)
        # print(head_i, head_j, time)
        head_i += r_dic[r][0]
        head_j += r_dic[r][1]
        # print(head_i, head_j)
        # print("-------------")

        if (0 > head_i or head_i >= N or 0 > head_j or head_j >= N) or data[head_i][head_j] == 1:
            return time

        queue.append((head_i, head_j))

        if data[head_i][head_j] == 2:
            data[head_i][head_j] = 1

        else:
            data[tail_i][tail_j] = 0
            data[head_i][head_j] = 1
            tail_i, tail_j = queue.popleft()


N = int(input())
K = int(input())
data = [[0] * N for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    data[x - 1][y - 1] = 2
# pprint.pprint(data)
L = int(input())
re = deque()

for _ in range(L):
    x, y = input().split()
    re.append((int(x), y))

print(fnc())
