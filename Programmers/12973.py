# Problem : https://programmers.co.kr/learn/courses/30/lessons/12973
# Date : 2021-10-18
# 2017 팁스타운: 짝지어 제거하기

def solution(s):
    words = [""]
    for char in s:
        if char == words[-1]:
            words.pop()
        else:
            words.append(char)
    return 1 if len(words) == 1 else 0
