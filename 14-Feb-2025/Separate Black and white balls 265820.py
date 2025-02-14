# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        prev_one = 0
        whites = 0
        for ind in range(len(s)):
            if s[ind] == '0':
                whites += prev_one
            else:
                prev_one += 1
        return whites
