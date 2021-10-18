# Problem : https://programmers.co.kr/learn/courses/30/lessons/42627
# Date : 2021-10-03
# 디스크 컨트롤러

import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    time = 0
    n = len(jobs)
    tasks = []
    answer = 0
    while jobs or tasks:
        while jobs and jobs[0][0] <= time:
            job = jobs.pop(0)
            heapq.heappush(tasks, (job[1], job[1] - job[0]))
        if tasks:
            task = heapq.heappop(tasks)
            answer += time + task[1]
            time += task[0]
        else:
            time += 1
    return answer // n

