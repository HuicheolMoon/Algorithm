# Problem : https://programmers.co.kr/learn/courses/30/lessons/83201
# Date : 2021-10-19
# 위클리 챌린지: 2주차_상호평가

def solution(scores):
    answer = ""
    n = len(scores)
    for i in range(n):
        evals = [review[i] for review in scores]
        max_score = max(evals)
        min_score = min(evals)
        unique_max = (evals.count(max_score) == 1)
        unique_min = (evals.count(min_score) == 1)
        if (evals[i] == max_score and unique_max) or (evals[i] == min_score and unique_min):
            evals.remove(evals[i])
        avgs = sum(evals) / len(evals)
        grade = getGrade(avgs)
        answer += grade
    return answer


def getGrade(score):
    if score >= 90:
        grade = "A"
    elif 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    elif 50 <= score < 70:
        grade = "D"
    elif score < 50:
        grade = "F"
    else:
        grade = "X"
    return grade
