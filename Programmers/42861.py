# Problem : https://programmers.co.kr/learn/courses/30/lessons/42861
# Date : 2021-10-03
# 섬 연결하기

def solution(n, costs):
    uf = list(range(n))
    costs.sort(key=lambda x: x[2])
    answer = 0
    count = 0
    while count < n-1:
        start, end, cost = costs.pop(0)
        if uf[start] != uf[end]:
            maxh, minh = max(uf[start], uf[end]), min(uf[start], uf[end])
            for i in range(len(uf)):
                if uf[i] == maxh:
                    uf[i] = minh
            answer += cost
            count += 1
    return answer

