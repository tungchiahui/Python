#main.py
def prime(p):
    if p == 1:
        return False
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

def PrimeSum(m, n):
    sums = 0
    for i in  range(m, n + 1):
        if prime(i) == True:
            sums += i
    return sums

a = int(input("请输入范围值m:"))
b = int(input("请输入范围值n:"))
m = PrimeSum(a,b)
print(m)










def prime(p):
    if p == 1:
        return False
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

def PrimeSum(m, n):
    sums = 0
    for i in  range(m, n):      #第一处错误
        if prime(i) == True:
            sums += i
    print(sums)                    #第二处错误

a = int(input(请输入范围值m:))         #第三处错误
b = int(input(请输入范围值n:))         #第四处错误
m = PrimeSum(a,b)
printf(m)                               #第五处错误