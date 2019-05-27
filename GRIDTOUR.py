from math import gcd
def checkTour(n,m,k):
    if m==1 and n==1:
        return 1
    elif gcd(k,m)!=1:
        return -1
    elif gcd(k,n)!=1:
        return -1
    else:
        return n*m
        
for _ in range(int(input())):
    n, m, k  = [int(i) for i in input().split()]
    print(checkTour(n,m,k))
