# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx = deque()
        mn = deque()
        max_len = 0
        right = 0
        left = 0
        while right < len(nums):
            while mx and nums[right] > mx[-1]:
                mx.pop()
            mx.append(nums[right])
            
            while mn and nums[right] < mn[-1]:
                mn.pop()
            mn.append(nums[right])
                

            while mx[0] - mn[0] > limit:
                if mx[0] == nums[left]:
                    mx.popleft()
                if mn[0] == nums[left]:
                    mn.popleft()
                left+=1
            max_len = max(max_len,right-left+1)
            right += 1

        return max_len

