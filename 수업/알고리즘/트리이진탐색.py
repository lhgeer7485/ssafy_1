def binary(i):
    global num

    if i <= N:
        binary(i * 2)
        tree[i] = num
        num += 1
        binary((i * 2) + 1)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)

    num = 1

    binary(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')