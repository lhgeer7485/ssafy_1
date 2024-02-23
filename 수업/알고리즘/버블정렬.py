data = [55, 7, 78, 12,42]

for a in reversed(range(len(data))):

    for b in range(0, a):
        if data[b] > data[b+1]:
            data[b], data[b+1] = data[b+1], data[b]

print(data)