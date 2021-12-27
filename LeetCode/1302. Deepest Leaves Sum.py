# Problem : https://leetcode.com/problems/deepest-leaves-sum/
# Date : 2021-12-28


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        return self.nextLeavesSum([root])

    def nextLeavesSum(self, leaves: List[TreeNode]) -> int:
        nextLeaves = []
        for leaf in leaves:
            nextLeaves.extend([x for x in [leaf.left, leaf.right] if x != None])
        if not nextLeaves:
            return sum([leaf.val for leaf in leaves])
        return self.nextLeavesSum(nextLeaves)
