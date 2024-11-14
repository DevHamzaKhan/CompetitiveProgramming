t = int(input())
for i in range(t):
    n = int(input())
    if(n == 0):
        print("haha good one")
    elif(n>=180):
        print("canceled")
    else:
        print(int(n/10)*"berkeley"+"time")