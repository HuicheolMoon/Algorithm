# Problem : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Date : 2021-05-20


from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        cands = [phone_dict[digit] for digit in digits]
        answer = ["".join(x) for x in product(*cands) if len(x) != 0]
        return answer
