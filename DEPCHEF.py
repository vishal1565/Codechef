def chooseSoldier(n,attack,defense):
    res = []
    for i in range(n):
        if defense[i]>attack[(i+1)%n]+attack[i-1]:
            res.append(defense[i])
    if len(res)==0:
        return -1
    else:
        return max(res)

t = int(input())
for _ in range(t):
    n = int(input())
    attack = [int(i) for i in input().split()]
    defense = [int(i) for i in input().split()]
    print(chooseSoldier(n,attack,defense))
