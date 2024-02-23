def quick_sort(arr, l, r):
    if l >= r:
        return l

    p = partition1(arr, l, r)

    quick_sort(arr, l, p - 1)
    quick_sort(arr, p + 1, r)


def partition1(arr, l, r):
    i = l
    j = r

    pivot = arr[l]

    while i < j:

        while arr[i] <= pivot and i < r:
            i += 1
        while arr[j] >= pivot and j > l:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[l], arr[j] = arr[j], arr[l]

    return j


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, N-1)
    #print(arr)
    print(f'#{tc} {arr[N//2]}')
