# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        ans = []
        for candy in candies:
            if max_candies - candy <= extraCandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans