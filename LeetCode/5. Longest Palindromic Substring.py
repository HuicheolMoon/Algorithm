# Problem : https://leetcode.com/problems/longest-palindromic-substring/
# Date : 2021-04-23


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n, 0, -1):  # n to 1 (part length)
            for j in range(0, n - i + 1):  # [0] to [0 ~ n-1] (start index)
                part = s[j:j + i]
                if self.is_palindrom(part):
                    return part

    def is_palindrom(self, s: str) -> bool:
        return True if s == s[::-1] else False
