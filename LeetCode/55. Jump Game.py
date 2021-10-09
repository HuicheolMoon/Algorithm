# Problem : https://leetcode.com/problems/jump-game/
# Date : 2021-06-02


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ai = 0
        for ci in range(len(nums)):
            if ci != 0 and ai < ci:
                return False
            ali = ci + nums[ci]
            if ai < ali:
                ai = ali
            if len(nums)-1 <= ali:
                return True
        return False
