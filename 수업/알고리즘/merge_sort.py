def merge_sort(left, right):
    if left == right:
        return

    mid = (right + left) // 2

    merge_sort(left, mid)
    merge_sort(mid + 1, right)

    i = left
    j = mid + 1
    tmp = []

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= mid:
        tmp.append(arr[i])
        i += 1

    while j <= right:
        tmp.append(arr[j])
        j += 1

    j = 0
    for i in range(left, right + 1):
        arr[i] = tmp[j]
        j += 1


arr = [7, 5, 4, 1, 2, 10, 3, 6, 9, 8]
merge_sort(0, len(arr) - 1)
print(arr)
