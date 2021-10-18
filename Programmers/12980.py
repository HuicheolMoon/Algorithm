# Problem : https://programmers.co.kr/learn/courses/30/lessons/12980
# Date : 2021-10-19
# Summer/Winter Coding(~2018): 점프와 순간 이동

def solution(n):
    answer = 0
    while n != 0:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            answer += 1
    return answer
