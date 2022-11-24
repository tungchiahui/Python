#判断101-180之间有多少个素数，并输出所有素数。
for i in range(101,180+1):
    a=2
    while a < i:
        if i % a == 0 :
            break
        else :
            a=a+1
    if a == i:
        print(i)