# Problem : https://programmers.co.kr/learn/courses/30/lessons/49191
# Date : 2021-10-03
# 순위

from collections import defaultdict

def solution(n, results):
    answer = 0
    graph = defaultdict(list)
    for win, lose in results:
        graph[win].append(lose)
    connects = [[False for _ in range(n)] for _ in range(n)]
    for x in range(n):
        connects[x][x] = True
    for winner, losers in graph.items():
        for loser in losers:
            connects[winner - 1][loser - 1] = True
    for mid in range(n):
        for win in range(n):
            for lose in range(n):
                if connects[win][mid] and connects[mid][lose]:
                    connects[win][lose] = True
    for j in range(n):
        for idx in [i for i, y in enumerate(connects[j]) if not y]:
            if not connects[idx][j]:
                break
        else:
            answer += 1
    return answer
