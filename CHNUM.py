for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    neg, pos = 0, 0
    for i in a:
        if i>0:pos += 1    
        else: neg += 1
    if neg== n or pos == n:
        print(n,n)
    else:
        if pos >= neg:
            print(pos,neg)
        else:
            print(neg,pos)