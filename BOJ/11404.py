# 플로이드
# Problem : https://www.acmicpc.net/problem/11404
# Date : 2021-10-22

from copy import deepcopy
import sys


def floyd_warshall(graph):
    k = len(graph)
    distances = deepcopy(graph)
    for mid in range(k):
        for start in range(k):
            for dest in range(k):
                if start == dest:
                    distances[start][dest] = 0
                    continue
                new_dist = distances[start][mid] + distances[mid][dest]
                if distances[start][dest] > new_dist:
                    distances[start][dest] = new_dist
    for i in range(k):
        for j in range(k):
            if distances[i][j] == float("inf"):
                distances[i][j] = 0
    return distances


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[float("inf") for _ in range(n)] for __ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
distances = floyd_warshall(graph)
for low in distances:
    result = " ".join([str(x) for x in low])
    print(result)
