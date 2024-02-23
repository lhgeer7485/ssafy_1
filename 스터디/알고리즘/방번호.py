N = input()
data = []

for x in N:
    data.append(int(x))

counts = [0] * 10

for x in data:
    if x == 9:
        counts[6] += 1
    else:
        counts[x] += 1

max = 0

for x in range(len(counts)):
    
    if x == 6:
        m = counts[x]
        if m % 2 == 0:
            m //= 2
        else:
            m //= 2
            m += 1
    else:
        if counts[x] > counts[max]:
            max = x

if counts[max] < m:
    result = m
else:
    result = counts[max]


print(result)

