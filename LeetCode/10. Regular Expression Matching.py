# Problem : https://leetcode.com/problems/regular-expression-matching/
# Date : 2021-04-25


import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = re.compile(p)
        return True if pattern.fullmatch(s) else False
