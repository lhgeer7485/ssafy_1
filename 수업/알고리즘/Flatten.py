def my_max_index(data):
    max = data[0]
    index = 0
    for x in range(len(data)):
        if max < data[x]:
            max = data[x]
            index = x

    return index

def my_min_index(data):
    min = data[0]
    index = 0
    for x in range(len(data)):
        if min > data[x]:
            min = data[x]
            index = x

    return index

for x in range(10):
    dump = int(input())
    data = list(map(int, input().split()))

    for a in range(dump):
        data[my_max_index(data)] -= 1
        data[my_min_index(data)] += 1

    result = data[my_max_index(data)] - data[my_min_index(data)]

    print(f'#{x+1} {result}')