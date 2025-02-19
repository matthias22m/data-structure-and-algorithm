# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alpha = [chr(i+97) for i in range(26)]
        s = list(s)
        prefix = [0]*(len(s)+1)

        for left,right,val in shifts:
            val = 1 if val == 1 else -1
            prefix[left] += val
            prefix[right+1] -= val
        
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        
        for i in range(len(s)):
            ind = ((ord(s[i])-97)+prefix[i])%26
            s[i] = alpha[ind]
        return ''.join(s)

        
