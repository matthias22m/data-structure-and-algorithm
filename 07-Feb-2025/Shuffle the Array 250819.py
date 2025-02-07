# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n
        new_nums=[]
        while i<n and j< 2*n:
            new_nums.append(nums[i])
            new_nums.append(nums[j])
            i+=1
            j+=1
        return new_nums
