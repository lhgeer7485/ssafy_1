def heap_push(data):
    global heap_pointer
    
    heap[heap_pointer] = data

    child = heap_pointer
    parent = child // 2

    while parent > 0:

        if heap[child] < heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]

        child = parent
        parent = child // 2
    heap_pointer += 1



heap = [0] * 101
heap_pointer = 1
heap_push(4)
heap_push(5)
heap_push(3)
heap_push(10)
heap_push(2)

print(heap)