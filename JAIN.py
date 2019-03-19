def returnVal(x):
    if x=='a':return 1
    elif x=='e':return 2
    elif x=='i':return 4
    elif x=='o':return 8
    else:return 16

for _ in range(int(input())):
    n = int(input())
    dish, table = [], [0]*32
    for i in range(n):
        tmp = set(input())
        t = 0
        tmp = ''.join(sorted(''.join(tmp)))
        for j in tmp:t+=returnVal(j)
        table[t] += 1
        dish.append(tmp)
    res = 0
    for i in range(31):
        for j in range(i+1,32):
            if i | j ==31:
                res += table[i]*table[j]
    res += (table[31]*(table[31]-1))//2
    print(res)
