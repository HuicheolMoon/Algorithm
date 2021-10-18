# Problem : https://programmers.co.kr/learn/courses/30/lessons/43162
# Date : 2021-10-03
# 네트워크

def dfs(start):
    visited[start] = True
    for dest, able in enumerate(edge[start]):
        if able and not visited[dest]:
            dfs(dest)


def solution(n, computers):
    global edge, visited
    edge = computers
    visited = [False for _ in range(n)]
    answer = 0
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    return answer
