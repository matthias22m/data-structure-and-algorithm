# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n , m = map(int,input().split())
ls1 = [int(i) for i in input().split()]
ls2 = [int(i) for i in input().split()]
ans = []
ind = 0
for num in ls2:
    while ind<len(ls1) and num > ls1[ind]:
        ind+=1
    ans.append(ind)
print(*ans)