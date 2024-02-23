def fnc(i):

    if i * 2 <= N:
        left = fnc(i * 2)
        right = fnc(i * 2 + 1)
        node[i] = left + right

    return node[i]


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    # 완전포화이진으로 하면 계산하기 쉬우니깐 +2를 해준다
    node = [0] * (N + 2)

    for _ in range(M):
        n1, n2 = map(int, input().split())
        node[n1] = n2

    fnc(1)
    print(f'#{tc} {node[L]}')
