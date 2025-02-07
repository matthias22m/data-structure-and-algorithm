# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    _list = []
    for _ in range(N):
        _input = [i for i in input().split()]
        if _input[0] == 'insert':
            num,ind = int(_input[-1]),int(_input[-2])
            _list.insert(ind,num)
        elif _input[0] == 'append':
            num = int(_input[-1])
            _list.append(num)
        elif _input[0] == 'pop':
            _list.pop()
        elif _input[0] == 'remove':
            num = int(_input[-1])
            _list.remove(num)
        elif _input[0] == 'sort':
            _list.sort()
        elif _input[0] == 'reverse':
            _list = _list[::-1]
        elif _input[0] == 'print':
            print(_list)
            