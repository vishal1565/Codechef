t=int(input())
while t>0 :
    n,k=[int(i) for i in input().split(' ')]
    a=[int(i) for i in input().split(' ')]
    motu = [a[2*i] for i in range((n+1)//2)]
    tomu = [a[2*i+1] for i in range(n//2)]
    diff=sum(tomu)-sum(motu)
    if diff>0 :
        print("YES")
    else:
        diff=abs(diff)
        motu.sort(reverse=True)
        tomu.sort()
        temp=0
        flag=False
        for i in range(min(k,len(tomu))):
            temp+=2*(motu[i]-tomu[i])
            if temp>diff:
                flag=True
                print("YES")
                break;
        if not flag :
            print("NO")
        #print("YES")
    t-=1
