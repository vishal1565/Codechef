t = int(input())
for _ in range(t):
    n = int(input())
    dishes,count = [],0
    for i in range(n):
        tmp = [0 for i in range(26)]
        temp = list(input())
        for i in temp:
            tmp[ord(i)-97] = 1
        dishes.append(tmp)
    temp = dishes[0]
    for i in range(1,n):
        for j in range(26):
            temp[j] = temp[j] and dishes[i][j]
    print(sum(temp))
