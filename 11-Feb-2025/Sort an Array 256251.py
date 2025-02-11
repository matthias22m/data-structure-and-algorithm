# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maxi,mini = max(nums),abs(min(nums))
        ans = []

        arr = [0]*(maxi+mini+1)
        for num in nums:
            arr[num+mini] += 1

        for i in range(len(arr)):
            for j in range(arr[i]):
                ans.append(i-mini)
            

        return ans