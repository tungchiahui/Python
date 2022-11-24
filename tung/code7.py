#输出 9*9 乘法口诀表。
for i in range(1, 10):
    print("\n")
    for j in range(1, i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j)+"\t",end = "")