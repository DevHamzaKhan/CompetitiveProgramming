n = int(input())
for i in range(n):
    x = int(input())
    l = [int(x) for x in input().split()]  
    ul = []
    oc = {}
    for i in l:
        if (i not in ul):
            oc[i] = i
            ul.append(i)
        else:
            oc[i] += i
    xa = 0
    na = 0
    for key in oc:
        if (oc[key] > xa) :
            na = key
            xa = oc[key]
    print(na)

            
