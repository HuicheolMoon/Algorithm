# Problem : https://programmers.co.kr/learn/courses/30/lessons/17681
# Date : 2020-02-24
# 2018 KAKAO BLIND RECRUITMENT [1차] 비밀지도


def union_arr(n, list1, list2):
    result = []
    # OR 비트 연산으로 지도 겹치기
    for number in [x | y for x, y in zip(list1, list2)]:
        binary_num = bin(number)[2:]    # 이진법 접두열('0b') 제거
        modified_num = "0" * (n - len(binary_num)) + binary_num
        result.append(modified_num)
    return result


def number_to_sharp(arr):
    result = []
    trans_dict = [" ", "#"]
    for low in arr:
        new_word = "".join([trans_dict[int(char)] for char in low])
        result.append(new_word)
    return result


def solution(n, arr1, arr2):
    union = union_arr(n, arr1, arr2)
    answer = number_to_sharp(union)
    return answer
