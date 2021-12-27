# Problem : https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
# Date : 2021-12-28


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for x, y, r in queries:
            count = 0
            for z, w in points:
                if self.in_circle(x, y, r, z, w):
                    count += 1
            answer.append(count)
        return answer

    def in_circle(self, x: int, y: int, r: int, z: int, w: int) -> bool:
        return (x - z) * (x - z) + (y - w) * (y - w) <= r * r
