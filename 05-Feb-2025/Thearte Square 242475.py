# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

from math import ceil

n , m , a = map(int,input().split())

vertical = ceil(n/a)
horizontal = ceil(m/a)

print(vertical*horizontal)