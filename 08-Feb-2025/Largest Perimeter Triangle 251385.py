# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            j = i+1
            k = i +2
            if nums[j] + nums[k] <= nums[i]:
                continue
            return nums[i]+nums[j]+nums[k]
        return 0

