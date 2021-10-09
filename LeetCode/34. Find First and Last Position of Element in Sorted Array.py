# Problem : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Date : 2021-06-02


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        rev_nums = nums[:]
        rev_nums.reverse()
        return [nums.index(target), len(nums) - rev_nums.index(target) - 1]
