def f1(n, m):
    len3 = len(m) - len(n)
    x = 0
    sm = 0
    result = 0

    for a in range(len3 + 1):
        for j in range(len(n)):
            sm += n[j] * m[x]
            x += 1

        x = a + 1
        if result < sm:
            result = sm

        sm = 0

    return result

t = int(input())
nList = list()
mList = list()
len1 = 0
len2 = 0

resultList = list()

for i in range(t):
    nm = list(map(int, input().split()))

    li1 = list(map(int, input().split()))
    li2 = list(map(int, input().split()))

    if nm[0] < nm[1]:
        nList = li1
        mList = li2
    else:
        nList = li2
        mList = li1

    resultList.append(f1(nList, mList))

for k in range(1, t + 1):
    print(f'#{k} {resultList[k - 1]}')
