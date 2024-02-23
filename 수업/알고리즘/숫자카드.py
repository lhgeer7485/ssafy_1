T = int(input())

for x in range(T):
    N = int(input())
    data = input()
    counts = [0] * 10

    for a in data:
        counts[int(a)] += 1
 
    max = counts[0]
    index = 0
    for a in range(len(counts)):
        if max <= counts[a]:
            max = counts[a]
            index = a

    print(f'#{x+1} {index} {max}')