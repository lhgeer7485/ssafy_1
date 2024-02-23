data = list(map(int, input().split()))

def fnc(lst):
    
    if len(lst) < 2:
        return lst
    
    first, secend = lst[:2]

    if first < secend:
        first, secend = secend, first

    for x in range(2, len(lst)):
        if lst[x] > first:
            secend = first
            first = lst[x]
        elif lst[x] > secend:
            secend = lst[x]

    return [first, secend]

print(fnc(data))