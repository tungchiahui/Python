#求1+2!+3!+...+21!的和。
sum = 0
t = 1
for n in range(1,21+1):
    t = t * n
    sum = sum + t
print(sum)