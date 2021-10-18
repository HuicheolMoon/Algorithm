# Problem : https://programmers.co.kr/learn/courses/30/lessons/1845
# Date : 2021-10-18
# 찾아라 프로그래밍 마에스터: 폰켓몬

def solution(nums):
    answer = min(len(nums) // 2, len(set(nums)))
    return answer
