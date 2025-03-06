# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        end_max = -inf
        overlap = 0
        points.sort(key=lambda p:p[1])
        for start,end in points:
            if start > end_max:
                end_max = end
                overlap += 1
        return overlap
            