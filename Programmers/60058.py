# Problem : https://programmers.co.kr/learn/courses/30/lessons/60058
# Date : 2021-09-03
# 2020 KAKAO BLIND RECRUITMENT - 괄호 변환

def solution(p):
    # step 1
    if p == "":
        return p
    # step 2
    u, v = bal_sep(p)
    # step 3
    if isvalid(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + clean(u)


def bal_sep(p: str) -> (str, str):
    delta = 0
    idx = len(p) - 1
    for i in range(len(p)):
        if p[i] == "(":
            delta += 1
        else:
            delta -= 1
        if delta == 0:
            idx = i + 1
            break
    return p[:idx], p[idx:]


def isvalid(p: str) -> bool:
    stack = []
    for i in range(len(p)):
        if p[i] == "(":
            stack.append(p[i])
        elif stack:
            stack.pop()
        else:
            return False
    if stack:
        return False
    return True


def clean(p: str) -> str:
    p = p[1:-1]
    answer = ""
    rev_dict = {"(": ")", ")": "("}
    for char in p:
        answer += rev_dict[char]
    return answer

