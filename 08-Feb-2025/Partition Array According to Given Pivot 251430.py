# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        gt = []
        lt = []
        count = nums.count(pivot)
        for num in nums:
            if num > pivot:
                gt.append(num)
            elif num < pivot:
                lt.append(num)
        ans = []
        for i in lt:
            ans.append(i)
        for i in range(count):
            ans.append(pivot)
        for i in gt:
            ans.append(i)
        return ans
            
