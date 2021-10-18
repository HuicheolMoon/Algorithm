# Problem : https://programmers.co.kr/learn/courses/30/lessons/49994
# Date : 2021-10-19
# Summer/Winter Coding(~2018): 방문 길이

def solution(dirs):
    answer = 0
    move = {"U": [0, 1, "D"], "D": [0, -1, "U"], "R": [1, 0, "L"], "L": [-1, 0, "R"]}
    walked = [[[] for _ in range(11)] for _ in range(11)]
    posit = [5, 5]
    for q in dirs:
        dx, dy, opp = move[q]
        if (0 <= posit[0] + dx <= 10) and (0 <= posit[1] + dy <= 10):
            if q not in walked[posit[1]][posit[0]]:
                walked[posit[1]][posit[0]].append(q)
                walked[posit[1] + dy][posit[0] + dx].append(opp)
                answer += 1
            posit = [posit[0] + dx, posit[1] + dy]
    return answer
