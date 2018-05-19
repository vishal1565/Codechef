t=int(input())
for k in range(t):
    n=int(input())
    a=list(map(int,input().strip().split(' ')))
    res=2*a[0]
    for i in range(1,n):
        res=res ^ (2*a[i])
    print(res)
