# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def isPalindrome(self, substr: str) -> bool:
        left = 0
        right = len(substr)-1
        while left < right:
            if substr[left] != substr[right]:
                return False
            left+=1
            right-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        count = 0
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
                continue
            left_check = self.isPalindrome(s[left:right])
            right_check = self.isPalindrome(s[left+1:right+1])
                
            return left_check or right_check
                
                
            
        return True



            