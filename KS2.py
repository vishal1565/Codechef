for _ in range(int(input())):
    n = [int(i) for i in input()]
    res = sum(n)%10
    print(*n,(10-res)%10,sep='')