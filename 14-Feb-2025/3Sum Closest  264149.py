# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = inf
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                _sum = nums[left]+nums[right]+nums [i]

                if abs(target - closest) > abs(target-_sum):
                    closest = _sum
                if _sum>target:
                    right-=1
                elif _sum<target:
                    left+=1
                else:
                    return _sum
        return closest


                    