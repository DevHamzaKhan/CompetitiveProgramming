jj = input().split()
n = int(jj[0])
q = int(jj[1])
a = list(map(int, input().split()))

f = []
for i in range(1, n + 2):
    f.append(0)
for aa in a:
    f[aa] += 1
def update(x, y):
    old_val = a[x - 1]
    if old_val != y:
        f[old_val] -= 1
        f[y] += 1
    a[x - 1] = y
def hq(l, r):
    inside = set()
    for i in range(l - 1, r):
        inside.add(a[i])
    for i in range(1, n + 1):
        if i not in inside:
            print(i)
            return
for zz in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        y = query[2]
        update(x, y)
    elif query[0] == 2:
        l = query[1]
        r = query[2]
        hq(l, r)