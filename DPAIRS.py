n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a1, b1 = [], []
for i in range(n):a1.append([a[i],i])
for i in range(m):b1.append([b[i],i])
a1.sort()
b1.sort()
count, shift = n+m-1, 0
if n>=m:
    while count!=0:
        for i in range(m):
            print(a1[shift+i][1],b1[i][1])
            count -= 1
            if count==0:
                break
        shift += 1
else:
    while count!=0:
        for i in range(n):
            print(a1[i][1],b1[shift+i][1])
            count -= 1
            if count==0:
                break
        shift += 1