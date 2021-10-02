# Problem : https://programmers.co.kr/learn/courses/30/lessons/42628
# Date : 2021-10-03
# 이중우선순위큐

import heapq

def solution(operations):
    q = []
    for x in operations:
        op = x.split()
        if op[0] == "I":
            heapq.heappush(q, int(op[1]))
        elif not q:
            continue
        elif op[0] == "D" and op[1] == "1":
            q = heapq.nlargest(len(q), q)[1:]
            heapq.heapify(q)
        elif op[0] == "D" and op[1] == "-1":
            heapq.heappop(q)
        else:
            return "Failure"
    answer = [max(q), min(q)] if q else [0, 0]
    return answer
