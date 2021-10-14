# 카드 정렬하기
# Problem : https://www.acmicpc.net/problem/1715
# Date : 2021-10-15

import sys
import heapq


n = int(sys.stdin.readline())
card_packs = [int(sys.stdin.readline()) for _ in range(n)]
heapq.heapify(card_packs)
answer = 0
while len(card_packs) > 1:
    min_pack = heapq.heappop(card_packs)
    next_min_pack = heapq.heappop(card_packs)
    new_pack = min_pack + next_min_pack
    answer += new_pack
    heapq.heappush(card_packs, new_pack)
print(answer)
