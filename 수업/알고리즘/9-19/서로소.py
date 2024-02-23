def union(x, y):
    xr = find_set(x)
    yr = find_set(y)

    p[xr] = yr


def find_set(x):
    if x == p[x]:
        return x

    p[x] = find_set(p[x])
    return p[x]

print(find_set(1))
print(find_set(2))
union(1, 2)
print(find_set(1))
print(find_set(2))