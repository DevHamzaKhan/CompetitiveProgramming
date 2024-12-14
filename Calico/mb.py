a = int(input()) 
for i in range(a):
    x = input().split() 
    b = int(x[0]) 
    n = int(x[1]) 
    s = list(map(int, input().split()))  

    occ = max(s)
    
    prefix_danger = [0] * (occ + 1)
    prefix_cost = [0] * (occ + 1)
    
    for si in s:
        for j in range(si):
            prefix_danger[j] += si - j  
        for j in range(si, occ + 1):
            prefix_cost[j] += j - si  
    
    best_height = -1
    min_danger = float('inf')
    min_cost = float('inf')

    for j in range(occ + 1):
        if prefix_cost[j] > b:
            continue
        if prefix_danger[j] < min_danger or (prefix_danger[j] == min_danger and prefix_cost[j] < min_cost):
            min_danger = prefix_danger[j]
            min_cost = prefix_cost[j]
            best_height = j

    print(best_height)
