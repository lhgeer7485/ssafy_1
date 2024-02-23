T = int(input())

for text_case in range(T):
    N = int(input())
    result = []

    bus_routes = [(list(map(int, input().split()))) for _ in range(N)]
    
    P = int(input())
    counts = [0] * P

    bus_stations = [int(input()) for _ in range(P)]

    for a in range(N):
        for point in range(bus_routes[a][0]-1, bus_routes[a][1]):
            counts[point] += 1

    

    for x in bus_stations:
        result.append(counts[x-1])

    print(f'#{text_case + 1}', *result)