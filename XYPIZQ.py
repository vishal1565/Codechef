from math import gcd
for _ in range(int(input())):
    n, t, x, y, z = [int(i) for i in input().split()]
    if t==1:
        if x<y and y<=z:
            print("Condition 1")
            g = gcd(2*n-y, 2*n+1)
            print((2*n-y)//g, (2*n+1)//g)
        elif x<y and y>z:
            g = gcd(y-1, 2*n+1)
            print((y-1)//g, (2*n+1)//g)
        elif x>=y and y<=z:
            g = gcd(y+1, 2*n+1)
            print((y+1)//g, (2*n+1)//g)
        elif x>=y and y>z:
            g = gcd(2*n-y+2, 2*n+1)
            print((2*n-y+2)//g, (2*n+1)//g)
        
    elif t==2:
        if x==z:
            print(0,2*n+1)
        else:
            g = gcd(2*n-2*y+1, 2*n+1)
            print((2*n-2*y+1)// g,(2*n+1)//g)
    
    elif t==3:
        if x<y and y<=z:
            g = gcd(2*n-y+2, 2*n+1)
            print((2*n-y+2)//g, (2*n+1)//g)
        elif x<y and y>z:
            g = gcd(y-1, 2*n+1)
            print((y-1)//g,(2*n+1)//g)
        elif x>=y and y<=z:
            g = gcd(y+1, 2*n+1)
            print((y+1)//g,(2*n+1)//g)
        elif x>=y and y>z:
            g = gcd(2*n-y, 2*n+1)
            print((2*n-y)//g,(2*n+1)//g)

    else:
        if x==z:
            print(0,2*n+1)
        else:
            g = gcd(2*n-2*y+1, 2*n+1)
            print((2*n-2*y+1)//g,(2*n+1)//g)