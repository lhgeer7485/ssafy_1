data = [20, 7, 23, 19, 10, 15, 25, 8, 13]

def my_sort(data, N):

    for i in range(N-1):
        min_index = i
        for j in range(i, N):
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

    print(data)


my_sort(data, len(data))