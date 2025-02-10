# Problem: Array Subset - https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

from collections import Counter


class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        if not set(b).issubset(set(a)):
            return False
        
        cnt_a = Counter(a)
        cnt_b = Counter(b)
        
        for cnt in cnt_b:
            if cnt_b[cnt] > cnt_a[cnt]:
                return False
        
        return True
    