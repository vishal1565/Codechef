from collections import Counter
def checkDPS(st):
    even, odd = 0, 0
    c = Counter(st)
    for i in c.keys():
        if c[i]%2 == 0:even += 1
        else: odd += 1
    if len(st)%2 == 0:
        if odd == 2:
            return 'DPS'
        else: return '!DPS'
    else:
        if odd == 0 or odd == 1 or odd == 3:
            return 'DPS'
        else:
            return '!DPS'

for _ in range(int(input())):
    st = input()
    print(checkDPS(st))
