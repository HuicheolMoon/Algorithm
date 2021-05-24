import heapq


# 1. Push
def push(heap, x):
    heap.append(x)
    idx = len(heap)-1
    while heap[idx] <= heap[(idx-1) // 2] and idx > 0:
        heap[idx], heap[(idx - 1) // 2] = heap[(idx - 1) // 2], heap[idx]
        idx = (idx - 1) // 2
    return heap


a = [1, 9, 6, 7, 4, 6, 5, 8, 2, 5]
heapq.heapify(a)
print(a)
push(a, 2)
print(a)


# 2. Pop
def pop(heap):
    result = heap[0]
    heap[0] = heap[-1]
    heap = heap[:-1]
    idx = 0
    left = 2 * (idx + 1) - 1
    right = left + 1
    while left <= len(heap) - 1:
        if right <= len(heap) - 1 and heap[idx] > min(heap[left], heap[right]):
            minh = heap.index(min(heap[left], heap[right]))
            heap[idx], heap[minh] = heap[minh], heap[idx]
            idx = minh
        elif right > len(heap) - 1 and heap[idx] > heap[left]:
            heap[idx], heap[left] = heap[left], heap[idx]
            idx = left
        left = 2 * (idx + 1) - 1
        right = left + 1
    print(result)
    return heap


b = [1, 9, 6, 7, 4, 6, 5, 8, 2, 5]
heapq.heapify(b)
print(b)
b = pop(b)
print(b)
