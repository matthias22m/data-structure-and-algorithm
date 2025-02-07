# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.append(-1)
        for i in range(len(arr)-1,0,-1):
            if arr[i] > arr[i-1]:
                arr[i-1] = arr[i]
        return arr[1:]