# Problem : https://programmers.co.kr/learn/courses/30/lessons/12981
# Date : 2021-10-19
# Summer/Winter Coding(~2018): 영어 끝말잇기

def solution(n, words):
    count = 0
    number = 0
    turn = 0
    index = words[0][0]
    used_words = []
    for word in words:
        if (word in used_words) or (word[0] != index) or (len(word) == 1):
            number = count % n + 1
            turn = count // n + 1
            break
        else:
            used_words.append(word)
            index = word[-1]
            count += 1
    answer = [number, turn]
    return answer
