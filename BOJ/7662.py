# 이중 우선순위 큐
# Problem : https://www.acmicpc.net/problem/7662
# Date : 2022-01-03

import heapq
import sys


T = int(sys.stdin.readline())
for _ in range(T):
    max_heap = []
    min_heap = []
    k = int(sys.stdin.readline())
    visited = [False for _ in range(k)]
    for i in range(k):
        operation = sys.stdin.readline().split()
        if operation[0] == "I":
            heapq.heappush(max_heap, (-int(operation[1]), i))
            heapq.heappush(min_heap, (int(operation[1]), i))
            visited[i] = True
        elif operation[0] == "D" and operation[1] == "1":
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                visited[heapq.heappop(max_heap)[1]] = False
        elif operation[0] == "D" and operation[1] == "-1":
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[heapq.heappop(min_heap)[1]] = False
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    result = "EMPTY"
    if max_heap and min_heap:
        result = f"{-max_heap[0][0]} {min_heap[0][0]}"
    print(result)
