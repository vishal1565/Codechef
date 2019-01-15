def normalGrid(n, m):
    res, temp, temp1, temp2, temp3 = [], [], [], [], []
    for i in range(m):
        if i%4<=1:
            temp.append(1)
            temp1.append(3)
            temp2.append(2)
            temp3.append(4)
        else:
            temp.append(2)
            temp1.append(4)
            temp2.append(1)
            temp3.append(3)
    for i in range(n):
        if i%4==0:res.append(temp)
        elif i%4==1:res.append(temp1)
        elif i%4==2:res.append(temp2)
        else:res.append(temp3)
    for i in res:
        print(*i)

def grid23(n, m):
    temp, temp1 = [], []
    for i in range(m):
        if i%6==0 or i%6==1:temp.append(1)
        elif i%6==2 or i%6==3:temp.append(2)
        else:temp.append(3)
    for i in range(m):
        if i%6==0 or i%6==5:temp1.append(2)
        elif i%6==1 or i%6==2:temp1.append(3)
        else:temp1.append(1)
    print(*temp)
    print(*temp1)

def grid32(n, m):
    t1, t2, t3, t4, t5, t6 = [1,2], [1,3], [2,3], [2,1], [3,1], [3,2]
    for i in range(n):
        if i%6==0:print(*t1)
        elif i%6==1:print(*t2)
        elif i%6==2:print(*t3)
        elif i%6==3:print(*t4)
        elif i%6==4:print(*t5)
        else:print(*t6)

for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    
    if n>=3 and m>=3:
        print("4")
        normalGrid(n, m)
    elif n==1:
        if m==1:
            print("1\n1")  #printing done
        elif m==2:
            print("1\n1 1") #printing done
        elif m>=3:
            print("2")      #printing done
            res = []
            for i in range(m):
                if i%4==0 or i%4==1:res.append(1)
                else:res.append(2)
            print(*res)
    
    elif n==2:
        if m==1:
            print(1)        #printing done
            print("1\n1")
        elif m==2:
            print(2)        #printing done
            print("1 1\n2 2")
        elif m>=3:
            print("3")
            grid23(n,m)
    
    elif n>=3:
        if m==1:
            print("2")      #printing done
            res, temp, temp1 = [], [1], [2]
            for i in range(n):
                if i%4==1 or i%4==0:res.append(temp)
                else:res.append(temp1)
            for i in res:print(*i)
        elif m==2:
            print("3")
            grid32(n,m)