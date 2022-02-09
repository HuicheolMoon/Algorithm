# Problem : https://programmers.co.kr/learn/courses/30/lessons/92342
# Date : 2022-02-09
# 2022 KAKAO BLIND RECRUITMENT: 양궁대회

from collections import deque


def solution(n, info):
    ryan_arrows = [0 for _ in range(len(info))]
    queue = deque([[0, ryan_arrows, n]]) #[쏠 점수(10-i), 각 점수별로 맞춘 화살 개수, 남은 화살 개수]
    wait_queue = []
    while queue:
        if queue[0][0] == 10:
            break
        start = queue.popleft()
        target_score, hit_arrows, rest_arrows = start
        new_target_score = target_score + 1
        # 해당 과녁에서 승리
        if rest_arrows - info[target_score] >= 1:
            new_hit_arrows = hit_arrows[:]
            new_hit_arrows[target_score] = info[target_score] + 1
            new_rest_arrows = rest_arrows - new_hit_arrows[target_score]
            wait_queue.append([new_target_score, new_hit_arrows, new_rest_arrows])
        # 해당 과녁에서 패배
        wait_queue.append([new_target_score, hit_arrows[:], rest_arrows])
        if not queue:
            queue = deque(wait_queue)
            wait_queue = []
    candidates = []
    max_delta = 0
    for case in queue:
        target_score, hit_arrows, rest_arrows = case
        final_hit_arrows = hit_arrows[:]
        final_hit_arrows[-1] += rest_arrows
        delta = score_delta(info, final_hit_arrows)
        if delta > 0:
            candidates.append([final_hit_arrows, delta])
            if delta > max_delta:
                max_delta = delta
    max_cands = []
    for cand in candidates:
        if cand[1] == max_delta:
            max_cands.append(cand[0])
    answer = [-1]
    if not max_cands:
        return answer
    max_cands = sorted([x[::-1] for x in max_cands], reverse=True)
    answer = max_cands[0][::-1]
    return answer


def score_delta(apeach, ryan):
    apeach_score = 0
    ryan_score = 0
    for i, x in enumerate(zip(apeach, ryan)):
        if x[0] == x[1] == 0:
            pass
        elif x[0] >= x[1]:
            apeach_score += (10 - i)
        else:
            ryan_score += (10 - i)
    return ryan_score - apeach_score

