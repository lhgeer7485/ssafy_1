def fnc(data, n):
    counts = 0

    while True:
        if data % n == 0:
            data //= n
            counts += 1
        else:
            break

    return counts


T = int(input())

for x in range(T):
    data = int(input())
    
    a = fnc(data, 2)
    b = fnc(data, 3)
    c = fnc(data, 5)
    d = fnc(data, 7)
    e = fnc(data, 11)

    print(f'#{x+1} {a} {b} {c} {d} {e}')