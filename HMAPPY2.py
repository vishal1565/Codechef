def check(n,a,b,k):
    if a%b!=0 and b%a!=0:
        return ((n//a)+(n//b)-2*(n//(a*b)))
    elif a%b==0:
        return ((n//b)-(n//a))
    elif b%a==0:
        return ((n//a)-(n//b))

t = int(input())
for _ in range(t):
    n, a, b, k = [int(i) for i in input().split()]
    if check(n,a,b,k)>=k:
        print("Win")
    else:
        print("Lose")
