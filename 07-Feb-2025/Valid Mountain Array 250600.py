# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] > arr[1]: 
            return False
        flag = True
        for i in range(len(arr)-1):
            if flag:
                if arr[i] >= arr[i+1]:
                    flag = False
            if not flag:
                if arr[i] <= arr[i+1]:
                    return False

        if not flag:
            return True

        return False
