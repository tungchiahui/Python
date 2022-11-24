#输入三个整数x,y,z，请把这三个数由小到大输出。
a = [] 
for i in range(3): 
    x = int(input('请输入第'+str(i+1)+"个整数:")) 
    a.append(x) 
a.sort()                            #给列表排序，此函数有两个入口参数，是否区分大小写和倒序/正序
print(a[0],"<",a[1],"<",a[2])