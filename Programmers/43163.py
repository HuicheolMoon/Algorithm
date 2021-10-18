# Problem : https://programmers.co.kr/learn/courses/30/lessons/43163
# Date : 2021-10-03
# 단어 변환

from collections import Counter


def trans_cands(begin, words):
    result = []
    mod = Counter(begin)
    for word in words:
        var = list((mod - Counter(word)).values())
        if len(var) == 1 and var[0] == 1:
            result.append(word)
    return result


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    discover = [begin]
    queue = [[begin, 0]]
    while queue:
        start = queue.pop(0)
        if start[0] == target:
            answer = start[1]
            break
        cands = trans_cands(start[0], words)
        for cand in cands:
            if cand not in discover:
                discover.append(cand)
                queue.append([cand, start[1] + 1])
    return answer
