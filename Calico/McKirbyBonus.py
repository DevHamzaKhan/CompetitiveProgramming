a = int(input())
for i in range(a):
    x = input().split()
    b = int(x[0])
    n = int(x[1])
    s = list(map(int, input().split()))
    occ = max(s) 
    s.sort() 
    ps = [0] * (n+1)
    for j in range(1, len(s)):
        ps[j] = s[j] + ps[j-1]
    ds = [0] * (n+1)
    for j in range(len(s)-1, -1, -1):
        ds[j] = ds[j+1] + s[j]
        
    ans = 0
    pdanger = float('inf')
    pcost = float('inf')
    
    for j in range(occ+1):
        print(ds[j], ps[j])
        
    print(ans)