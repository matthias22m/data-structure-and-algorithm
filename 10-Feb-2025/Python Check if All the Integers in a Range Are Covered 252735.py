# Problem: Python Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        sets = []
        union = set()
        for ls in ranges:
            range_set = set(range(ls[0],ls[1]+1))
            union = union | range_set

        if union.issuperset(set(range(left,right+1))):
            return True
            
        return False