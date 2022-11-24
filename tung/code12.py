#找出错误，并重新写出正确的答案（共有五处错误，修改每个错误得2分，修改不对扣1分，直到扣没为止。）:
#使用函数求素数和
#prime(p), 其中函数prime当用户传入参数p为素数时返回True，否则返回False.
#PrimeSum(m,n),函数PrimeSum返回区间[m, n]内所有素数的和。题目保证1用户传入的参数1<=m<n。然后调用函数计算在[7,46]内所有素数之和。

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


