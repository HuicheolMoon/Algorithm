# Problem : https://leetcode.com/problems/group-anagrams/
# Date : 2021-06-02


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anans = defaultdict(list)
        for char in strs:
            key = "".join(sorted(char))
            anans[key].append(char)
        return list(anans.values())
