T = int(input())

data = []


for x in range(T):
    data.append(input().split())




for x in range(T):
    st = ''
    for a in range(len(data[x][1])):
        for b in range(int(data[x][0])):
            st += data[x][1][a]
    print(st)        