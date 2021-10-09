# Problem : https://programmers.co.kr/learn/courses/30/lessons/49189
# Date : 2021-10-04
# 가장 먼 노드

from collections import defaultdict

def solution(n, edge):
    vertex = defaultdict(list)
    discover = [False for _ in range(n+1)]
    distances = [0] + [float("inf") for _ in range(n)]
    for line in edge:
        vertex[line[0]].append(line[1])
        vertex[line[1]].append(line[0])
    queue = []
    queue.append([1, 0])
    while queue:
        start = queue.pop(0)
        if start[1] < distances[start[0]]:
            distances[start[0]] = start[1]
        for dest in vertex[start[0]]:
            if not discover[dest]:
                discover[dest] = True
                end = [dest, start[1] + 1]
                queue.append(end)
    answer = distances.count(max(distances))
    return answer