T = 10

for tc in range(1, T + 1):
    t = int(input())
    key = input()

    data = input()

    a = 0
    cnt = 0

    while a < len(data):

        for k in range(len(key)):
            if (a + k) < len(data):
                if data[a+k] == key[k]:
                    if k == len(key) - 1:
                        cnt += 1
                        a += len(key)
                        break
                    continue
            a += 1
            break
    print(f'#{tc} {cnt}')