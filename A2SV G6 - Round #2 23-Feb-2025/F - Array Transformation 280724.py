# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
from math import inf

for _ in range(int(input())):
    ln = int(input())
    ls = [int(i) for i in input().split()]
    cnt = Counter(ls)
    freq = list(cnt.values())
    unique = set(freq)
    _min = inf
    for f in unique:
        count = 0
        for f2 in freq:
            if f > f2:
                count += f2
            else:
                count += f2 - f
        _min = min(_min,count)

    print(_min)