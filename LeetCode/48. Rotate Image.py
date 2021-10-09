# Problem : https://leetcode.com/problems/rotate-image/
# Date : 2021-06-02


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N // 2):
            matrix[i], matrix[N-1-i] = matrix[N-1-i], matrix[i]
        for j in range(N):
            for k in range(j, N):
                matrix[j][k], matrix[k][j] = matrix[k][j], matrix[j][k]
