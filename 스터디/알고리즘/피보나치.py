T = int(input())
data = []
for x in range(T):
    data.append(int(input()))
    
def fnc(n):
    zero = [1, 0, 1]
    one = [0, 1, 1]

    if n == 0:
        return zero, one    
    elif n == 1:
        return zero, one
    elif n == 2:
        return zero, one

    else:
        for x in range(3, n+1):
            zero.append(zero[x-1] + zero[x-2])
            one.append(one[x-1] + one[x-2])

    return zero, one
    
for x in data:
    zero, one = fnc(x)
    print(f'{zero[x]} {one[x]}')