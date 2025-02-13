# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ln = len(s1)
        count = Counter(s1)
        
        for i in range(len(s2)-ln+1):
            if s2[i] in count:
                if Counter(s2[i:i+ln]) == count:
                    return True
            
            
        return False