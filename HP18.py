t = int(input())
for _ in range(t):
    n, a, b = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    count,countB, countA = 0,0,0
    for i in arr:
        if i%(a*b)==0:
            count+=1
        elif i%a==0:
            countA+=1
        elif i%b ==0:
            countB+=1
# BOB plays first

    if count!=0:
        # BOB deletes the set of multiples of a*b
        # Next turn ALICE
        if countA>=countB:
            print("BOB")
        else:
            print("ALICE")
    
    else:
        # BOB and ALICE one number at a time
        if countA<=countB:
            print("ALICE")
        else:
            print("BOB")