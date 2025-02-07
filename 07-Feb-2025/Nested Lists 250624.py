# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        scores.append([name,score])
            
    scores.sort(key= lambda sc: sc[1])
    
    low = scores[0][1]
    snd = 0
    flag = True
    names = []
    for name, sc in scores:
        if sc > low and flag:
            names.append(name)
            snd = sc
            flag =False
        else:
            if snd == sc:
                names.append(name)
    names.sort()
    for name in names:
        print(name)