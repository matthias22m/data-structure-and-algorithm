# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from collections import defaultdict
from math import sqrt


def primeFactorCounter(num,_dict):
    while num % 2 == 0:
        _dict[2]+=1
        num = num / 2
        
    for i in range(3,int(sqrt(num))+1,2):
        while num % i== 0:
            _dict[i]+=1
            num = num / i
    if num > 2:
        _dict[num]+=1

for _ in range(int(input())):
    ln = int(input())
    _dict = defaultdict(int)
    nums = list(map(int,input().split()))

    for num in nums:
        primeFactorCounter(num,_dict)
    
    for _, val in _dict.items():
        if val%ln != 0:
            print('NO')
            break

    else:
        print('YES')