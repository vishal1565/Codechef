from math import floor
for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.insert(0,-1)
    total, res = 0, -1
    for i in range(1,n+1):
        total = sum([floor(element/(j+1)) for j,element in enumerate(a[i:n+1])])
        if total <= k:
            res = i
            break
    if res == -1:
        print(n+1)
    else:
        print(res)