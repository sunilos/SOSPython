# Example of simple Try Catch Exception
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

try:  
    num1 = int(input("Enter First Number: "))  
    num2 = int(input("Enter Second Number: "))  
    num3 = num1/num2;  
    print("num1/num2 = ",num3)  
except Exception:  
    print("can't divide by zero")  
else:  
    print("Hi I am else block")   

