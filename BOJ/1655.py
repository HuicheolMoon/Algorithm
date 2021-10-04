# 가운데를 말해요
# Problem : https://www.acmicpc.net/problem/1655
# Date : 2020-02-26

import sys
import heapq

n = int(sys.stdin.readline())
q_max = []
q_min = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(q_max) == 0:
        heapq.heappush(q_max, -num)
    elif len(q_max) == len(q_min) and num < q_min[0]:
        heapq.heappush(q_max, -num)
    elif len(q_max) == len(q_min):
        heapq.heappush(q_max, -heapq.heappop(q_min))
        heapq.heappush(q_min, num)
    elif num < -q_max[0]:
        heapq.heappush(q_min, -heapq.heappop(q_max))
        heapq.heappush(q_max, -num)
    else:
        heapq.heappush(q_min, num)
    print(-q_max[0])
