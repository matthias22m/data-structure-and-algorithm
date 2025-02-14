# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import Counter


n , k = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

longest = 0
indexes = []
window = Counter()
left = 0
for right in range(n):
    window[nums[right]] += 1
    if len(window) > k:
        while len(window) > k:
            window[nums[left]] -= 1
            if window[nums[left]] == 0:
                del window[nums[left]]
            left+=1

    if right-left+1 > longest:
        longest = max(right-left+1,longest)
        indexes = [left+1,right+1]

print(*indexes)
