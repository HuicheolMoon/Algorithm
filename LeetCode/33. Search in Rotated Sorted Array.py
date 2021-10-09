# Problem : https://leetcode.com/problems/search-in-rotated-sorted-array/
# Date : 2021-06-02


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)
