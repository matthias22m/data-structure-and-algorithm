# Problem: Presents - https://codeforces.com/problemset/problem/136/A

num_people = int(input())
people = [int(p) for p in input().split()]

_dict = {}

for ind, g in enumerate(people):
    _dict[g] = ind + 1

ans = []

for i in range(num_people):
    ans.append(str(_dict[i+1]))

print(' '.join(ans))