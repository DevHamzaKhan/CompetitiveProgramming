

a = int(input())
for i in range(a):
    x = input().split()
    b = int(x[0])
    n = int(x[1])
    s = input().split()
    s = list(map(int, s))
    occ = max(s)
    ans = 0
    pdanger = 10000000
    pcost = 10000000
    for j in range(0, occ+1):
        num = 0
        dang = 0
        for k in s:
            if k > j:
                num += k-j
            else:
                dang += j-k
        if num <= b:
            if (dang < pdanger):
                ans = j
                pcost = num
                pdanger = dang
            if (dang == pdanger):
                if (num < pcost):
                    pcost = num
                    pdanger = dang
                    ans = j
                    
    print(ans)