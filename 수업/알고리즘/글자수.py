T = int(input())

for tc in range(1, T + 1):
    st1 = input()
    st2 = input()

    dic = {}

    for a in st1:
        dic.setdefault(a, 0)

    for x in st2:
        try:
            dic[x] += 1
        except KeyError:
            pass

    data = list(dic.values())

    max = data[0]

    for x in data:
        if max < x:
            max = x

    print(f'#{tc} {max}')