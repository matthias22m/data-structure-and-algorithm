# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target > 1 and maxDoubles != 0:
            if target%2 == 0:
                maxDoubles -= 1
                target //= 2
                count += 1
            else:
                target = (target-1)//2
                maxDoubles -= 1
                count+=2
        count += target-1
        return count