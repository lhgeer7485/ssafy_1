import pprint

# def fnc(si, sj, k):
#     cnt = 0
#
#     pk = k
#     is_back = False
#
#     while 0 <= si < N and 0 <= sj < M:
#         # print("ddd")
#         while True:
#             # print("aaaa")
#             cnt += 1
#             data[si][sj] = 1
#             pk = k
#
#             while True:
#                 # print(k)
#                 k += 1
#                 k = k % 4
#                 if k == pk:
#                     is_back = True
#                     # print("dddd")
#                     break
#
#                 di, dj = dr[k]
#
#                 ni = si + di
#                 nj = sj + dj
#                 print(ni, nj)
#                 if 0 > ni or ni >= N or nj > 0 or nj >= M:
#                     continue
#                 if data[ni][nj] == 0:
#                     si, sj = ni, nj
#                     print("dddd")
#                     break
#         if is_back:
#             if pk == 0:
#                 k = 1
#             elif pk == 1:
#                 k = 0
#             elif pk == 2:
#                 k = 3
#             elif pk == 3:
#                 k = 2
#
#             di, dj = dr[k]
#             si += di
#             sj += dj
#             is_back = False
#
#     return cnt

dr = {
    0: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    1: (0, 1),
}


# 상하좌우 탐색하고 없으면 뒤로간 좌표와 방향을 리턴
def check(i, j, d):
    pd = d
    if d == 0:
        back = 2
    elif d == 2:
        back = 0
    elif d == 3:
        back = 1
    elif d == 1:
        back = 3

    for x in range(4):
        d = (d + 1) % 4
        if d == back:
            continue
        di, dj = dr[d]

        ni = i + di
        nj = j + dj

        if 0 > ni or ni >= N or 0 > nj or nj >= M:
            continue
        if data[ni][nj] == 1:
            continue

        return ni, nj, d

    di, dj = dr[back]

    i += di
    j += dj

    return i, j, pd


def clean(r, c, d):
    cnt = 0

    while 0 <= r < N and 0 <= c < M:
        if data[r][c] == 0:
            cnt += 1
            data[r][c] = 1
        r, c, d = check(r, c, d)
        print(r, c, d)

    return cnt


N, M = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

print(clean(r, c, d))
pprint.pprint(data)