# Problem : https://programmers.co.kr/learn/courses/30/lessons/12982
# Date : 2021-10-19
# Summer/Winter Coding(~2018): 예산

def solution(d, budget):
    d.sort()
    answer = 0
    for req in d:
        if budget < req:
            break
        else:
            budget -= req
            answer += 1
    return answer
