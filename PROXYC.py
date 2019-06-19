from math import ceil
for _ in range(int(input())):
    d = int(input())
    s = list(input())
    count, present = 0, s.count('P')
    for i in range(2,d-2):
        if s[i]=='A' and (s[i-1]=='P' or s[i-2]=='P') and (s[i+1]=='P' or s[i+2]=='P'):
            count += 1
    res = (3*d-4*present)/4
    if count >= res:
        print(max(int(ceil(res)),0))
    else:print(-1)