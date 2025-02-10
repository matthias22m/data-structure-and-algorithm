# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            for j in range(i+1,len(names)):
                if heights[i] < heights[j]:
                    names[i],names[j] = names[j],names[i]
                    heights[i],heights[j] = heights[j],heights[i]
                    
        return names