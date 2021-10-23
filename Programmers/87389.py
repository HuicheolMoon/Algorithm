# Problem : https://programmers.co.kr/learn/courses/30/lessons/87389
# Date : 2021-10-23
# 나머지가 1이 되는 수 찾기

def solution(n):
    answer = n - 1
    for x in range(2, n):
        if (n - 1) % x == 0:
            return x
    return answer

