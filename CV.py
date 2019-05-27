vowels = ['a','e','i','o','u']
for _ in range(int(input())):
    n = int(input())
    st = list(input())
    count = 0
    for i in range(1,n):
        if st[i] in vowels:
            if st[i-1] not in vowels:
                count += 1
    print(count)
