# Problem : https://programmers.co.kr/learn/courses/30/lessons/17684
# Date : 2021-09-03
# 2018 KAKAO BLIND RECRUITMENT [3차] 압축

import string


def solution(msg):
    answer = []
    N = len(msg)
    zip_dict = [" "]
    zip_dict.extend(list(string.ascii_uppercase))
    idx = 0
    length = 1
    while idx + length <= N:
        word = msg[idx:idx+length]
        if word in zip_dict:
            length += 1
        else:
            zip_dict.append(word)
            word = word[:-1]
            answer.append(zip_dict.index(word))
            idx += length -1
            length = 1
    answer.append(zip_dict.index(word))
    return answer
