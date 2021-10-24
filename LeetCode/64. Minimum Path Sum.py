# Problem : https://leetcode.com/problems/minimum-path-sum/
# Date : 2021-10-24

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for __ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m + n - 1):
            for y in range(i+1):
                x = i - y
                if x < 0 or x >= n or y >= m:
                    continue
                if x == 0:
                    dp[y][x] = grid[y][x] + dp[y-1][x]
                elif y == 0:
                    dp[y][x] = grid[y][x] + dp[y][x-1]
                else:
                    dp[y][x] = grid[y][x] + min(dp[y-1][x], dp[y][x-1])
        return dp[m-1][n-1]
