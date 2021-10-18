# Problem : https://programmers.co.kr/learn/courses/30/lessons/77484
# Date : 2021-10-18
# 2021 Dev-Matching: 웹 백엔드 개발자: 로또의 최고 순위와 최저 순위
# 구현

def solution(lottos, win_nums):
    stand = len(set(lottos) & set(win_nums))
    unknown = 0
    var = lottos.count(unknown)
    answer = [rank(stand+var), rank(stand)]
    return answer


def rank(n):
    min_rank = 6
    result = min(min_rank + 1 - n, min_rank)
    return result
