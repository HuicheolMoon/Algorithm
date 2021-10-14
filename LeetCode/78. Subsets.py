# Problem : https://leetcode.com/problems/subsets/
# Date : 2021-10-15


from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        max_length = len(nums)
        for i in range(max_length + 1):
            result.extend(list(combinations(nums, i)))
        return result
