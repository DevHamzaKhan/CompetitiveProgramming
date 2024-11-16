cases = int(input())
for c in range(cases):
    n = int(input())
    print((2**(n//3 + 1) - 2) % 3359232)