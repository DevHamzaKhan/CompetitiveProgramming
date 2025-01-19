l = []
for i in range(25):
    l.append(5**i)
n = int(input())
for i in range(n):
    x = int(input())
    ans = "MIT time"
    for j in range(24, 0, -1):
        if(x > l[j]):
            ans = "MIT^" + str(j+1) + " time"
            break
    print(ans)