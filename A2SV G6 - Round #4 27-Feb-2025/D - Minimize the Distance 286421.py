# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

from math import inf


n = int(input())
ls = [int(i) for i in input().split()]
ls.sort()
if n%2 == 0:
    n -= 1
print(ls[n//2])