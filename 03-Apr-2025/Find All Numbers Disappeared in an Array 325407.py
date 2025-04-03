# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        pointer = 0
        ans = []
        while pointer < len(nums):
            correct_val = nums[pointer] - 1

            if pointer != correct_val and not (nums[correct_val] == correct_val+1):
                nums[pointer],nums[correct_val] = nums[correct_val],nums[pointer]
            else:
                pointer += 1
                
        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans.append(i+1)
        return ans