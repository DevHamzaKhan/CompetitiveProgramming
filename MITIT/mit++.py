n = int(input())
for z in range(n):
    x = int(input())
    l = input()
    i = 0
    valid = True
    
    while i < len(l):
        if l[i] == 'M':
            i += 1
            if i + 1 < len(l) and l[i] == 'I' and l[i + 1] == 'T':
                i += 2
                while i + 1 < len(l) and l[i] == 'I' and l[i + 1] == 'T':
                    i += 2
            else:
                valid = False
                break
        else:
            valid = False
            break
    if valid:
        print ("YES")
    else:
        print ("NO")