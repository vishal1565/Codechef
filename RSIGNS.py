MOD = int(1e9+7)
for _ in range(int(input())):
    k = int(input())-1
    res, temp = 1, 2
    while k>0:
        if k%2==1:
            res = (res%MOD * temp%MOD)%MOD
        k >>= 1
        temp = (temp%MOD * temp%MOD)%MOD
    res = (10*res)%MOD
    print(res)