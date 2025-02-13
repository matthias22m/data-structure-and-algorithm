# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

from math import inf


for _ in range(int(input())):
    ln = int(input())
    ls = [int(i) for i in input().split()]
    neg = False if ls[0] >0 else True
    _sum = 0
    
    right = 0
    while right < len(ls):
        if neg:
            cur = -inf
            while right < len(ls) and ls[right] < 0:
                cur = max(cur,ls[right])
                right+=1
            neg = False
        else:
            cur = 0
            while right < len(ls) and ls[right] > 0:
                cur = max(cur,ls[right])
                right+=1
            neg = True
        
        _sum+=cur
    print(_sum)