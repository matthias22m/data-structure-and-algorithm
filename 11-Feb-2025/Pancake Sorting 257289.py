# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def reverse(self, arr: List[int], indx: int, rev_ind: int, ans: List[int]) -> None:
        ans.append(indx+1)
        i = 0
        while i<indx:
            arr[i],arr[indx] = arr[indx],arr[i]
            i+=1
            indx-=1
        indx = rev_ind-1
        ans.append(indx+1)
        i = 0
        while i<indx:
            arr[i],arr[indx] = arr[indx],arr[i]
            i+=1
            indx-=1

    def pancakeSort(self, arr: List[int]) -> List[int]:
        el = -1
        maxi = len(arr)
        ans = []
        while maxi> 1 :
            if maxi == arr[el]:
                el -= 1
                maxi -= 1
            indx = arr.index(maxi)
            self.reverse(arr,indx,maxi,ans)
        return ans
            
