# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        st = []
        for num in nums2:
            while st and st[-1] < num:
                next_greater[st[-1]] = num
                st.pop()
            st.append(num)
        ans = []
        for num in nums1:
            ans.append(next_greater.get(num,-1))
        return ans