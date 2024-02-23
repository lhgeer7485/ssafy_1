T = int(input())

for tc in range(1, T + 1):

    tc, N = input().split()
    N = int(N)

    data = list(input().split())

    dic = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3,
           'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7,
           'EGT' : 8, 'NIN' : 9}
    

    for a in range(N-1):
        min = a
        for b in range(a, N):
            if dic[data[min]] > dic[data[b]]:
                min = b
        data[min], data[a] = data[a], data[min]

    print(tc)
    print(*data)
        