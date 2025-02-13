# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = []
        i = 0
        while i*i <= c:
            squares.append(i*i)
            i+=1

        left, right = 0,len(squares)-1
        while left<=right:
            _sum = squares[left] + squares[right]
            if _sum > c:
                right-=1
            elif _sum < c:
                left+=1
            else:
                return True
        return False

