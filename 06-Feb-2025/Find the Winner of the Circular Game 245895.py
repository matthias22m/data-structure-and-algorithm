# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        people = [i+1 for i in range(n) ]
        st = 0
        for i in range(n):
            if len(people) == 1:
                break
            ind = (k-1+st)%(n-i)
            people.remove(people[ind])
            st=ind
            
        return people[0]
