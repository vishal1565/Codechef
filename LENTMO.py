for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    k = int(input())
    x = int(input())

    diff,xorAmt,s = [], [], sum(a)
    maxi, s1,s2 = 0, 0, 0
    for i in range(n):
        temp = a[i]^x
        xorAmt.append(temp)
        diff.append(temp-a[i])
    diff.sort(reverse = True)
    if k%2==0:
        for i, elem in enumerate(diff):
            s1 += elem
            if i%2==1:maxi = max(maxi,s1)
    else:
        for i,elem in enumerate(diff):
            s2 += elem
            maxi = max(maxi,s2)
    if n==k:
        print(max(sum(xorAmt),s))
    else:
        print(s+maxi)