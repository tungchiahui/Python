#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
n = int(input('请输入需要分解的正整数:'))         # 创建一个列表用来存放遍历出来的因数
lt = []
m = n      # 给n换个名字记录,便于打印时打印出用户输入的n

while n > 1:
    for i in range(2,n+1):
        if n % i == 0:
            n = n // i                # 记录下用最小因数分解后的n
            lt.append(str(i))       # 把i转换成str,存到列表,便于后面用join拼接字符串列表
            break                   # 找到一个最小的因数时,就跳出for in循环,开始下一次循环
if len(lt) == 1:
    print(m,'=','1 *',m)
else:
    s = '*'.join(lt)
    print(m,'=',s)