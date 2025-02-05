# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ch = []
        if s1 == s2:
            return True
        
        for ind in range(len(s1)):
            if s1[ind] != s2[ind]:
                ch.append(ind)
            if len(ch) > 2:
                return False
        else:
            if len(ch)==1:
                return False
            return s1[ch[0]] == s2[ch[1]] and s1[ch[1]] == s2[ch[0]]