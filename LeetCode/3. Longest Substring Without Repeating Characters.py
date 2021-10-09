# Problem : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Date : 2021-04-23


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        sent = ""
        for char in s:
            if char not in sent:
                sent = char + sent
                l += 1
            else:
                max_len = max(max_len, l)
                sent = char + sent[:sent.index(char)]
                l = len(sent)
        max_len = max(max_len, l)
        return max_len
