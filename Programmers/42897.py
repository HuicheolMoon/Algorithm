# Problem : https://programmers.co.kr/learn/courses/30/lessons/42897
# Date : 2022-03-14
# 도둑질

def solution(money):
    n = len(money)
    dpy = [[0, 0] for _ in range(n)] # 첫 집을 털었을 때 돈의 최댓값 (해당 집을 털었을 때 0, 아닐 때 1)
    dpn = [[0, 0] for _ in range(n)] # 첫 집을 안 털었을 때 돈의 최댓값 (해당 집을 털었을 때 0, 아닐 때 1)
    dpy[0][0] = money[0]
    dpy[1][1] = money[0]
    dpn[1][0] = money[1]
    for i in range(2, n-1):
        dpy[i][0] = max(dpy[i-2]) + money[i]
        dpy[i][1] = max(dpy[i-1])
        dpn[i][0] = max(dpn[i-2]) + money[i]
        dpn[i][1] = max(dpn[i-1])
    dpy[n-1][1] = max(dpy[n-2])
    dpn[n-1][0] = max(dpn[n-3]) + money[n-1]
    answer = max(dpy[n-1] + dpn[n-1])
    return answer
