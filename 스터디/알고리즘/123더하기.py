T = int(input())

def fnc(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return fnc(n-1) + fnc(n-2) + fnc(n-3)


for x in range(T):
    data = int(input())
    print(fnc(data))

