from math import ceil

def insertElement(target, arr):
    start,end = 0,len(arr)-1
    while end-start>0:
        mid = (start+end)//2
        if arr[mid]>target:
            end = mid
        else:
            start = mid+1
    if len(arr)>start and arr[start]<target:start += 1
    arr.insert(start,target)

t = int(input())
for _ in range(t):
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    count = 0

    for i in range(n):
        sub, freq = [], [0]*2001
        for j in range(i,n):
            insertElement(a[j],sub)
            freq[a[j]] += 1
            temp = (k-1)//(ceil(k/(j-i+1)))
            f = freq[sub[temp]]
            if f<2001 and freq[f]>0:
                count += 1
    print(count)