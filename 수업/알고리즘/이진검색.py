data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def search(data, key):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == key:
            return True
        elif data[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return False

print(search(data, 2))
