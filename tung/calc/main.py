#main.py
#创建一个项目名为calc的包结构，并且创建两个包，包名分别是addsub和muldiv
#第一个包负责定义加法减法函数，第二个包负责定义乘法除法函数
#并在入口程序（类似于主函数）中套用两个包中的模块来达到2个整数之间的加减乘除的运算
import addsub.function1
from muldiv import function2
formula = input("请输入算式：").split()
formula[0] = int(formula[0])
formula[2] = int(formula[2])
if formula[1] == "+":
    result = addsub.function1.add(formula[0],formula[2])
    print("计算结果是："+str(formula[0])+formula[1]+str(formula[2])+"="+str(result))
if formula[1] == "-":
    result = addsub.function1.sub(formula[0],formula[2])
    print("计算结果是："+str(formula[0])+formula[1]+str(formula[2])+"="+str(result))
if formula[1] == "*":
    result = function2.mul(formula[0],formula[2])
    print("计算结果是："+str(formula[0])+formula[1]+str(formula[2])+"="+str(result))
if formula[1] == "/":
    result = function2.div(formula[0],formula[2])
    print("计算结果是："+str(formula[0])+formula[1]+str(formula[2])+"="+str(result))