# Problem : https://programmers.co.kr/learn/courses/30/lessons/81301
# Date : 2021-10-18
# 2021 카카오 채용연계형 인턴십: 숫자 문자열과 영단어
# 구현

def solution(s):
    alpha_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                  "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    answer = ""
    part = ""
    for char in s:
        if char.isalpha():
            part += char
            if part in alpha_dict:
                answer += alpha_dict[part]
                part = ""
            continue
        # digit
        answer += char
    answer = int(answer)
    return answer
