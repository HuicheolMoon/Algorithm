# Problem : https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
# Date : 2021-12-28


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ball_indices = [i for i in range(len(boxes)) if boxes[i] == "1"]
        return [sum([abs(j-index) for index in ball_indices]) for j in range(len(boxes))]
