t=int(input())
while t>0:
    x1,x2,x3,v1,v2=[int(i) for i in input().split()]
    if (abs(x1-x3))/v1 > (abs(x2-x3))/v2:
        print("Kefa")
    elif (abs(x1-x3))/v1 < (abs(x2-x3))/v2:
        print("Chef")
    else:
        print("Draw")
    t-=1
