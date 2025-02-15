# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        index1 = 0
        index2 = 0
         
        ans = []
        while index1 < len(A) and index2 < len(B):
            first_start, first_end = A[index1]
            second_start, second_end = B[index2]
            if first_start <= second_end and second_start <= first_end:
                ans.append([max(first_start, second_start), min(first_end, second_end)])
                
            if first_end <= second_end: 
                index1 += 1
            else:
                index2 += 1
        return ans