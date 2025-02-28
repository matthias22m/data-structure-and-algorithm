# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        p1,p2 = 0,len(people)-1
        boat =0
        while p1<p2:
            if people[p1]+people[p2] <= limit:
                p1+=1
                p2-=1
                boat+=1
            else:
                boat+=1
                p2-=1
           
        if p1 == p2: 
            boat+=1

        return boat