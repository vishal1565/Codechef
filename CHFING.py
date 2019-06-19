MOD = int(1e9+7)
for _ in range(int(input())):
	n, k = [int(i) for i in input().split()]
	res = k-1
	if n<k:
		k -= n
		n -= 1
		res += k+(k*(k//n))
		res -= n*(((k//n)*((k//n)+1))>>1)
	print(res%MOD)