# Problem : https://programmers.co.kr/learn/courses/30/lessons/84512
# Date : 2021-11-14
# 위클리 챌린지: 모음사전

def solution(word):
    word_dict = ["A", "E", "I", "O", "U"]
    new_word = word + " " * (len(word_dict) - len(word))
    pivot = 0
    for _ in range(len(word_dict)):
        pivot = 5 * pivot + 1
    answer = pivot * word_dict.index(new_word[0]) + 1
    pivot = (pivot - 1) // 5
    for char in word[1:]:
        if char == " ":
            return answer
        index = word_dict.index(char)
        answer += pivot * index + 1
        pivot = (pivot - 1) // 5
    return answer
