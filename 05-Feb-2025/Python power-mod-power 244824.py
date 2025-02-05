# Problem: Python power-mod-power - https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

ls = []
for i in range(3):
    ls.append(int(input()))
print(pow(ls[0],ls[1]))
print(pow(ls[0],ls[1],ls[2]))  