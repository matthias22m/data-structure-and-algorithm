# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = 0
        for left in range(len(nums)):

            if nums[left] == 0 and left == right:
                return right == len(nums)-1
                
            right = left + nums[left] if left + nums[left] > right else right

            if right >= len(nums) -1:
                return True

        return False

