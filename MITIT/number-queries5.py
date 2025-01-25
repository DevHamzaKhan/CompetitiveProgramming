N, Q = map(int, input().split())
a = list(map(int, input().split()))
f = [0] * (N + 1)

for n in a:
    f[n] += 1

for _ in range(Q):
    q = list(map(int, input().split()))
    
    if q[0] == 1:
        x, y = q[1] - 1, q[2]
        o = a[x]
        a[x] = y
        f[o] -= 1
        f[y] += 1
        
    elif q[0] == 2:
        l, r = q[1] - 1, q[2] - 1
        s = set(a[l:r+1])
        for num in range(1, N + 1):-
            if num not in s:
                print(num)
                break