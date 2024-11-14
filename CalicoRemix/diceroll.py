n = int(input())
for i in range(n):
    x = int(input())
    l = [int(x) for x in input().split()]  
    ul = []
    for i in l:
        if (i not in ul):
            ul.append(i)
    nal = 0
    x = 0
    ans = 0
    for i in ul:
        s = 0
        for j in l:
            if j != i:
                s += j
        s = s/(len(l))
        if (nal == 0):
            x = s
            ans = i
            nal = 2
        if (s < x):
            x = s
            ans = i
    print(ans)

            
