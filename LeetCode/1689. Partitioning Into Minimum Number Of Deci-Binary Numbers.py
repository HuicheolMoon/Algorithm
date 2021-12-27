# Problem : https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# Date : 2021-12-28


class Solution:
    def minPartitions(self, n: str) -> int:
        for i in range(9, 0, -1):
            if str(i) in n:
                return i
