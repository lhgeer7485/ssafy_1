numbers = set(range(1, 10001))
inits = set()



for a in range(1, 10001):
    sum = a
    for b in str(a):
        sum += int(b)
    inits.add(sum)

result = sorted(numbers - inits)

for x in result:
    print(x)