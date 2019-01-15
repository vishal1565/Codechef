for _ in range(int(input())):
    n, p = [int(i) for i in input().split()]
    if n<=2:
        print(p*p*p)
    else:
        res = (p-(n-1)//2)*(p-(n-1)//2)
        res += (p-(n-1)//2)*(p-n)
        res += (p-n)*(p-n)
        print(res)