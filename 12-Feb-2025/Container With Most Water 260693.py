# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        vol = 0
        while left<right:
            new_vol = min(height[left],height[right]) * (right-left)
            vol = max(new_vol,vol)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return vol