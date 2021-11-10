# Problem : https://programmers.co.kr/learn/courses/30/lessons/77885
# Date : 2021-11-10
# 월간 코드 챌린지 시즌2: 2개 이하로 다른 비트

def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
            continue
        bin_num = "0" + bin(number)[2:]
        index = len(bin_num) - bin_num[::-1].index("0") - 1
        f_bin_num = bin_num[:index] + bin_num[index:index+2][::-1] + bin_num[index+2:]
        answer.append(int("0b" + f_bin_num, 2))
    return answer
