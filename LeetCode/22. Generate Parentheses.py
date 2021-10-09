# Problem : https://leetcode.com/problems/generate-parentheses/
# Date : 2021-06-02


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = set([])
        if n == 1:
            answer = ["()"]
            return answer
        for i in range(1, n//2+1):
            left = self.generateParenthesis(i)
            right = self.generateParenthesis(n-i)
            for l in left:
                for r in right:
                    part = [r + l, l + r]
                    answer.update(part)
        cands = self.generateParenthesis(n-1)
        for cand in cands:
            new = "(" + cand + ")"
            answer.add(new)
        answer = list(answer)
        return answer
