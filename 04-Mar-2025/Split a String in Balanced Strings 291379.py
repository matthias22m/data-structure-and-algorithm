# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        l = 0
        count = 0
        for i in range(len(s)):
            if s[i] == 'R':
                r+=1
            else:
                l+=1

            if l == r:
                count+=1
                l=0
                r=0
        return count
            