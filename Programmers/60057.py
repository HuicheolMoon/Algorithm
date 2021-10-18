# Problem : https://programmers.co.kr/learn/courses/30/lessons/60057
# Date : 2021-09-03
# 2020 KAKAO BLIND RECRUITMENT - 문자열 압축

def solution(s):
    answer = len(s)
    for n in range(1, len(s) // 2 + 1):
        answer = min(answer, n_zip_str(s, n))
    return answer

def n_zip_str(s, n):
    idx = 0
    lng = n
    mul = 1
    result = 0
    while idx + lng <= len(s):
        word = s[idx:idx+lng]
        next_word = s[idx+lng:idx+(lng*2)]
        if word == next_word:
            mul += 1
        else:
            if mul > 1:
                result += len(str(mul)) + lng
            else:
                result += lng
            mul = 1
        idx += lng
    result += len(s[idx:])
    return result

