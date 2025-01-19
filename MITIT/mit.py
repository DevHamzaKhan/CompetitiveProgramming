t = int(input())
for _ in range(t):
    s = int(input())
    l = input()
    good = True
    for i in range(len(l)-2):
        if l[i] == "M" and l[i+1:i+3] != "IT":
            good = False
            break
        if(l[i]!= 'M' and l[i]!='I' and l[i]!='T'):
            good = False
            break
        if l[i] == "T" and l[i+1:i+3] != "IT" and l[i+1] != "M":
            good = False
            break
    if l[-2:] != "IT":
        good = False
    if good:
        print("YES")
    else:
        print("NO")