# Problem : https://programmers.co.kr/learn/courses/30/lessons/84512
# Date : 2021-11-14
# 위클리 챌린지: 모음사전

def solution(word):
    word_dict = ["A", "E", "I", "O", "U"]
    pivot = 0
    answer = 0
    for _ in range(len(word_dict)):
        pivot = 5 * pivot + 1
    for char in word:
        if char == " ":
            return answer
        index = word_dict.index(char)
        answer += pivot * index + 1
        pivot = (pivot - 1) // 5
    return answer
