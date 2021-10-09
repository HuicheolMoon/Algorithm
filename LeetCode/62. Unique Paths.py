# Problem : https://leetcode.com/problems/unique-paths/
# Date : 2021-10-09


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer = self.combination(m + n - 2, n - 1)
        return answer

    def combination(self, p, k):
        # p >= k
        result = 1
        if k == 0:
            return result
        result = self.rangeMulti(p - k + 1, p) // self.rangeMulti(1, k)
        return result

    def rangeMulti(self, a, b):
        # a <= b
        result = 1
        for i in range(a, b + 1):
            result *= i
        return result
