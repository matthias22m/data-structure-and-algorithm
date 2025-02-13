# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        longest = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in unique:
                unique.add(s[right])
                right+=1
            else:
                unique.remove(s[left])
                left+=1
            longest = max(len(unique),longest)
        return longest