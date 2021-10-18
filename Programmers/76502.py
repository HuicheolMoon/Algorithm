# Problem : https://programmers.co.kr/learn/courses/30/lessons/76502
# Date : 2021-10-19
# 월간 코드 챌린지 시즌2: 괄호 회전하기

def is_correct(s):
    stack = []
    bracket_dict = {"]": "[", ")": "(", "}": "{"}
    for char in s:
        if char in "[({":
            stack.append(char)
        elif len(stack) == 0 or bracket_dict[char] != stack[-1]:
            return False
        else:
            stack.pop()
    return True if len(stack) == 0 else False


def solution(s):
    answer = 0
    for i in range(len(s)):
        if is_correct(s):
            answer += 1
        s = s[1:] + s[0]
    return answer
