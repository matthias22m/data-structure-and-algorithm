# Problem: Union of Arrays with Duplicates - https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        union = set(a) | set(b)
        return len(union)