# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    # Write your code here
    ans = [0]*100
    for i in arr:
        ans[i] += 1
        
    return ans
