jj = input().split()
n = int(jj[0])
q = int(jj[1])
a = list(map(int, input().split()))

def handle_query(l, r):
    inside = set(a[l - 1: r])
    for i in range(1, n + 1):
        if i not in inside:
            print(i)
            return

for z in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 2:
        l = query[1]
        r = query[2]
        handle_query(l, r)