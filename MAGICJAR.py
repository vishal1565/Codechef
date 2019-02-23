t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    res = 0
    for i in range(n):
        res += a[i]-1
    print(res+1)
