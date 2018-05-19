t=int(input())
while t>0:
    m,n=[int(i) for i in input().split()]
    A=[int(i) for i in input().split()]
    B=[int(i) for i in input().split()]
    div=1000000007
    fib=[(1,0),(0,1)]
    for i in range(2,100001):
        fib.append(((fib[i-1][0]+fib[i-2][0])%div,(fib[i-1][1]+fib[i-2][1])%div))
    res=0
    for i in range(m):
        res+=(A[i]*fib[n-1][0]+B[i]*fib[n-1][1])%div
    res=res*m
    res=res%div
    print(res)

    t-=1
