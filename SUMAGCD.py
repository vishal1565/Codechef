from math import gcd, inf

for _ in range(int(input())):
    n = int(input())
    a = sorted(list(set([int(i) for i in input().split()])))
    n = len(a)
    left, right = [a[0]], [0 for i in range(n)]
    for i in range(1,n):
        left.append(gcd(a[i],left[i-1]))
    right[-1] = a[-1]
    for i in range(n-2,-1,-1):
        right[i] = gcd(a[i],right[i+1])
    if n==1:
        print(2*a[0])
        continue
    res = a[0]+right[1]
    for i in range(i,n-1):
        res = max(res,a[i]+gcd(left[i-1],right[i+1]))
    res = max(res,a[-1]+left[-2])
    print(res)