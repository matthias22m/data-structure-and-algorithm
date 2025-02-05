# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        major = len(nums)//3
        ans = []
        for num, freq in count.items():
            if freq > major:
                ans.append(num)
        return ans
