data = [0, 4, 1, 3, 1, 2, 4, 1]

max_data = data[0]

new_data = [0] * len(data)

for x in range(1, len(data)):
    if max_data < data[x]:
        max_data = data[x]


counts = [0] * (max_data + 1)

for x in data:
    counts[x] += 1

for x in range(1, len(counts)):
    counts[x] += counts[x-1]

for x in reversed(range(len(data))):
    counts[data[x]] -= 1
    new_data[counts[data[x]]] = data[x]

print(new_data)