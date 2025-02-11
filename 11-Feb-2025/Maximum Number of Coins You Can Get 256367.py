# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        j = len(piles)-1
        ans = 0
        for i in range(0,len(piles)-1,2):
            if i >= j:
                break
            ans+= piles[i+1]
            j-=1
        return ans  
