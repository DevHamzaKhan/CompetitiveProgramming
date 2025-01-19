n = int(input())
for j in range(n):
    x = int(input())
    l = input()
    good = True
    for i in range(len(l)-2):
        if(l[i]!= 'M' and l[i]!='I' and l[i]!='T'):
            good = False
            break
        if(l[i] == 'M'):
            if(l[i+1] != 'I'):
                good = False
                break
        if(l[i] == 'I'):
            if(l[i+1] != 'T'):
                good = False
                break
        if(l[i] == 'T'):
            if(l[i+1] != 'I' and l[i+1] != 'M'):
                good = False
                break
    if l[-3:] != "MIT" and l[-3:] != "TIT":
        good = False
    if good:
        print("YES")
    else:
        print("NO")
