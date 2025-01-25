jj = input().split()
n = int(jj[0])
q = int(jj[1])
l = input().split()

for i in range(n):
    l[i] = int(l[i])

for j in range(q):
    x = input().split()
    
    if x[0] == "1":
        l[int(x[1]) - 1] = int(x[2])
    
    if x[0] == "2":
        l_idx = int(x[1]) - 1  
        r_idx = int(x[2]) - 1 

        inside = []
        for i in range(l_idx, r_idx+1):
            inside.append(int(l[i]))
        for i in range(1, n+1):
            if int(i) not in inside:
                print(i)
                break