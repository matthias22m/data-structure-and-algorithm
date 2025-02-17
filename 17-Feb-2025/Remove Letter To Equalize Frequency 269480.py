# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        for ind in range(len(word)):
            wd = word[:ind] + word[ind+1:]  
            count = Counter(wd)
            if len(set(count.values())) == 1: 
                return True
        return False