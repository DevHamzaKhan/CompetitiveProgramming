jj = input().split()
n = int(jj[0])
q = int(jj[1])
a = list(map(int, input().split()))

f = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    f[a[i]][i + 1] += 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        f[j][i] += f[j][i - 1]

def hq(l, r):
    for i in range(1, n + 1):
        c = f[i][r] - f[i][l - 1]
        if c == 0:
            print(i)
            return

for aaa in range(q):
    x = list(map(int, input().split()))
    if x[0] == 2:
        l = x[1]
        r = x[2]
        hq(l, r)