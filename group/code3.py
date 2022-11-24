#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

h = 100
one_x = h
x = one_x
sum = one_x        #第一次直接被计算进总和中
for i in range(10):
    x = x / 2
    sum = sum + 2 * x
sum = sum - 2 * x     #减掉第10次的距离
print(sum,x)