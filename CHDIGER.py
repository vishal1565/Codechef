    def newNumber(n,d,i):
        newNum = list(str(n)+str(d))
        newNum.remove(str(i))
        newNum = ''.join(newNum)
        return int(newNum)

    for _ in range(int(input())):
        num, d = [int(i) for i in input().split()]
        while True:
            digits, flag = sorted(list(str(num)),reverse = True), False
            for i in digits:
                newNum = newNumber(num,d,i)
                if newNum < num:
                    num, flag = newNum, True
                    break
            if not flag:break
        print(num)
