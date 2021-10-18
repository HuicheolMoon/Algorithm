# Problem : https://programmers.co.kr/learn/courses/30/lessons/1844
# Date : 2021-10-19
# 찾아라 프로그래밍 마에스터: 게임 맵 최단거리

from collections import deque


def solution(maps):
    answer = -1
    height = len(maps)
    width = len(maps[0])
    queue = deque([[[0, 0], 1]]) # [y, x]
    visited = [[False for _ in range(width)] for _ in range(height)]
    visited[0][0] = True
    while queue:
        cur_loc, dist = queue.popleft()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_y = cur_loc[0] + dy
            next_x = cur_loc[1] + dx
            if (0 <= next_y <= height - 1) and (0 <= next_x <= width - 1) and (maps[next_y][next_x] == 1) and not visited[next_y][next_x]:
                next_loc = [next_y, next_x]
                visited[next_y][next_x] = True
                if next_loc == [height - 1, width - 1]:
                    answer = dist + 1
                    return answer
                else:
                    queue.append([next_loc, dist+1])
    return answer
